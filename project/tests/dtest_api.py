import unittest
import requests
import json
from myAPI import api

IP = "0.0.0.0"
PORT = "5555"
URL = "http://" + IP + ":" + PORT

class APITest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		with open("./project/files/MemoryLayout1.vsml", "rb") as f:
			myFile = {'file':f}
			response = requests.post(URL + "/upload", files=myFile)
			if response.status_code != 200:
				print(response.content.decode())
				raise Exception("SetUpClass failed for APITest")


	def test_home(self):
		response = requests.get(URL + "/")
		self.assertEqual(200, response.status_code)

	def test_MetaRoute(self):
		response = requests.get(URL + "/metaInfo")
		self.assertEqual(200, response.status_code)
		map = json.loads(response.content.decode('utf-8'))
		map = map['metaInfo']
		self.assertEqual("4D4C4D4C", map['magicNumber'])
		self.assertEqual("56534D4C", map['memoryLayoutType'])

		self.assertEqual(16, map['pageSize'])
		self.assertEqual(64, map['nbPhysicalPages'])
		self.assertEqual(0, map['nbSwapPages'])
		self.assertEqual(1, map['nbBitmapPages'])
		self.assertEqual(2, map['nbPTPages'])
		self.assertEqual(1, map['nbPLTPages'])

	def test_BitmapRoute(self):
		response = requests.get(URL + "/bitmapInfo")
		self.assertEqual(200, response.status_code)

	def test_ptRoute(self):
		response = requests.get(URL + "/ptInfo")
		self.assertEqual(200, response.status_code)

	def test_pltRoute(self): 
		response = requests.get(URL + "/pltInfo") 
		self.assertEqual(200, response.status_code) 


if __name__ == "__main__":
	unittest.main()
