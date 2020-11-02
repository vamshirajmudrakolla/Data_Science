#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv(r"C:\Users\Administrator.DESKTOP-V37RNIA\Documents\python project\COVID\owid-covid-data.csv")


# In[3]:


data.columns


# In[5]:


sns.pairplot(data)

