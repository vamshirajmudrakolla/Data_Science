#!/usr/bin/env python
# coding: utf-8

# # DataType Operators

# In[2]:


a = 0b1010111
print(a)


# In[3]:


print(bin(765))


# In[4]:


print(oct(9876))


# In[6]:


a = eval(hex(0b10100110111110))
print(a,type(a))


# In[15]:


import sys
a=290
print(a,type(a))
print('size of a=',sys.getsizeof(a))

b=20998668888
print(b,type(b),sys.getsizeof(a))
c=258456952554411663322221112222541100003354789654445877112311000033547896544458771123110000335478965444587711231100003354789654445877112311000033547896544458771123
print(c,type(c),sys.getsizeof(a))


# In[20]:


a = 10 + 20j
print(a,type(a))
print(a.real)
print(a.imag)


# In[23]:


age=float(input('enter value'))
print(age,type(age))


# In[26]:


print(complex(True,True))


# In[27]:


print((1+2j)/(1+2j))


# In[28]:


print(ord('P'))


# In[32]:


print('A'==65)
print('A'=='A')
print(ord('A')==65)


# In[35]:


print(''and 0)
print(87 and 78)
print(0 and 0.0)


# In[36]:


print(''or 0)
print(87 or 78)
print(0 or 0.0)


# In[37]:


print(230<<5)


# In[6]:


a=10
a=a+5
print(a)

a += 5
print(a)


# In[8]:


print('p' in 'python')
print(9 in range(10))


# In[9]:


a=10
b=10
print(a is b)
print(id(a))
print(id(b))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




