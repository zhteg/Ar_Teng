# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:08:17 2016

@author: tzhan
"""
import math
from matplotlib import pyplot as plt 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np


class FigurePlot(object):
    def logPlot(self, fileName):
        timestep,temp,PE,KE,TotE=[],[],[],[],[]
        with open(fileName) as fr:
            for line in fr:
                line=line.split()
                if line[0].isdigit():
                    timestep.append(int(line[0]))
                    temp.append(float(line[1]))
                    PE.append(float(line[2]))
                    KE.append(float(line[3]))
                    TotE.append(float(line[2])+float(line[3]))

        ax1 = plt.subplot(211)
        plt.plot(timestep, temp, 'r')
        plt.setp(ax1.get_xticklabels(), visible=False)
        plt.ylabel('Temperature (K)', fontsize=14, color='r')
        for tl in ax1.get_yticklabels():
            tl.set_color('r')

        ax2 = ax1.twinx()
        ax2.plot(timestep, KE,'k.')
        ax2.set_ylabel('Kinetic Energy (J)', fontsize=14)

        # share x and y
        ax3 = plt.subplot(212, sharex=ax1)
        plt.plot(timestep,PE, timestep,TotE)
        plt.xlim(min(timestep), max(timestep))
        plt.xlabel('Timestep ($10^{-14} s$)', fontsize=16)
        plt.ylabel('Energy (J)', fontsize=12)
        plt.legend(["Potential Energy","Total Energy"])
        plt.show()


    def getRowNum(self, fileName):
        col, content=0, []
        with open(fileName) as fr:
            fr.readline()
            for line in fr:
                line=line.split()
                try:
                    float(line[0])
                    content.append(float(line[0]))
                    col+=1
                except ValueError:
                    return col, content
                
    def rdfPlot(self, fileName):
        col, content=self.getRowNum(fileName)
        sumList, numList, i =[0]*col, [0]*col, col
        with open(fileName) as fr:     
            for line in fr:
                if i == col:
                    i=0
                    continue
                else:
                    line=line.split()
                    sumList[i]+=float(line[1])
                    numList[i]+=1
                    i+=1
        for i in range(col):
            if numList[i] !=0:
                sumList[i]/=numList[i]

        ax3 = plt.subplot(121)
        plt.plot(content,sumList)
        plt.xlim(min(content), max(content))
        plt.xlabel('Distance (sigma)', fontsize=16)
        plt.ylabel('Radial Distribution Function', fontsize=16)
        #plt.show()

    def autoVPlot(self, fileName):
        col, content=self.getRowNum(fileName)
        sumList, numList, i =[0]*col, [0]*col, col
        with open(fileName) as fr:     
            for line in fr:
                if i == col:
                    i=0
                    continue
                else:
                    line=line.split()
                    sumList[i]+=float(line[1])
                    numList[i]+=1
                    i+=1
        nol  =     sumList[0]     
        for i in range(col):
            if numList[i] !=0:
                sumList[i]/=numList[i]/nol
                
        ax4 = plt.subplot(122)
        plt.subplots_adjust(wspace=0.5)
        plt.plot(content,sumList)
        plt.xlim(min(content), max(content))
        plt.xlabel('Timestep ($10^{-14} s$)', fontsize=16)
        plt.ylabel('Velocity Auto-correlation', fontsize=16)
        plt.tight_layout
        plt.show()

if __name__ == "__main__":        
    FigurePlot().logPlot('../results/log.txt')
    FigurePlot().rdfPlot("../results/rdf.txt")
    FigurePlot().autoVPlot("../results/autocorrelation.txt")
    
        