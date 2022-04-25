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
		map = json.loads(response.content.decode('utf-8'))
		map
		self.assertEqual(map['bitmapInfo'] , [0,1,2,3,4,6,11,16,21,22,32])

	def test_ptRoute(self):
		response = requests.get(URL + "/ptInfo")
		self.assertEqual(200, response.status_code)
		map = json.loads(response.content.decode('utf-8'))
		map = map['ptinfo']
		expectedValue = {'0': {'ACL': [0], 'isSwappedOut': False, 'page location': 0, 'pageId': 0 }, '1': { 'ACL': [0], 'isSwappedOut': False, 'page location': 1, 'pageId': 1 }, '2': { 'ACL': [0], 'isSwappedOut': False, 'page location': 2, 'pageId': 2 }, '3': { 'ACL': [0], 'isSwappedOut': False, 'page location': 3, 'pageId': 3 }, '4': { 'ACL': [ 0 ], 'isSwappedOut': False, 'page location': 4, 'pageId': 4 }, '6': { 'ACL': [ 0, 30 ], 'isSwappedOut': False, 'page location': 6, 'pageId': 6 }, '11': { 'ACL': [ 0, 30 ], 'isSwappedOut': False, 'page location': 11, 'pageId': 11 }, '16': { 'ACL': [ 0, 44, 8 ], 'isSwappedOut': False, 'page location': 16, 'pageId': 16 }, '21': { 'ACL': [ 0, 8 ], 'isSwappedOut': False, 'page location': 21, 'pageId': 21 }, '22': { 'ACL': [ 0, 30 ], 'isSwappedOut': False, 'page location': 22, 'pageId': 22 }, '32': { 'ACL': [ 0, 8 ], 'isSwappedOut': False, 'page location': 32, 'pageId': 32}}
		self.assertEqual(map, expectedValue)

	def test_pltRoute(self): 
		response = requests.get(URL + "/pltInfo") 
		self.assertEqual(200, response.status_code) 
		map = json.loads(response.content.decode('utf-8'))
		map = map['pltInfo']
		self.assertEqual(map, {'0': [0, 1, 2, 3, 4], '8': [16, 32, 21], '30': [22, 6, 11], '44': [16]})


if __name__ == "__main__":
	unittest.main()
