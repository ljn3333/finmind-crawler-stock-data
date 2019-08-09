
# coding: utf-8

# In[9]:


from FinMind.Data import Load
import requests
import numpy as np
import pandas as pd
import datetime
import os
import time
import csv
import util


# In[10]:


url = 'http://finmindapi.servebeer.com/api/data'
list_url = 'http://finmindapi.servebeer.com/api/datalist'


# In[11]:


util.mkdir('stock_price')


# # stock_id_list

# In[12]:


form_data = {'dataset':'TaiwanStockInfo',
             'stock_id':'',
             'date':''}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])
data_id_list = data["stock_id"].tolist()
data_id_list


# In[14]:


step = 0
starttime = datetime.datetime.now()

for xxxx in data_id_list:
    try:
        save_name = xxxx+"_price.csv"
        save_data = pd.read_csv(os.path.join("stock_price/",save_name),converters = {u'stock_id':str}).drop(['Unnamed: 0'],axis = 1)

        form_data = {'dataset':'TaiwanStockPrice',
                 'stock_id':xxxx,
                 'date':save_data.date.tolist()[-1]}
        res = requests.post(
                url,verify = True,headers = {},
                data = form_data)

        temp = res.json()
        update_data = pd.DataFrame(temp['data'])

        droped_data = update_data.drop([0])
        save_data.append([droped_data],ignore_index= True).to_csv(os.path.join("stock_price/",save_name))
        step +=1
        if step%10 == 0:
            print("已完成更新"," ",str(step)+'/'+str(len(data_id_list)))
            endtime = datetime.datetime.now()
            print("執行時間:",(endtime - starttime).seconds,"秒")
            
    except FileNotFoundError:
        print(xxxx,"is not exist !")
        pass

