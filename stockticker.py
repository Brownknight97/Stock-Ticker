import urllib
import re
import json
import matplotlib.pyplot as plt

name=raw_input("Enter Stock Symbol:  ").upper()
htmltext=urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1Y/"+name+":US")
data=json.load(htmltext)
datapoints=data["data_values"]

xvals=[]
yvals=[]

for point in datapoints:
    xvals.append(point[0])
    yvals.append(point[1])

for point in datapoints:
    print "Time", point[0],"Cost", point[1]
print "the number of points is ", len(datapoints)

plt.plot(xvals, yvals)
plt.show()

    
