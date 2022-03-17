#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


data = pd.read_csv("Netflix_data.csv")
data.head()


# In[5]:


def cast_len(val):
    if val == "None":
        return 0
    else:
            return len(str(val).split(", "))


# In[6]:


data["cast"].isnull().sum()


# In[7]:


data["cast"].replace(np.nan, "None", inplace=True)


# In[8]:


data.tail()


# In[13]:


data["Cast_Member"] = data["cast"].apply(cast_len)


# In[9]:


data.tail()


# In[27]:


data.groupby(["type","genre",]).count()


# In[17]:


data.groupby(["release_year","type"]).count()


# In[36]:


data.loc[0:10,["type","country"]]


# In[ ]:




