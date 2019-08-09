
# coding: utf-8

# In[1]:


from FinMind.Data import Load
import requests
import pandas as pd
import time
import os
import datetime


# In[3]:


url = 'http://finmindapi.servebeer.com/api/data'
list_url = 'http://finmindapi.servebeer.com/api/datalist'
form_data = {'dataset':'TaiwanStockInfo',
             'stock_id':'',
             'date':''}
res = requests.post(
        url,verify = True,headers = {},
        data = form_data)

temp = res.json()
data = pd.DataFrame(temp['data'])


# # stock_id_list

# In[4]:


data_id_list = data["stock_id"].tolist()


# In[5]:


# # 代碼有四位的stock_id

# stock_id_list = []
# for ids in data_id_list:
#     if len(ids) == 4 :
#         stock_id_list.append(ids)
        
# print(stock_id_list)


# In[6]:


step = 0
starttime = datetime.datetime.now()

for xxxx in data_id_list:
    form_data = {'dataset':'TaiwanStockPrice',
                 'stock_id':xxxx,
                 'date':''}
    res = requests.post(
            url,verify = True,headers = {},
            data = form_data)

    temp = res.json()
    stock_price = pd.DataFrame(temp['data'])
    save_name = str(xxxx)+'_price.csv'
    save_path = os.path.join("stock_price/",save_name)
    stock_price.to_csv(save_path)
    step +=1
    if step%10 == 0:
        print("已完成"," ",str(step)+'/'+str(len(data_id_list)))
        endtime = datetime.datetime.now()
        print("執行時間:",(endtime - starttime).seconds,"秒")
        


# In[14]:


# data[data["industry_category"] == '水泥工業']


# # read price

# In[62]:


# #要加{u'stock_id':str} stock_id前面的0才不會不見
# pd.read_csv("stock_price/1101_price.csv",converters = {u'stock_id':str})

