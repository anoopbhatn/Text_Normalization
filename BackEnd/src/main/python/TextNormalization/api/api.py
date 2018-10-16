from flask import Flask, redirect, url_for, request

from flask import json

import os

ip = str(os.system('hostname -I'))

app = Flask(__name__)


@app.route('/get')
def sendNormalized():
	return textAndSpeech


@app.route('/post', methods=['GET', 'POST'])
def getData():
	if request.method == 'POST':
		textToBeNormalized = request.form['textToBeNormalized']
		fileHandle = open('input.txt','w')
		fileHandle.write(textToBeNormalized)
		return redirect("http://"+ip+":4200/afternormalize", code=302)


if __name__ == "__main__":
    app.run(debug=True)
	


   