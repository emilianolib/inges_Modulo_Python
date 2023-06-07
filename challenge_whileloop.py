#!/usr/bin/env python
# coding: utf-8

# In[1]:


##el challenge consiste en contar cuantas consonantes hay en un string hasta que aparece una vocal


# In[5]:


def challenge (string):
    i=0
    while string[i] not in 'aeiouAEIOU' and i<len(string):
        i=i+1
    return i


# In[6]:


challenge ('hola')


# In[7]:


challenge ('xyz')


# In[8]:


##el problema se da porque esta al revez planteado las condiciones del while####


# In[10]:


def challenge_modificado(string):
    i=0
    while  i<len(string)and string[i] not in 'aeiouAEIOU':
        i=i+1
    return i


# In[12]:


challenge_modificado('xyz')


# In[ ]:




