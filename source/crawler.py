# -*- coding: utf-8 -*-
from lxml import etree
import sys


def team_score_add(selector,path):
	obj = selector.xpath(path)[0]
        try:
                obj = int(obj)
		return obj
        except:
                return 0

def toInt(obj):
	if obj == "--":
		return -1
	else:
		return int(obj)

def yn_to_bool(obj):
	if obj=='是':
		return 1
	elif obj=='否':
		return 0
	else:
		return -1

def tg_to_array(obj):
	obj = obj.split()
	goal = int(obj[0].split("-")[0])
	total = int(obj[0].split("-")[1])
	if goal==0 or total==0:
		percent = 0 
	else:
		percent = goal/(total+0.0)
	return [total,goal,percent]

def tg2_to_array(obj):
	goal = int(obj.split("/")[0])
	total = int(obj.split("/")[1])
	return [total,goal]

def player(selector,team,order):
	if team == 1:
		table = "part part01 blk"
	elif team == 2:
		table = "part part02 blk"
	path = "//div[@class=\'"+table+"\']/div[1]/table[1]/tbody[1]/tr["+str(order)+ "]/"
	team = 1
	namepath = path + "td[1]/a[1]/text()"
	namepath2 = path + "td[1]/text()"
	numberpath = path + "td[2]/text()"
	timepath = path + "td[3]/text()"
	starterpath = path + "td[4]/text()"
	Twopointpath = path + "td[5]/text()"	
	Threepointpath = path + "td[6]/text()"
	Penaltypath = path + "td[7]/text()"
	freboundpath = path + "td[8]/text()"
	breboundpath = path + "td[9]/text()"
	assistpath = path + "td[10]/text()"
	foulpath = path + "td[11]/text()"
	stealpath = path + "td[12]/text()"
	mispath = path + "td[13]/text()"
	blockpath = path + "td[14]/text()"
	dunkpath = path + "td[15]/text()"
	fouledpath = path + "td[16]/text()"
	fastpath = path + "td[17]/text()"
	fastpath2 = path + "td[17]/script[1]/text()"
	pointpath = path + "td[18]/text()"
	pointpath2 = path + "td[18]/script[1]/text()"
	
	try:
		try:
			name = selector.xpath(namepath)[team-1].strip()
		except:
			name = selector.xpath(namepath2)[team-1].strip()
	except:
		print "Finish scan players!"
		return -1

	number = toInt(selector.xpath(numberpath)[team-1])
	time = selector.xpath(timepath)[team-1].strip()
	starter = yn_to_bool(selector.xpath(starterpath)[team-1].strip())
	[TwoPointTotal,TwoPointGoal,TwoPointPer] = tg_to_array(selector.xpath(Twopointpath)[team-1].strip())
	[ThreePointTotal,ThreePointGoal,ThreePointPer] = tg_to_array(selector.xpath(Threepointpath)[team-1].strip())
	[PenPointTotal,PenPointGoal,PenPointPer] = tg_to_array(selector.xpath(Penaltypath)[team-1].strip())
	frebound = toInt(selector.xpath(freboundpath)[team-1])	
	brebound = toInt(selector.xpath(breboundpath)[team-1])	
	assist = toInt(selector.xpath(assistpath)[team-1])	
	foul = toInt(selector.xpath(foulpath)[team-1])	
	steal = toInt(selector.xpath(stealpath)[team-1])	
	mistake = toInt(selector.xpath(mispath)[team-1])	
	block = toInt(selector.xpath(blockpath)[team-1])	
	dunk = toInt(selector.xpath(dunkpath)[team-1])	
	fouled = toInt(selector.xpath(fouledpath)[team-1])	
	
	try:
		[fasttotal, fastgoal] = tg2_to_array(selector.xpath(fastpath)[team-1].strip())
	except:
		[fasttotal, fastgoal] = tg2_to_array(selector.xpath(fastpath2)[team-1].strip().split("\"")[1])
		
	try:	
		point = toInt(selector.xpath(pointpath)[team-1])	
	except:
		point = toInt(selector.xpath(pointpath2)[team-1].strip().split("\"")[1])

	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print "player: 		",str(number),name
	print "play time: 		",time
	print "starter (1/0): 		",str(starter)
	print "Two-Pointers: 		",[TwoPointTotal,TwoPointGoal,TwoPointPer]
	print "Three-Pointers: 	",[ThreePointTotal,ThreePointGoal,ThreePointPer]
	print "Penalty Ball: 		",[PenPointTotal,PenPointGoal,PenPointPer]
	print "Rebound (forward/back):",[frebound,brebound]
	print "assist:			",assist
	print "foul:			",foul
	print "steal:			",steal
	print "mistake:		",mistake
	print "block:			",block
	print "dunk:			",dunk
	print "fouled:			",fouled
	print "fast attack:		",[fasttotal, fastgoal]
	print "point:			",point
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

	return 0

