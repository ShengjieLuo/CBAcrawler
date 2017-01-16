import requests
import sys

def catchPage(url):
	reload(sys)
        sys.setdefaultencoding( "utf-8" )
	html = requests.get(url)
	if html.status_code == 200:
		print "[Info]     Get 200 response from website: "+url 
		#print html.text
		html.encoding='gbk'
		return html.text
	else:
		print "[Error]    Get the wrong reponse from website: "+url
		return None

if __name__=="__main__":
	catchPage("http://cba.sports.sina.com.cn/cba/schedule/show/-1")
	catchPage("http://cba.sports.sina.com.cn/cba/schedule/show/14579")
	
