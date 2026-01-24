#BUS COUNTDOWN DISPLAY
#NB a list of Naptan Codes can be found here: https://timetablegraveyard.co.uk/FullStopInfo.txt

import urllib
import urllib.request
import json

def apiRequest(NaptanCode):
    url = 'https://api.tfl.gov.uk/StopPoint/'+NaptanCode+'/arrivals'
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    infile = urllib.request.urlopen(req)
    arrival_times_raw = infile.read().decode()
    arrivals = json.loads(arrival_times_raw)

    return arrivals
'''
Q1 (see below) Create seconds_to_minutes() function here
#One line needed within the function
'''
def seconds_to_minutes(a):
    b, c = divmod(a, 60)
    return f' {b} minutes, {c} seconds'

'''Q2 (see below) Create Highbury_Corner_F() function here
#several lines needed within the function
'''

def Highbury_Corner_F():
    print('Highbury Corner, Stop F:')
    # create header
    header = ["lineId", "destinationName", "timeToStation"]

    # print header
    print(f"{header[0]} {header[1]} {header[2]}")
    print("-" * 25)
    NaptanCode = '490000108F'
    createDisplay(NaptanCode)

def createDisplay(NaptanCode):
    arrivals = apiRequest(NaptanCode)
    for arrival_dict in arrivals:
        print(arrival_dict["lineId"], arrival_dict["destinationName"], seconds_to_minutes(arrival_dict["timeToStation"]))

def main():
    Highbury_Corner_F()
main()
'''
1)
 a) Create a function to turn arrival times into minutes (add on lines 17-18)
 b) Call your new function in the correct place on line 31, so that the display board is now in minutes

2)
 add a function to check bus departures at a stop of your choice e.g. Highbury Corner, Stop F.
 a list of Naptan Codes can be found here: https://timetablegraveyard.co.uk/FullStopInfo.txt

question: Why does running again give different times?
'''