def crawlerPage(content):
	if content == None:
		return None
	selector = etree.HTML(content)
	#content_field = selector.xpath('//<span class=\"team_name team_nameA\">') 
	#content_field = selector.xpath('//body/*') 
	#content_field = selector.xpath("//div[@class='teams']")
	teamA_name = selector.xpath("//span[@class='team_name team_nameA']/text()")[0]
	teamB_name = selector.xpath("//span[@class='team_name team_nameB']/text()")[0]
	teamA_score = int(selector.xpath("//div[@class='team_score team_scoreA']/span/text()")[0])
	teamB_score = int(selector.xpath("//div[@class='team_score team_scoreB']/span/text()")[0])
	teamA_score_1 = int(selector.xpath("//div[@class='score_tab']/div[2]/span[1]/text()")[0])
	teamA_score_2 = int(selector.xpath("//div[@class='score_tab']/div[3]/span[1]/text()")[0])
	teamA_score_3 = int(selector.xpath("//div[@class='score_tab']/div[4]/span[1]/text()")[0])
	teamA_score_4 = int(selector.xpath("//div[@class='score_tab']/div[5]/span[1]/text()")[0])
	teamB_score_1 = int(selector.xpath("//div[@class='score_tab']/div[2]/span[2]/text()")[0])
        teamB_score_2 = int(selector.xpath("//div[@class='score_tab']/div[3]/span[2]/text()")[0])
        teamB_score_3 = int(selector.xpath("//div[@class='score_tab']/div[4]/span[2]/text()")[0])
        teamB_score_4 = int(selector.xpath("//div[@class='score_tab']/div[5]/span[2]/text()")[0])

	teamA_score_a1 = team_score_add(selector,"//div[@class='score_tab']/div[6]/span[1]/text()")
	teamA_score_a2 = team_score_add(selector,"//div[@class='score_tab']/div[7]/span[1]/text()")
	teamB_score_a1 = team_score_add(selector,"//div[@class='score_tab']/div[6]/span[2]/text()")
	teamB_score_a2 = team_score_add(selector,"//div[@class='score_tab']/div[7]/span[2]/text()")

	time = selector.xpath("//div[@class='part blk compare']/p[1]/span[1]/text()")[0]	

	for team in [1,2]:
		count = 1
		while (1>0):
			print "team: ",str(team)," count",str(count)
			result = player(selector,team,count)
			if result == 0:
				count += 1
				continue
			elif result == -1:
				break
	
	print "time: ",time
	print "Host Team: ",teamA_name,":",str(teamA_score)
	print "|",str(teamA_score_1),"|",str(teamA_score_2),"|",str(teamA_score_3),"|",str(teamA_score_4),"|",str(teamA_score_a1),"|",str(teamA_score_a2),"|"
	print "Guest Team: ",teamB_name,":",teamB_score
	print "|",str(teamB_score_1),"|",str(teamB_score_2),"|",str(teamB_score_3),"|",str(teamB_score_4),"|",str(teamB_score_a1),"|",str(teamB_score_a2),"|"
	return None
