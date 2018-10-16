from flask import Flask, redirect, url_for, request

from flask import json

from gtts import gTTS

import time

import os

import json

import commands

status, ip = commands.getstatusoutput("hostname -I")

# ip = os.system('hostname -I')
ip=ip.strip().split(' ')
ip=ip[0]
print 'ip',ip

from src.main.python.TextNormalization.main import TextNormalization

# from src.main.python.TextNormalization.api.api import *

classList = [className.strip() for className in tuple(open("classList.txt", 'r'))]

inputList = [inputStr.strip() for inputStr in tuple(open("input.txt", 'r'))]


def normalize(inputWhole):

	lines = inputWhole.split('\n')

	print lines

	outputList=[]

	for line in range(len(lines)):
		outDict={}
		speechObj = gTTS(text=lines[line], lang='en', slow=False)
		filename=int(time.time())
		speechObj.save("../../Server-instance/speech/"+str(filename)+".mp3")
		outDict["id"]=line+1
		outDict["before"]=lines[line]
		outDict["speech"]="http://"+ip+":8080/speech/"+str(filename)+".mp3"
		outputList.append(outDict)
	return outputList

app = Flask(__name__)


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
		os.system('python test.py')
		return redirect("http://"+ip+":4200/afternormalize", code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
	


   