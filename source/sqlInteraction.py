import mysql.connector
import datetime
import sys

#######################################################
#          To execute the SQL statement               #
#Note:                                                #
#1. Qualified for any kind of SQL statement           #
#2. Used for simple mysql operation by python         #
#######################################################
def exeSQL(sql):
	config = {
        	  'user':'root', 
	          'password':'123456', 
	          'host':'127.0.0.1', 
	          'port':3306,  
	          'database':'cba'}
	conn = mysql.connector.connect(**config)
	cur = conn.cursor()
	cur.execute(sql)
	conn.commit()
        cur.close()
	conn.close()
	return 1

#######################################################
#          To execute the SQL statement               #
#Note:                                                #
#1. Only used for query statement                     #
#2. Used for simple mysql operation by python         #
#######################################################
def exeSQLquery(sql):
	config = {
        	  'user':'root', 
	          'password':'123456', 
	          'host':'127.0.0.1', 
	          'port':3306,  
	          'database':'cba'}
	conn = mysql.connector.connect(**config)
	cur = conn.cursor()
	cur.execute(sql)
	result_set = cur.fetchall()
	'''
	if result_set:
		for row in result_set:
			print "%s, %s, %d" % (row[0],row[1],row[2])
	'''
        cur.close()
	conn.close()
	return result_set

