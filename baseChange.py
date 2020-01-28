#Copyright 2020 Ian McDowell
import math
from textwrap import wrap
HEX_LETTERS = ['A','B','C','D','E','F']
HEX_NUMBERS = ['0','1','2','3','4','5','6','7','8','9',]


#input being hex string of the format: 0x-------
#output being binary string
def hexToBin(hexNum):
	binNum = ''
	for digit in hexNum:
		binNum += decToBin(int(hexDigToDec(digit)))
	return binNum

def hexToDec(hexNum):
	return binToDec(hexToBin(hexNum))

def hexDigToDec(hexDigit):
	global HEX_LETTERS
	global HEX_NUMBERS
	if hexDigit in HEX_NUMBERS:
		return int(hexDigit)
	elif hexDigit in HEX_LETTERS:
		convertedNum = 10
		for letter in HEX_LETTERS:
			if hexDigit == letter:
				return convertedNum
			else:
				convertedNum += 1

def binToHex(binNum):
	hexNum = ''
	if len(binNum) % 4 != 0:
		binNum = ('0' * (4 -(len(binNum) % 4))) + binNum
	for binChunk in wrap(binNum,4):
		hexNum += decToHexDigit(str(binToDec(binChunk)))
	return hexNum

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

def decToHex(decNum):
	return binToHex(binToDec(decNum))

def decToHexDigit(decNum):
	global HEX_LETTERS
	global HEX_NUMBERS
	if decNum in HEX_NUMBERS:
		return decNum
	else:
		return HEX_LETTERS[int(decNum)-10]
