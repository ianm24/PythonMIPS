# Copyright 2020 Ian McDowell
# Started 24 Jan 2020
# get op code/instruction type 
# figure out rest of instruction
import baseChange
import csv,sys,math



MIPS_INSTRUCTION_LIST = 'MIPSInstructions.csv'
DELIM = ","


def hexToInstruction(hexNum):
	binNum = baseChange.hexToBin(hexNum)
	if '1' in binNum[:6]:
		# print('I-type')
		# opCode, rsSource, rtDestination, imm
		binInstruction = [binNum[0:6],binNum[6:11],binNum[11:16],binNum[16:]]
		# print(binInstruction)
		betweenInstruction = [binInstruction[0], baseChange.binToDec(binInstruction[1]),
		baseChange.binToDec(binInstruction[2]), baseChange.binToDec(binInstruction[3])]
		# print(betweenInstruction)
		preFormatInstruction = [getOpCode(baseChange.binToHex(binInstruction[0]),'None'), 
			getRegister(betweenInstruction[1]), getRegister(betweenInstruction[2]),
			betweenInstruction[3]]
		# print(preFormatInstruction)
		print('Hex Instruction: ' + str(hexNum) + '\nMIPS Instruction: ' 
			+ str(preFormatInstruction[0]) + ' ' + str(preFormatInstruction[2]) 
			+ ', ' + str(preFormatInstruction[1]) + ', ' + str(preFormatInstruction[3]))
	else:
		# print('R-type')
		# opCode, rsSource, rtSource, rdDestination, shiftAmount, functCode
		binInstruction = [binNum[0:6],binNum[6:11],binNum[11:16],binNum[16:21],
		binNum[21:26],'00' + binNum[26:]]
		# print(binInstruction)
		betweenInstruction = [baseChange.binToHex(binInstruction[0]),baseChange.binToDec(binInstruction[1]),
			baseChange.binToDec(binInstruction[2]),baseChange.binToDec(binInstruction[3]),
			baseChange.binToDec(binInstruction[4]),hexNum[6:]]
		# print(betweenInstruction)
		preFormatInstruction = [getOpCode(betweenInstruction[0],hexNum[6:]), 
			getRegister(betweenInstruction[1]), getRegister(betweenInstruction[2]),
			getRegister(betweenInstruction[3]), getRegister(betweenInstruction[4])]
		# print(preFormatInstruction)
		print('Hex Instruction: ' + str(hexNum) + '\nMIPS Instruction: ' 
			+ str(preFormatInstruction[0]) + ' ' + str(preFormatInstruction[3]) 
			+ ', ' + str(preFormatInstruction[1]) + ', ' + str(preFormatInstruction[2]))

		
def getOpCode(opHex, functHex):
	global MIPS_INSTRUCTION_LIST
	global DELIM
	csv_file = csv.reader(open(MIPS_INSTRUCTION_LIST,"r"), delimiter=DELIM)
	if functHex == 'None':
		for row in csv_file:
			if opHex == row[0]:
				return row[1]
	for row in csv_file:
		if opHex == row[0] and functHex == row[1]:
			return row[2]

def getRegister(decNum):
	if decNum == 0:
		return '$zero'
	elif decNum == 1:
		return '$at'
	elif (decNum > 1 and decNum < 4):
		return '$v' + str(decNum-2)
	elif (decNum > 3 and decNum < 8):
		return '$a' + str(decNum-4)
	elif (decNum > 7 and decNum < 16):
		return '$t' + str(decNum-8)
	elif (decNum > 15 and decNum < 24):
		return '$s' + str(decNum-16)
	elif (decNum > 23 and decNum < 26):
		return '$t' + str(decNum-24+8)
	elif (decNum > 25 and decNum < 28):
		return '$k' + str(decNum-26)
	elif decNum == 28:
		return '$gp'
	elif decNum == 29:
		return '$sp'
	elif decNum == 30:
		return '$fp'
	elif decNum == 31:
		return '$ra'
