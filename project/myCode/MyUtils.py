#TODO remove for Students
#Given an integer val, transform it into a string in the specified base (supporting only binary and hex for now) with enough leading 0 to make the final string a total of "len" digits
#def intToBase(val, base, len):
#	if len < 1 :
#		raise ValueError("Cannot encode anything with a len (" + str(len) + ") less than 1.")
#	if val > base**len:
#		raise ValueError("The value ("+ str(val) + ") is too big to be encoded in the specified len (" + str(len) + ") in the given base (" + str(base) + "). ")
#	if val < 0 :
#		raise ValueError("Cannot encode negative value (" + str(val) + ")")
#	if base == 2:
#		return bin(val)[2:].zfill(len)
#	elif base == 16:
#		return hex(val)[2:].zfill(len).upper()
#	else:
#		raise ValueError("Conversion from int to base () is not yet supported. Lazy pro[f](grammer)")


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
		raise ValueError("Cannot extract a sequence from pos (" + str(startPosOctet)  + " octet) with length (" + str(nbOctets) + ")  in a dataBlock of total lenght (" + str(len(dataBlock)/2) + ").")
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

#TODO remove for Students
#Given a data block as an hex string, we fill it (with 0) until is has the given size of nbOctets
#def fillDataBlockUpTo(dataBlock, nbOctets):
#	if nbOctets < 1 :
#		raise ValueError("Cannot fill a dataBlock up to 0 or less octets. Currently requeted (" + str(nbOctets) + ") octets.")
#	if len(dataBlock) % 2 == 1: 
#		#dataBlock must be of even length because each octet is two hex digits
#		dataBlock = dataBlock + "0"
#	if len(dataBlock) / 2 > nbOctets:
#		raise ValueError("Cannot fill a dataBlock of (" + str(len(dataBlock)/2)  + ") octets to (" + str(nbOctets) + ") octets. Already too big.")
#	while len(dataBlock) / 2 < nbOctets:
#		dataBlock = dataBlock + "00"
#	return dataBlock
