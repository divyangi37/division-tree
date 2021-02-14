#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sklearn import tree
#[size,wheels,cost,weight]
f=[[0,2,3,0,],[1,3,4,0],[2,4,5,1],[2,6,5,1],[0,4,4,0]]
l=['bike','auto','car','truck','car']
clf=tree.DecisionTreeClassifier()
trained=clf.fit(f,l)
res=trained.predict([[0,2,3,1],[2,4,5,1]])
print(res)


# In[ ]:




