from src.main.python.TextNormalization.main import TextNormalization

# from src.main.python.TextNormalization.api.api import *

classList = [className.strip() for className in tuple(open("classList.txt", 'r'))]

inputLists = [inputStr.strip().split(' ') for inputStr in tuple(open("input.txt", 'r'))]



nt = TextNormalization(classList)

print 'hello'

for inputList in inputLists:
	outputStr = ''
	for inputStr in inputList:
		outputStrPart = nt.modelFinal(inputStr).strip().strip('"')
		outputStr += outputStrPart + ' '
	print outputStr

