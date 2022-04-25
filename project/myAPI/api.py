
from flask import *

from myCode import MetaPage
from myCode import PageBroker
from myCode import BitmapPage
from myCode import PTPage
from myCode import PLTPage

app = Flask('memoryanalysis')

@app.route('/')
def welcome(): #pragma: no cover
	name = "Zachary Gingras, Gabriel Bertrand"

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
def upload(): #pragma: no cover
	if 'file' not in request.files:
		return make_response('file missing from upload request.',400)
	file = request.files['file']
	file.save(PageBroker.DUMP_FILE)
	try:
		__getMetaPage()
	except:
		return make_response("The file provided does not appear to be a valid memory dump file.", 400)
	return "file successfully uploaded.</br>Return <a href='/'>home</a>"


def __getMetaPage(): #pragma: no cover
	dumpMetaPage = PageBroker.getPage(0)
	metaPage = MetaPage.parseFromHexDump(dumpMetaPage)
	return metaPage


@app.route('/metaInfo')
def getMetaPageInfo(): #pragma: no cover
	metaPage = __getMetaPage()
	return jsonify({'metaInfo':metaPage.toMap()})


def __getBitmapPage(): #pragma: no cover
	dumpBitmapPage = PageBroker.getPage(1)
	bitmapPage = BitmapPage.getListOfPages(dumpBitmapPage)
	return bitmapPage

@app.route('/bitmapInfo')
def getBitmapPageInfo(): #pragma: no cover
	bitmapPage = __getBitmapPage()
	return jsonify(bitmapPage.toMap())


def __getPtinfoPage(): #pragma: no cover
	dumpPtInfoPage = PageBroker.getPage(0)
	pageList = PageBroker.getPage(1)
	ptinfoPage = PTPage.getDictionary(dumpPtInfoPage, pageList)
	return ptinfoPage


@app.route('/ptInfo')
def getPTPageInfo(): #pragma: no cover
	ptpPage = __getPtinfoPage()
	return jsonify(ptpPage.toMap())

def __getPltinfoPage(): #pragma: no cover
	dumpPtInfoPage = PageBroker.getPage(0)
	pageList = PageBroker.getPage(1)
	ptinfoPage = PTPage.getDictionary(dumpPtInfoPage, pageList)
	return ptinfoPage


@app.route('/pltInfo')
def getPLTPageInfo(): #pragma: no cover
	page = PageBroker.getPage(0)
	pltPage = __getPltinfoPage()
	return jsonify(PLTPage.getDictionary(page).toMap())


if __name__ == '__main__': #pragma: no cover
	app.run(debug=True, host='0.0.0.0', port = 5555)
