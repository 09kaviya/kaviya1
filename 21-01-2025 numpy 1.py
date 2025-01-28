#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=np.array([10,20,30,40])
print("One dimensional array:",a)


# In[3]:


import numpy as np
b=np.array([[1,2,3],[4,5,6]])
print("Two dimensional array:",b)


# In[4]:


import numpy as np
c=np.array([[1,2,3],[4,5,6,],[7,8,9]])
print("Three dimensional array:",c)


# In[5]:


import numpy as np
d=np.zeros([1,2])
print("\n array with all zeros:\n",d)


# In[6]:


import numpy as np
e=np.random.random((1,2))
print("\n Random number:\n",e)


# In[9]:


import numpy as np
f=np.arange(1,10,1)
print("\n Sequence array:\n",f)


# In[11]:


import numpy as np
g=np.random.random((2,3))
new=g.reshape((3,2))
print("\n original array:\n",g)
print("\n new array:\n",new)


# In[23]:


import numpy as np
a=np.array((3,2))
h=a.flatten()                    
print("\n original array:\n",a)
print("\n flatten array:\n",h)
print("\n dimensional of array:\n",a.ndim)


# In[29]:


import numpy as np
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\n dimensional of array:\n",a.ndim)


# In[31]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("shaped of array ",a.shape)


# In[33]:


import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("data type",a.dtype )


# In[ ]:




