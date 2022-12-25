#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import numpy as np #linear algebra
import pandas as pd #data processing, csv file I/O (e.g pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df_train=pd.read_csv('DigiDB_digimonlist.csv')
df_train.head()
#pd.read_csv('DigiDB_digimonlist.csv')
#pd.read_csv('DigiDB_supportlist.csv')


# In[5]:


#WE will display the number of rows and column
df_train.shape


# In[6]:


df_train.describe()


# In[7]:


df_train.head()


# In[8]:


#Displaying the columns in our dataset
df_train.columns


# In[9]:


df_train.info()
#This command gives basic information about each column in dataset


# In[10]:


f,ax=plt.subplots(figsize=(15,15))
sns.heatmap(df_train.corr(),annot=True, linewidths=1,fmt='.1f',ax=ax,cmap='YlGnBu')


# we see that,there are no null values in a row.if there were any missing values ,than we would need to choose a strategy for dealing with them:

# In[11]:


#let's look for the maximum HP
df_train['Lv 50 HP'].max()


# # VISUAL EXPLORATORY DATA ANALYSIS

# Box plots: visualize basic statistics like outliers , min/max or quantities
#     * I want to compare level of digimons and their attack

# In[12]:


df_train.boxplot(column='Lv 50 HP', by='Lv50 Atk')


# In[14]:


data= df_train.loc[:,['Lv 50 HP','Lv50 Atk', 'Lv50 Def']]
data.plot()


# In[15]:


#subplots
data.plot(subplots=True)


# In[16]:


#scatter plot
data.plot(kind ='scatter',x='Lv50 Atk', y='Lv50 Def')


# In[24]:


#hist plot

data.plot.hist(stacked=True, bins=50 , range=(0,300), y='Lv50 Def')


# In[25]:


df_train['Type'].unique()


# In[26]:


#Now i want to know , what type of digimons have the biggest attack ?
pd.crosstab(df_train['Type'], df_train['Lv50 Atk'])


# In[27]:


df_train[df_train['Type']=='Data']['Lv50 Atk'].max()


# In[28]:


df_train[df_train['Type'] == 'Free']['Lv50 Atk'].max()


# In[29]:


df_train[df_train['Type'] == 'Vaccine']['Lv50 Atk'].max()


# In[30]:


df_train[df_train['Type'] == 'Virus']['Lv50 Atk'].max()


# The next step, i will plot the type of digimons and their amount.

# In[31]:


digimons_movelist = pd.read_csv('DigiDB_digimonlist.csv')


# In[32]:


digimons_movelist['Type'].value_counts().plot(kind='bar')
plt.title('Digimonsters type')
plt.ylabel('Count')
plt.show()


# In[ ]:




