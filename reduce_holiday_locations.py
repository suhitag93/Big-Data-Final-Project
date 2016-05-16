#!/usr/bin/python
import sys
trip_count = 0
prev_key = None
total_passengers = 0
flag = False
#sys.stdin=open('dropmaphol.txt','r')
for line in sys.stdin:
    try:
        line =line.strip()
        key,passengers =line.split("\t")
        if flag==False:
            prev_key = key
            total_passengers = passengers
            trip_count = 1
            flag = True
            continue

        if prev_key == key:
            trip_count +=1
            total_passengers += passengers
        else:

            print "%s,%s,%s" %(key,total_passengers,trip_count)
            prev_key = key
            total_passengers = passengers
            trip_count = 1
    except:
        pass
print "%s,%s,%s" %(prev_key,total_passengers,trip_count)
