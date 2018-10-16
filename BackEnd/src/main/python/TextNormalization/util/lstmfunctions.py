from imports import *


# Functions to fetch required properties for seq-to-seq lstm
def fetchLstmProperties(className):
	# Opens Properties File
	fileHandle = open("src/main/python/TextNormalization/properties/"+className+".properties","r")
	# Csv Reader object
	reader=csv.reader(fileHandle,delimiter='=')
	# Creating Dictionary to store properties
	propertiesDictionary=dict()
	# For every line / property create a key-value -> property-value pair
	for line in reader:
		propertiesDictionary[line[0]]=line[1]

	# The number of tokens for the encoder
	num_encoder_tokens = int(propertiesDictionary["num_encoder_tokens"])
	# The number of tokens for the decoder
	num_decoder_tokens = int(propertiesDictionary["num_decoder_tokens"])
	# The Maximum Sequence length of the encoder
	max_encoder_seq_length = int(propertiesDictionary["max_encoder_seq_length"])
	# The Maximum Sequence length of the decoder
	max_decoder_seq_length = int(propertiesDictionary["max_decoder_seq_length"])

	return num_encoder_tokens,num_decoder_tokens,max_encoder_seq_length,max_decoder_seq_length


# To fetch data pickled 
def fetchLstmData(className):
	# File handle for target_token_index
	fh1=open("src/main/python/TextNormalization/model/pickles/"+className+"/target_token_index.pkl","rb")
	# File handle for reverse_target_char_index 
	fh2=open("src/main/python/TextNormalization/model/pickles/"+className+"/reverse_target_char_index.pkl","rb")
	# File handle for input_token_index
	fh3=open("src/main/python/TextNormalization/model/pickles/"+className+"/input_token_index.pkl","rb")

	try:
		target_token_index = pickle.load(fh1)
	except:
		print className
	reverse_target_char_index = pickle.load(fh2)

	input_token_index = pickle.load(fh3)

	return target_token_index,reverse_target_char_index,input_token_index


# To load Encoder and Decoder models
def loadLstmModels(className):
	# Load Encoder Model
	with open('src/main/python/TextNormalization/model/json/'+className+'_encoder.json', 'r') as f:
		encoder_model = model_from_json(f.read())
	
	# Load Encoder weights
	encoder_model.load_weights('src/main/python/TextNormalization/model/weights/'+className+'_encoder_model_weights.h5')

	# Load Decoder Model
	with open('src/main/python/TextNormalization/model/json/'+className+'_decoder.json', 'r') as f:
		decoder_model = model_from_json(f.read())
	
	# Load Decoder Weights
	decoder_model.load_weights('src/main/python/TextNormalization/model/weights/'+className+'_decoder_model_weights.h5')

	return encoder_model , decoder_model


# To convert input string to numpy array
def textToArray(input_seq,num_encoder_tokens,max_encoder_seq_length,input_token_index):
	# If required - include " " in the string
	input_seq = '"'+input_seq+'"'
	
	# Array of zeros of desired dimensions
	encoder_input_data = np.zeros((1, max_encoder_seq_length, num_encoder_tokens),dtype='float32')

	# For every character, set 1.0 to corresponding character index
	for t,char in enumerate(input_seq):
		encoder_input_data[0][t][input_token_index[char]]=1.

	return encoder_input_data


# To decode the input sequence to get final output 
def decodeSequence(lstmProp, input_seq):

	encoder_model = lstmProp[7]
	decoder_model = lstmProp[8]
	num_encoder_tokens = lstmProp[0] 
	max_encoder_seq_length = lstmProp[2] 
	num_decoder_tokens = lstmProp[1]
	max_decoder_seq_length = lstmProp[3]
	target_token_index = lstmProp[4]
	input_token_index = lstmProp[6]
	reverse_target_char_index = lstmProp[5]

	# Convert input string - input_seq to numpy array
	input_seq = textToArray(input_seq,num_encoder_tokens,max_encoder_seq_length,input_token_index)
	
	# Encode the input as state vectors.
	states_value = encoder_model.predict(input_seq)
	
	# Generate empty target sequence of length 1.
	target_seq = np.zeros((1, 1, num_decoder_tokens))
    
    # Populate the first character of target sequence with the start character.
	target_seq[0, 0, target_token_index['\t']] = 1.

	# Sampling loop for a batch of sequences
	# (to simplify, here we assume a batch of size 1).
	stop_condition = False
	decoded_sentence = ''
	
	while not stop_condition:
		output_tokens, h, c = decoder_model.predict( [target_seq] + states_value )
		# Sample a token
		sampled_token_index = np.argmax(output_tokens[0, -1, :])
		sampled_char = reverse_target_char_index[sampled_token_index]
		
		decoded_sentence += sampled_char

		# Exit condition: either hit max length
		# or find stop character.
		if (sampled_char == '\n' or len(decoded_sentence) > max_decoder_seq_length):
			stop_condition = True
		
		# Update the target sequence (of length 1).
		target_seq = np.zeros((1, 1, num_decoder_tokens))
		target_seq[0, 0, sampled_token_index] = 1.

		# Update states
		states_value = [h, c]


	return decoded_sentence


# To fetch all models and properties of LSTM
def lstmConsolidate(classNames):

	classDictionary = dict()

	# For every class, do the following
	for className in classNames:
		# Fetch Properties
		num_encoder_tokens,num_decoder_tokens,max_encoder_seq_length,max_decoder_seq_length = fetchLstmProperties(className)

		# Fetch Pickled Data
		target_token_index,reverse_target_char_index,input_token_index = fetchLstmData(className)

		# Fetch encoder - decoder models
		encoder_model , decoder_model = loadLstmModels(className)

		# Creating a list for every class
		classList = list()

		# Appending properties, data and models in sequence to classList
		classList.append(num_encoder_tokens)
		classList.append(num_decoder_tokens)
		classList.append(max_encoder_seq_length)
		classList.append(max_decoder_seq_length)
		classList.append(target_token_index)
		classList.append(reverse_target_char_index)
		classList.append(input_token_index)
		classList.append(encoder_model)
		classList.append(decoder_model)

		classDictionary[className] = classList

	return classDictionary



months = {
			'1': 'January', '2': 'February','3': 'March', '4': 'April','5': 'May',
			'6': 'June', '7': 'July','8': 'August','9': 'September','10':'October',
			'11':'November','12':'December','01': 'January', '02': 'February','03': 'March',
			 '04': 'April','05': 'May','06': 'June', '07': 'July','08': 'August','09': 'September'
		}
