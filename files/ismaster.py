from time import  sleep
import pymongo
conn = pymongo.connection.Connection('localhost', 27017)
db = conn['local']

counter = 0

while counter < 30 :
    if db.command('isMaster')['ismaster']  == True:
        print "\nchanged=yes"
        break
    counter += 1
    sleep(1)
