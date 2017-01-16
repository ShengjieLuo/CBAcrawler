from catch import catchPage
#from crawler import carwlerPage
import crawler
from urls import geturls

def write():
	urllist = geturls()
	for url in urllist:
		content = catchPage(url)
		info	= crawler.crawlerPage(content)
		#result = writeDB(info)
	return None
		
def read():
	pass

def main():
	write()
	read()

if __name__=="__main__":
	write()



