from imports import *

def fetchXgboostProperties():
	# Opens Properties File
	fileHandle = open("src/main/python/TextNormalization/properties/xgboost_model.properties","r")
	# Csv Reader object
	reader=csv.reader(fileHandle,delimiter='=')
	# Creating Dictionary to store properties
	propertiesDictionary=dict()
	# For every line / property create a key-value -> property-value pair
	for line in reader:
		propertiesDictionary[line[0]]=line[1]

	# Maximum number of features
	max_num_features = int(propertiesDictionary["max_num_features"])

	pad_size = int(propertiesDictionary["pad_size"])

	boundary_letter = int(propertiesDictionary["boundary_letter"])

	space_letter = int(propertiesDictionary["space_letter"])

	return max_num_features,pad_size,boundary_letter,space_letter


def fetchXgboostData():
	# Fetch stored labels
	labelsHandle = open("src/main/python/TextNormalization/model/pickles/xgboost_pickles/labels.pkl","rb")

	labels = pickle.load(labelsHandle)

	return labels


def loadXgboostModel():
	# Fetch xgboost saved model
	xgboostHandle = open("src/main/python/TextNormalization/model/pickles/xgboost_pickles/xgboost_model.pkl")

	xgboost_model = pickle.load(xgboostHandle)

	return xgboost_model


def context_window_transform(data, pad_size, max_num_features, boundary_letter):

	pre = np.zeros(max_num_features)
	pre = [pre for x in np.arange(pad_size)]

	data = pre + data + pre
	neo_data = []

	for i in np.arange(len(data) - pad_size * 2):
		row = []
		for x in data[i : i + pad_size * 2 + 1]:
			row.append([boundary_letter])
			row.append(x)
		row.append([boundary_letter])
		neo_data.append([int(x) for y in row for x in y])

	return neo_data


def transformInput(inputText):
	# Fetch all properties
	max_num_features,pad_size,boundary_letter,space_letter = fetchXgboostProperties()
	# Array to store input in required format
	x_row = np.ones(max_num_features, dtype=int) * space_letter

	for xi, i in zip(list(str(inputText)), np.arange(max_num_features)):
		x_row[i] = ord(xi)

	x_row=[x_row]

	x_data = np.array(context_window_transform(x_row, pad_size, max_num_features,boundary_letter))
	
	x_data = np.array(x_data)

	dvalid = xgb.DMatrix(x_data)

	return dvalid


def xgboostPrediction(inputText):
	# Transform text to required form
	inp = transformInput(inputText)

	xgboost_model = loadXgboostModel()
	# Output will be index of the label 
	output = xgboost_model.predict(inp)

	# Load the saved labels data
	labels = fetchXgboostData()

	return labels[int(output[0])]