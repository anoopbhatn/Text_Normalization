# Importing all required in-built classes and models
from util.imports import *

# Import all functions related to lstm
from util.lstmfunctions import *

# Import all functions related to xgboost
from util.xgboostfunctions import *


class TextNormalization:

	lstmProperties = dict()

	electronicDict = { '.' : 'dot' , '/' : 'slash' , ':' : 'colon' }

	# File to store results
	# resultsFile = None

	def __init__(self,classNames):
		self.lstmProperties = lstmConsolidate(classNames)
		# self.resultsFile = open("resultsOverall.csv","a")

	def xgboostPredict(self,inputStr):
		return xgboostPrediction(inputStr) 

	def lstmPredict(self,lstmProp,inputStr):
		return decodeSequence(lstmProp,inputStr)

	def modelFinal(self,inputStr):
		# Predict the class of the input string
		className = self.xgboostPredict(inputStr).lower()

		resultsFile = open("resultsOverall.csv","a")

		resultsFile.write(className+','+inputStr+',')

		print className

		if className == "plain" or className == "punct":
			resultsFile.write(inputStr+'\n')
			return inputStr
		elif className == "date" and len(inputStr) > 4:
			date = inputStr.split('/')
			print date
			if int(date[1]) > 12:
				temp=date[0]
				date[0]=date[1]
				date[1]=date[0]
			outputSeq = str(num2words(int(date[0]), to='ordinal'))
			outputSeq += ' of ' + months[date[1]] + ' '
			outputSeq += self.lstmPredict(self.lstmProperties['date'],date[2]).strip('"')
			resultsFile.write(outputSeq+'\n')
			return outputSeq
		elif className == "electronic":
			outputSeq = ''
			for i in inputStr:
				if i in self.electronicDict:
					outputSeq += self.electronicDict[i] + ' '
				else:
					outputSeq += i + ' '
			resultsFile.write(outputSeq+'\n')
			return outputSeq

		# Fetch all the properties related to that class
		lstmClassProp = self.lstmProperties[className]

		# Write the predicted output to the results file
		predictedSeq = self.lstmPredict(lstmClassProp, inputStr)

		resultsFile.write(predictedSeq+'\n')

		return predictedSeq