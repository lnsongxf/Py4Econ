'''
Created on Sep 29, 2013

@author: fan
'''
# import ProjectDisertCredit.Support.Timer import Timer
# python "C:/Users/fan/Py4Econ/support/timer.py"

import time
import datetime as date

def curTimeDiff(startTime=None):
    if (startTime==None):
        return time.time()
    else:
        return (time.time()-startTime)

def getDateTime(timeType =6):

    if (timeType==1):
        date_time = date.datetime.now().time()

    if (timeType==2):
        date_time = date.datetime.now()

    if (timeType==3):
        date_time = date.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if (timeType==4):
        date_time = date.datetime.now().strftime('%Y-%m-%d %H:%M')

    if (timeType==5):
        date_time = date.datetime.now().strftime('%Y%m_%d_%H%M')

    if (timeType==6):
        date_time = date.datetime.now().strftime('%Y%m_%d')

    return date_time

class Timer(object):
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, value, traceback):
        if self.name:
            print ('[%s]' % self.name)
        print ('Elapsed: %s' % (time.time() - self.tstart))

if __name__ == '__main__':
    with Timer('foo_stuff'):
        1+1
