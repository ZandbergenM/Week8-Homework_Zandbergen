#!/usr/bin/env python
# coding: utf-8

# In[1]:


from arcgis import GIS


# In[2]:


gis = GIS()


# In[13]:


search_result = gis.content.search(query="Seattle", item_type="Feature Layer", max_items = 10)
search_result


# In[21]:


seattle_item = search_result[6]


# In[22]:


seattle_item.layers


# In[23]:


df = seattle_item.layers[0].query().sdf


# In[24]:


df.head()


# In[33]:


m1 = GIS().map("Seattle")
m1.zoom = 11
m1


# In[35]:


df.spatial.plot(map_widget = m1,
               renderer_type = 'u',
               col = 'condition')


# In[36]:


import matplotlib.pyplot as plt


# In[54]:


test = plt.hist(df['condition'])
plt.title('Condition of Seattle Trails')
plt.xlabel("Condition")
plt.ylabel("Trail Segments")


# In[ ]:




