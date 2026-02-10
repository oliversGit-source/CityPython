import time


class stopwatch():
    def __init__(self):
        self.__starttime = time.time()

    def start(self):
        self.__starttime = time.time()

    def stop(self):
        self.__endtime = time.time()

    def timeelapsed(self):
        self.__timeelapsed = (self.__endtime - self.__starttime)

    def getStartTime(self):
        return self.__starttime

    def getEndTime(self):
        return self.__endtime

    def getTimeElapsed(self):
        return self.__timeelapsed

count = 0
testlist = []
for x in range(0, 10000000):
    testlist.append(x)

st1 = stopwatch()
st1.start()
for x in testlist:
    count += 1
    if count == 10000000:
        st1.stop()
        st1.timeelapsed()
        time = st1.getTimeElapsed()

print(f'The time taken to loop the list is {time} seconds')