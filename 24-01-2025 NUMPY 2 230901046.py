#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([10,20,30,40])
slice1=a[1:2]
print(slice1)


# In[2]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
slice2=a[1:10:2]
print(slice2)


# In[3]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
slice3=a[1:10:3]
print(slice3)


# In[5]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
slice4=a[::4]
print(slice4)


# In[6]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
slice5=a[::-1]
print(slice5)


# In[7]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
subarray=a[0:2,1:3]
print(subarray)


# In[8]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
subarray=a[:2,:1]
print(subarray)


# In[11]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
col1=a[:,0]
print(col1)


# In[13]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
row1=a[0,:]
print(row1)


# In[14]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
row2=a[0:2:1]
print(row2)


# In[17]:


import numpy as np
import array
a=array.array('i',[1,2,3,4,5])
print(a[0])
print(a[3])


# In[19]:


import numpy as np
a=np.array([1,2,3,4,5])
print(a[0])
print(a[3])


# In[21]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0,0])
print(a[2,1])


# In[23]:


import numpy as np
a=np.array([1,2,3,4,5])
print("basic indexing",a[1])
print("neagative indexing",a[-1])
print("slicing indexing",a[1:2])


# In[ ]:





