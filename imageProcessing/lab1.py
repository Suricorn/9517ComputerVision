#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


im1 = cv2.imread("/Users/claire/Desktop/9517Vision/Lab/lab1/COMP9517_22T2_Lab1_Images(1)/cat.png", 0)


# In[3]:


im1.shape


# In[4]:


type(im1)


# In[5]:


np.min(im1)


# In[6]:


np.max(im1)


# In[7]:


plt.imshow(im1, 'gray')


# In[8]:


row,col = im1.shape


# In[9]:


print(im1)


# In[23]:


x = np.mat("-1,0,1;-2,0,2;-1,0,1")
y = np.mat("-1,-2,-1;0,0,0;1,2,1")

print(np.dot(x,y))


# In[28]:


for r in range(0,row,1):
    for c in range(0, col):
        l=[im1[r,c],im1[r,c+1], im1[r,c+2]]
        [im1[r+1,c],im1[r+1,c+1], im1[r+1,c+2]]
        [im1[r+2,c],im1[r+2,c+1], im1[r+2,c+2]]
        


# In[11]:


im2 = cv2.imread("/Users/claire/Desktop/9517Vision/Lab/lab1/COMP9517_22T2_Lab1_Images(1)/Dog.png")


# In[12]:


im2 = cv2.cvtColor(im2, cv2.COLOR_RGB2BGR)


# In[13]:


im2.shape


# In[35]:


plt.imshow(im2)


# In[ ]:




