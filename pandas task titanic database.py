#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[53]:


#df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df


# 1. Find out how many male and female passenger was onboarded

# In[7]:


df["Sex"].value_counts()


# 2.how many survived we have

# In[8]:


df["Survived"].value_counts()


# we have 342 survived.

# 3.how many casuality we have 

# In[ ]:


we have 549 casuality


# 4. what is name of a person who is the eldest one 

# In[15]:


df[df["Age"]==max(df["Age"])]


# name of the eldest one is Barkworth, Mr. Algernon Henry Wilson

# 5. how many passenger do we have in first , second and third class 

# In[16]:


df["Pclass"].value_counts()


# 6.how many person we have whose name starts with "s"

# In[22]:


First_letter=df["Name"].astype(str).str[0].value_counts()
First_letter


# In[ ]:


so S as first letter in 86 names of the passenger


# 7.try to create a new column which is a summation  of "SibSp" and "parch"

# In[24]:


df["sum"]=df["SibSp"]+df["Parch"]


# In[25]:


df


# In[ ]:


8 . how many person do we have below age of 25 .


# In[34]:


Less_than_25years=df["Age"]<25
Less_than_25years.value_counts()


# There are 278 person  below age of 25 .

# 9.how many person died whose age was less then 40 

# In[38]:


lessthan40anddied=(df["Age"]<40) & (df["Survived"]==0)
lessthan40anddied.value_counts()


# There are 322 person  below age of 40 and they died  .

# 10 . from a  cabin column seperate text and numeric value . 

# In[49]:


df["Text"]=df["Cabin"].str.extract('([A-Za-z]+)')
df["Numberic_value"]=df["Cabin"].str.replace('([A-Za-z]+)','')


# In[51]:


df


# In[ ]:




