#Copyright 2020 Ian McDowell
import math

#input being hex string of the format: 0x-------
#output being binary string
def hexToBin(hexNum):
	binNum = ''
	for num in hexNum.replace('0x', ''):
		binNum += decToBin(int(hexDigToDec(num)))
	return binNum

# def hexToDec(hexNum):

def hexDigToDec(hexDigit):
	hexLetters = ['A','B','C','D','E','F']
	hexNumbers = ['0','1','2','3','4','5','6','7','8','9',]
	if hexDigit in hexNumbers:
		return hexDigit
	elif hexDigit in hexLetters:
		convertedNum = 10
		for letter in hexLetters:
			if hexDigit == letter:
				return convertedNum
			else:
				convertedNum += 1

# def binToHex(binNum):

def binToDec(binNum):
	sumNum = 0
	currDigit = 0
	for digit in binNum:
		if digit == '1':
			sumNum += int(math.pow(2,(len(binNum)-currDigit-1)))
		currDigit += 1
	return sumNum

def decToBin(decimal):
	workNum = ''
	div = 8
	while div != 0:
		if int(decimal / div) > 0:
			workNum += '1'
			decimal -= div
		else:
			workNum += '0'
		div = int(div / 2)
	return workNum

#def decToHex(decNum):