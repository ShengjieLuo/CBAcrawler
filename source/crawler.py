# coding = utf-8
from lxml import etree
import sys

def crawlerPage(content):
	if content == None:
		return None
	selector = etree.HTML(content)
	#content_field = selector.xpath('//<span class=\"team_name team_nameA\">') 
	#content_field = selector.xpath('//body/*') 
	#content_field = selector.xpath("//div[@class='teams']")
	teamA_name = selector.xpath("//span[@class='team_name team_nameA']/text()")[0]
	teamB_name = selector.xpath("//span[@class='team_name team_nameB']/text()")[0]
	teamA_score = selector.xpath("//div[@class='team_score team_scoreA']/span/text()")[0]
	teamB_score = selector.xpath("//div[@class='team_score team_scoreB']/span/text()")[0]



	print "Host Team: ",teamA_name,":",teamA_score
	print "Guest Team: ",teamB_name,":",teamB_score
	return None
