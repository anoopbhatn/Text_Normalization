from flask import Flask, redirect, url_for, request

from flask import json

from gtts import gTTS

import time

import json

import commands

import tensorflow as tf

from flask_cors import CORS



status, ip = commands.getstatusoutput("hostname -I")

# ip = os.system('hostname -I')
ip=ip.strip().split(' ')
ip=ip[0]
print 'ip',ip
from src.main.python.TextNormalization.main import TextNormalization

classList = [className.strip() for className in tuple(open("classList.txt", 'r'))]

nt = TextNormalization(classList)
graph = tf.get_default_graph()

def normalizefun(line):
	outputStr = ''
	for inputStr in line:
		print 'weird',inputStr
		try:
			outputStrPart = nt.modelFinal(inputStr).strip().strip('"')
		except:
			outputStrPart = 'error'
		print 'in between',outputStrPart
		outputStr += outputStrPart + ' '
	print outputStr
	return outputStr

def normalize(inputWhole):

	lines = inputWhole.split('\n')

	inputList = [inputStr.strip().split(' ') for inputStr in lines]
	inputList = [[str(s) for s in sublist] for sublist in inputList]
	
	print inputList,'initial'

	outputList=[]

	for line in range(len(inputList)):
		outDict={}
		print 'hello',lines[line]
		global graph
		with graph.as_default():
			outline = normalizefun(inputList[line])
		print 'world',outline
		speechObj = gTTS(text=outline, lang='en', slow=False)
		filename=int(time.time())
		speechObj.save("../../Server-instance/speech/"+str(filename)+".mp3")
		outDict["id"]=line+1
		outDict["before"]=lines[line]
		outDict["speech"]="http://"+ip+":8080/speech/"+str(filename)+".mp3"
		outputList.append(outDict)
	return outputList

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

textAndSpeech=[]

@app.route('/get', methods=['GET'])
def sendNormalized():
	print textAndSpeech
	return json.dumps(textAndSpeech)


@app.route('/post', methods=['GET', 'POST'])
def getData():
	if request.method == 'POST':
		textToBeNormalized = request.form['textToBeNormalized']
		fileHandle = open('input.txt','w')
		fileHandle.write(textToBeNormalized)
		global textAndSpeech
		textAndSpeech = normalize(textToBeNormalized)
		return redirect("http://"+ip+":4200/afternormalize", code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)