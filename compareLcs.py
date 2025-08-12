import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

obsDates = ["17/Jan", "18/Jan a", "18/Jan b", "18/Jan c", "20/Jan","25/Jan", "13/Feb"]

def AddLabs(xlab, ylab):
    plt.xlabel(xlab)
    plt.ylabel(ylab)

file = open("mitaka_lcs_rel.dat","r")
dataLines = []
for line in file:
    dataLines.append(line)
file.close()

file = open("out_lcs", "r")
modelLines = []
for line in file:
    modelLines.append(line)
file.close()




chunks = int(dataLines.pop(0))
datas = []

for i in range(chunks):
    lines = int(dataLines.pop(0).split(' ')[0])
    data = []
    for j in range(lines):
        a = dataLines.pop(0).split(' ')
        time = float(a[0])
        cnts = float(a[2])
        data.append([time, cnts])
    datas.append(data)

'''
data = datas[0]
times = []
cnts = []
modelData = []
for j in range(len(data)):
    times.append(data[j][0])
    cnts.append(data[j][1])

print(cnts)
#plt.show()
'''
for i in range(len(datas)):
    data = datas[i]
    times = []
    elapsed = []
    cnts = []
    modelData = []
    for j in range(len(data)):
        times.append(data[j][0] - 2400000.5)
        cnts.append(data[j][1])
        modelData.append(float(modelLines.pop(0)))

    for t in times:
        elapsed.append((t - times[0])*24 )
        
    plt.subplot(3,3,i+1)
    plt.plot(elapsed, modelData, color = "forestgreen", label = "Model") 
    plt.errorbar(elapsed,cnts, color = "rebeccapurple", label = "Measured", fmt = 'x', markersize = 2)
    AddLabs("Time Elapsed [hr]", "Intensity")
    plt.title(obsDates[i])
    plt.legend(loc = "best")

#plt.plot([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
plt.show()

