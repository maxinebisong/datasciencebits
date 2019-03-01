
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


#Using UCLA auto dataset

path="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(path,header=None)


# In[9]:


df.head(5)
df.tail(5)


# In[11]:


# create headers list and insert in dataframe
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
df.head(10)


# In[12]:


#Dropping NA from dataset
df.dropna(subset=["price"], axis=0)


# In[13]:


# Naming columns
df.columns.values


# In[14]:


df.to_csv("test.csv")


# In[15]:


#Column summary

df.describe()


# In[16]:


# describe all the columns in "df" 
df.describe(include = "all")


# In[17]:


# Info on all headings similar to proc content

df.info()

