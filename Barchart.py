# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 01:34:16 2019

@author: kdandebo
"""

import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns


df = pd.read_csv("C:/Users/kdandebo/Desktop/Models/Python excercise/mn-budget-detail-2014.csv")
#print(df.head(5))

#print(df.info())
#print(df.describe())
print(df.columns)
#sns.pairplot(df)
#sns.distplot(df['amount'])
y = df[df['amount'] >= 4500000]
#y = df[df['amount']]
plt.xlabel('University name')
plt.ylabel('Budget(in millions)')
plt.title('Budget of Universities which are greater than 4500000')

plt.bar(y['category'],y['amount'],color='Green')
plt.show()
#print(df.corr())