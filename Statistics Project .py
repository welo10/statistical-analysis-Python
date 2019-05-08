# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:53:58 2019

@author: Waleed Ehab Badr
58 118 92 108 132 32 140 138 96 161 120 86 115 118 95 83 112 128 127 124 123 134 94 67 124 155 105 100 112 141 104 132 98 146 132 93 85 94 116 113
40
"""

import math
import matplotlib, sys
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT
import numpy as np
from scipy.stats import linregress
matplotlib.use('TkAgg')
Data=[]
Y=[]
X=[]


def NumOfClasses(Data):
    return math.ceil(1+3.3*math.log(len(Data),10))
def LengthOfInterval(Data):
    return round(Data[len(Data)-1]-Data[0]/(NumOfClasses(Data)))
def Mean(Data):
    sum = 0
    for i in Data:
        sum = sum+i
    return sum/len(Data)
def Mode(Data):
    maxi=1
    mode=[]
    for i in Data:
        if(Data.count(i)>maxi):
            mode.clear()
            maxi=Data.count(i)
            mode.append(i)
        elif(Data.count(i) == maxi and maxi>1 and (len(mode)==0 or mode[len(mode)-1]!=i)):
            mode.append(i)
    return mode
def Median(Data):
    
    if(len(Data)%2!=0):
        return Data[int((len(Data))/2)]
    else :
        return (Data[int(len(Data)/2)]+Data[int(len(Data)/2)-1])/2
Q=[]
def CalcQ(Data):
        Q.clear()
        FirstInterval=[]
        ThirdInterval=[]
        for i in range(int(len(Data)/2)):
            FirstInterval.append(Data[i])
        for i in range(math.ceil(len(Data)/2),len(Data)):
            ThirdInterval.append(Data[i])
        Q.append(Median(FirstInterval))
        Q.append(Median(Data))
        Q.append(Median(ThirdInterval))
        print(Q[2])
def showHistogram():
    p = f.gca()
    p.hist(Data,bins=NumOfClasses(Data),ec='k')
    canvas.draw()
def BoxPlot():
    p=f2.gca()
    p.boxplot(Data)
    canvas2.draw()
def Graph():
    p=f3.gca()
    p.scatter(Data,Y,c='b')
    fit = np.polyfit(Data,Y,1)
    fit_fn = np.poly1d(fit) 
    # fit_fn is now a function which takes in x and returns an estimate for y
    p.plot(Data, fit_fn(Data),c='r')
    canvas3.draw()
def oneData():
    Data.sort()
    s1.set("Mean: " + str(Mean(Data)))
    s2.set("Mode: " + str(Mode(Data)))
    s3.set("Median: " + str(Median(Data)))
    CalcQ(Data)
    s4.set("Q1: " + str(Q[0]))
    s5.set("Q2: " + str(Q[1]))
    s6.set("Q3: " + str(Q[2]))
    showHistogram()
    BoxPlot()
def addX():
    for i in e1.get().split():
        Data.append(int(i))
    X=Data
    print(X)
    oneData()
def addY():
    for i in e2.get().split():
        Y.append(int(i))
    res=linregress(Data, Y)
    s7.set("Coefficient Of Correlation: " + str(res[2]))
    Graph()
w = tk.Tk()
frame = Frame(w)
frame.pack()
e1=Entry(frame, width=45)
e1.pack(side=LEFT,padx=15,pady=15)
b=tk.Button(frame, text='ADD X', width=20, command=addX)
b.pack()
frameY=Frame(w)
frameY.pack()
e2=Entry(frameY , width=45)
e2.pack(side=LEFT,padx=15,pady=15)
b2=tk.Button(frameY, text='ADD Y', width=20, command=addY)
b2.pack(pady=10)
Values =Frame(w)
Values.pack()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s1.set("Mean: 0")
s2.set("Mode: 0")
s3.set("Median: 0")
s4.set("Q1: 0")
s5.set("Q2: 0")
s6.set("Q3: 0")
s7.set("coefficient of correlation: 0")
meanx = Label(Values,font=(None, 15), textvariable=s1)
modex = Label(Values,font=(None, 15), textvariable=s2)
medianx = Label(Values,font=(None, 15), textvariable=s3)
Q1x = Label(Values,font=(None, 15), textvariable=s4)
Q2x = Label(Values,font=(None, 15), textvariable=s5)
Q3x = Label(Values,font=(None, 15), textvariable=s6)
corrx = Label(Values,font=(None, 15), textvariable=s7)
meanx.pack(side=LEFT)
corrx.pack(side=RIGHT)
modex.pack(side=RIGHT)
medianx.pack(side=RIGHT)
Q1x.pack(side=RIGHT)
Q2x.pack(side=RIGHT)
Q3x.pack(side=RIGHT)
f = Figure(figsize=(5,4), dpi=100)
canvas = FigureCanvasTkAgg(f, master=w)
canvas.get_tk_widget().pack(side=LEFT)
f2 = Figure(figsize=(5,4), dpi=100)
canvas2 = FigureCanvasTkAgg(f2, master=w)
canvas2.get_tk_widget().pack(side=RIGHT)
f3 = Figure(figsize=(5,4), dpi=100)
canvas3 = FigureCanvasTkAgg(f3, master=w)
canvas3.get_tk_widget().pack(side=BOTTOM)
w.mainloop()

