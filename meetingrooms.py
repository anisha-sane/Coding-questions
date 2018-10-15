'''
Created on 03-Mar-2018

@author: User
'''
'''
inter=[]
class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e

def canattendallmeetings(interval):
    interval.sort()
    
    #print  interval
    for i in range(1,len(interval)):
        print interval[i][0].end
       # if interval[i][0].start<interval[i-1][0].end:
        #    print "Hi"
         #   return False
    #return True

a=Interval(0,30)
b=Interval(5,10)
inter.append([a,b])
c=canattendallmeetings(inter)
#print c
'''
'''
inter=[]
class Interval:
    def __init__(self,s=0,e=0):
        self.start=s
        self.end=e

def canattendallmeetings(interval):
    interval.sort()
    
    for i in range(1,len(interval)):
        #print interval[i].start
        if interval[i].start<interval[i-1].end:
            return False
    return True

a=Interval(0,30)
inter.append(a)
b=Interval(31,50)
inter.append(b)


c=canattendallmeetings(inter)
print c
'''
import bisect
arr=[1,2,3,4,5]
index = bisect.bisect_left(arr, 3)
print index