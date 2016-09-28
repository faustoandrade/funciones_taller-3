
# coding: utf-8

# In[66]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# In[73]:

x=[0,10,20,30,40,50,60,70,80,90,100]
a = 20
b = 50
c = 70


# In[74]:

def triangle(x,a,b,c):
    if ((x<a) & (x>=c)):
        return 0
    if ((a<=x) & (x<b)):
        return (x-a)
    if ((b<=x) & (x<=c)):
        return (c-x)


# In[75]:

plt.xlabel('Valores de X')
plt.title('Funcion Triangulo')
plt.plot(triangle(x,a,b,c))


# In[30]:

get_ipython().magic(u'matplotlib inline')
import math
import numpy as np
import matplotlib.pyplot as plt


# In[42]:

x = np.arange(-10, 10,5)


# In[52]:

def sigmoidal(x):
    n = []
    for item in x:
        n.append(1/(1+math.exp(-item)))
    return n


# In[53]:

plt.xlabel('Valores de X')
plt.title('Funcion Sigmoidal')
plt.plot(x, sigmoidal(x))


# In[ ]:

get_ipython().magic(u'matplotlib inline')
import math
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:

x=[0,10,20,30,40,50,60,70,80,90,100]
a = 20
b = 50
c = 70
d = 150


# In[80]:

def trapecio(x,a,b,c,d):
    if ((x<a) & (x>=c)):
        return 0
    if ((a<=x) & (x<b)):
        return (x-a)
    if ((b<=x) & (x<=c)):
        return (c-x)
    if (x>=d)&(x<c):
        return (x-d)/(c-d)


# In[81]:

plt.xlabel('Valores de X')
plt.title('Funcion Trapecio')
plt.plot(trapecio(x,a,b,c,d))


# In[ ]:

get_ipython().magic(u'matplotlib inline')
import math
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:

x=[0,10,20,30,40,50,60,70,80,90,100]
a = 20
b = 60


# In[82]:

def hombro(x,a,b):
    if (x<a):
        return 0
    if (x>=a)& (x<b):
        return (x-a)/(b-a)
    if (x>=b):
        return 1   


# In[83]:

plt.xlabel('Valores de X')
plt.title('Funcion hombro')
plt.plot(x, hombro(x,a,b,))


# In[ ]:



