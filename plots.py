import matplotlib.pyplot as plt
import csv
import numpy as np
x = []
y = []
z=[]
count =1
with open('output.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        count+=1
        if row:
                x.append(count)
                y.append(float(row[1]))
                z.append(float(row[2]))
        
        #if(count == 120):
        #    break
        
plt.plot(x,y, label='Price')
plt.plot(x,z, label = 'moving average')
#plt.yticks(np.arange(min(y), max(y)+1, 0.87))
plt.xlabel('x')

plt.ylabel('y')
plt.legend()
plt.show()
