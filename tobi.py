#!/usr/bin/env python
# coding: utf-8

# # dsjsadhasjdadasdasdas
# ## ola
# 
# #### tudo bem
# *nesting* **ola** ***olas*** ****sadasda****

# In[ ]:


name = "Toby"


# In[ ]:


print ("Hello")
get_ipython().system('pip list ')


# In[ ]:


get_ipython().run_line_magic('lsmagic', '')


# In[9]:


import numpy as np 
import matplotlib.pyplot as plt

x = np.random.rand(5)
y = np.random.rand(5)
colors = np.random.rand(5)
area = 100
plt.scatter(x, y, s=area, c=colors, alpha =0.5)
plt.show()


# In[ ]:


get_ipython().run_cell_magic('HTML', '', '')


# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline - para permir ver matplotlib(gráficos)')
%%timeit -- comparar tempos


# In[11]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,10))
df

