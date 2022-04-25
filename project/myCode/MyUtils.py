#Given an hex string, transform it into an integer
def hexToInt(val):
	return int(val, 16)

#Given a data bloc as an hex string, we what to extract the sequence starting at "startPosOctet" (specified in octets) and being of length "nbOctets" (also specified in octets)
def extractSequence(dataBlock, startPosOctet, nbOctets):
	#let's first convert startPos and nbOctets in hex digits instead of octets (1 octet is 2 hex digits)
	startPosDigit = startPosOctet * 2
	nbDigits = nbOctets * 2
	if startPosDigit < 0:
		raise ValueError("Cannot extract a sequence from pos (" + str(startPosOctet)  + " octet) in any dataBlock.")
	if startPosDigit + nbDigits > len(dataBlock):
		raise ValueError("Cannot extract a sequence from pos (" + str(startPosOctet)  + " octet) with length (" + str(nbOctets) + ")  in a dataBlock of total lenght (" + str(len(dataBlock)/2) + ")." + dataBlock)
	return dataBlock[startPosDigit:startPosDigit + nbDigits]


#read a block from binary file and converts it to hex.
#filename, the file to read from
#offset, the position where to start reading given in octets (e.g., 0 means start, 100, means skip the first 99 octets)
#length, the number of octets to read
def readBlockFromFileInHex(fileName, offset, length):
	with open(fileName, "rb") as file:
		content = file.read()
		file.close()
		content = content[offset: offset+length]
		hexa = []
		for x in content:
			hexa.append(hex(x)[2:].zfill(2))
		return "".join(hexa).upper()
