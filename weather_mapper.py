#!/usr/bin/python

import sys
import pytz
import datetime

#sys.stdin = open('weather-data.txt')

#averages

for line in sys.stdin:
    line = line.strip()
    line = line.split()
    if (line[0].isdigit() and len(line)==33):

        date,time = line[2][0:8], line[2][8:12]

        #put date in format:
        date = date[0:4]+"-"+str(date[4:6])+"-"+date[6:8]

        #put time in format:
        time = time[0:2]+":"+time[2:4]

        #set date time format:
        fmt = "%Y-%m-%d\t%H:%M GMT"

        date_time = date+"\t"+time+" GMT"

        #original string time zone:
        gmt = pytz.timezone('GMT')
        date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d\t%H:%M GMT')
        date_time =gmt.localize(date_time)  #read string as datetime value in GMT

        #conversion time zone:
        est = pytz.timezone('US/Eastern')

        #convert to EST value:
        new_date_time = date_time.astimezone(est)   #convert GMT to EST value

        #print new_date_time.year

        date_hr = str(new_date_time).split(":")[0]
        date,time = str(new_date_time).split(" ")

        for i in range(0,len(line)):
            if line[i].__contains__("*"):
                line[i]=str(None)
        value = time + ","+ line[6]+","+line[7]+ ","+line[11] + ","+ line[21] + ","+ line[22] + ","+ line[26] + ","+ line[27] + ","+ line[30] + ","+ line[32]
                        #time, sky cover, visibility, temperature, dew, max temp, min temp, pcp01, snow depth
        #print line
        if (int(new_date_time.year) == 2015):
            print "%s\t%s" %(date, value)
    else:
        continue
