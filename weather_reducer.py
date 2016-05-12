#!/usr/bin/python

import sys
import datetime

#if the temperature is not recorded the average uptil that time for that day can be counted as a replacement.

#sys.stdin = open('map_out')
sum_temp =0

sum_vis = 0

sum_pcp =0.00

count =0

flag_pcp = False
flag_vis =False
flag_temp = False

for line in sys.stdin:

    line = line.strip()
    key,value =line.split("\t")
    #print value
    value = value.split(",")
    #print value
    if value[4].isdigit():
        sum_temp += int(value[4])       #to take the average of the day uptil that hour of the temperature
        count+=1
        temp_flag =True
    if value[3].isdigit():
        sum_vis += float(value[3])       #to take the average visibility of the day uptil that hour
        count +=1
        flag_vis =True
    if value[8].isdigit():
        sum_pcp += float(value[8])       #to take the average of the hourly precipitation uptil that hour
        count+=1
        flag_pcp=True

    #print sum_temp,count
    value.append(str(float(sum_vis/count)))
    value.append(str(int(sum_temp/count)))
    value.append(str(float(sum_pcp/count)))
    if (value[3]=='None') and flag_vis:
        value[3]= value[10]
    if(value[4]=='None') and flag_temp:
        value[4]=value[11]
    if(value[8]=='None') and flag_pcp:
        value[8]=value[12]
    final_value = value[0]
    for i in range(1,len(value)):
        final_value+=','+value[i]
    print "%s,%s" %(key, final_value)

