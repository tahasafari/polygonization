import numpy as np 
import matplotlib.pyplot as plt
import math

initialtriangle=[]

def innertrianglecheck(newpoint):

    a=math.sqrt((initialtriangle[0]-initialtriangle[2])**2+(initialtriangle[1]-initialtriangle[3])**2)
    b=math.sqrt((initialtriangle[0]-initialtriangle[4])**2+(initialtriangle[1]-initialtriangle[5])**2)
    c=math.sqrt((initialtriangle[2]-initialtriangle[4])**2+(initialtriangle[3]-initialtriangle[5])**2)
    k=(a+b+c)/2
    mainarea=math.sqrt((k*(k-a)*(k-b)*(k-c)))
    n1=math.sqrt((initialtriangle[0]-newpoint[0])**2+(initialtriangle[1]-newpoint[1])**2)
    n2=math.sqrt((initialtriangle[2]-newpoint[0])**2+(initialtriangle[3]-newpoint[1])**2)
    n3=math.sqrt((initialtriangle[4]-newpoint[0])**2+(initialtriangle[5]-newpoint[1])**2)
    k1=(a+n1+n2)/2
    k2=(b+n1+n3)/2
    k3=(c+n3+n2)/2
    area1=math.sqrt(k1*(k1-a)*(k1-n1)*(k1-n2))
    area2=math.sqrt(k2*(k2-b)*(k2-n3)*(k2-n1))
    area3=math.sqrt(k3*(k3-c)*(k3-n2)*(k3-n3))
    if(mainarea-(area1+area2+area3)<0.0000001):
        initialtriangle[0]=newpoint[0]
        initialtriangle[1]=newpoint[1]


def buildinitialtriangle(s):
    arr=[]
    newpoint=[]
    index=0
    term=0

    for i in s:
        arr.append(i['x'])
        arr.append(i['y'])   

    for i in range(6):
        initialtriangle.append(arr[i])
    print(initialtriangle)

    for i in arr:
        index=index+1
        if(index>6):
            newpoint.append(i)
            term=term+1
            if(term>1):
                innertrianglecheck(newpoint)
                term=0


def main_function():
    f=open("points.txt","r")
    s=[]
    for i in f.readlines():
        z=i.split(' ')
        s.append(dict(x=int(z[0]),y=int(z[1])))
    buildinitialtriangle(s)



main_function()

print(initialtriangle)