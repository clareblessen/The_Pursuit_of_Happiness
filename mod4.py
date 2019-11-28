import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df18 = pd.read_csv('data/2018.csv')
df17 = pd.read_csv('data/2017.csv')
df16 = pd.read_csv('data/2016.csv')
df15 = pd.read_csv('data/2015.csv')
df18['Year'] = '2018'
df17['Year'] = '2017'
df16['Year'] = '2016'
df15['Year'] = '2015'