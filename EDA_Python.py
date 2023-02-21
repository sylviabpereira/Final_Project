#!/usr/bin/env python
# coding: utf-8

# In[48]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import math
from functools import reduce


# In[49]:


df = pd.read_csv(r'C:\Users\sylvia.pereira\OneDrive - alteryx.com\Desktop\Dataset_EDA_Combined_2.csv')
df.head()


# In[50]:


df.describe()


# In[51]:


profile = df.profile_report(title='Pandas Profiling Report')


# In[52]:


profile.to_file("output4.html")


# In[ ]:




