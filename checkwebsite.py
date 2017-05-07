import http.client
import re
import hashlib
import psycopg2
import urllib.parse


urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
dbConn = psycopg2.connect( database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
dbCur = dbConn.cursor(cursor_factory=RealDictCursor)

def getCurrentWebsiteHash(weburl):
	httpConn = http.client.HTTPSConnection(weburl)
	httpConn.request('GET', 'https://medium.com/' + user + '/latest')

	resp = httpConn.getresponse()
	data = resp.read()

	hash_object = hashlib.md5( data )
	print(hash_object.hexdigest())

	return hash_object.hexdigest()

def getWebList():
	try:
		dbCur.execute("select * from webcheckerdb where website = " + weburl )
		rows = dbcur.fetchall()
	except:
		print ("error during select: " + str(traceback.format_exc()) )
	return rows

def checkWebList(weblist):
	for webrecord in weblist:
		currWebHash = getCurrentWebsiteHash( webrecord['website'])
		if currWebHash != webrecord['lasthashcode']:
			print 'Website ' + webrecord['website'] + ' has changed ';

if __name__ == "__main__":
	weblist = getWebList()
	checkWebList( weblist )