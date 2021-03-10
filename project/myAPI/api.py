from flask import *

from myCode import MetaPage
from myCode import PageBroker

app = Flask('memoryanalysis')

@app.route('/')
def welcome():
	name = "FG" #TODO put your name here

	return """
	<form action="/upload" enctype="multipart/form-data" method="POST">
	<p>
		Welcome to the memory dump analysis API.<br>
		<br> <br>
		This code is provided as a starting point for TP4.
		<br> <br>
		Produced by:""" + name + """
	</p>
	<p>
		Please specify a file to analyze: <br>
		<input type="file" name="file" size="40">
	</p>
	<div>
		<input type="submit" value="Submit">
	</div>
	<p>
		Or analyse the (previously) uploaded file by going to one of the following:</br>
			<ul>
			<li><a href="/metaInfo">metaInfo</a></br></li>
			<li><a href="/bitmapInfo">bitmapInfo</a></br></li>
			<li><a href="/ptInfo">ptInfo</a></br></li>
			<li><a href="/pltInfo">pltInfo</a></br></li>
			</ul>
	</p>
	</form>"""



@app.route('/upload', methods=['POST'])
def upload():
	if 'file' not in request.files:
		return make_response('file missing from upload request.',400)
	file = request.files['file']
	file.save(PageBroker.DUMP_FILE)
	try:
		__getMetaPage()
	except:
		return make_response("The file provided does not appear to be a valid memory dump file.", 400)
	return "file successfully uploaded.</br>Return <a href='/'>home</a>"


def __getMetaPage():
	dumpMetaPage = PageBroker.getPage(0)
	metaPage = MetaPage.parseFromHexDump(dumpMetaPage)
	return metaPage


@app.route('/metaInfo')
def getMetaPageInfo():
	fileName = PageBroker.getDumpFileName()
	metaPage = __getMetaPage()
	return jsonify({'fileName':fileName, 'metaInfo':metaPage.toMap()})


@app.route('/bitmapInfo')
def getBitmapPageInfo():
	return "Something needs to be done here."


@app.route('/ptInfo')
def getPTPageInfo():
	return "Something needs to be done here."


@app.route('/pltInfo')
def getPLTPageInfo():
	return "Something needs to be done here."


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 5555)
