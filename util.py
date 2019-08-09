
# coding: utf-8

# In[1]:


import os


# In[2]:


#建立資料夾

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符號
    path=path.rstrip('\\')
 
    # 判斷路徑是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判斷結果
    if not isExists:
        # 如果不存在則建立目錄
        print (path ,'建立成功')
        # 建立目錄操作函式
        os.makedirs(path)
        return True
    else:
        # 如果目錄存在則不建立，並提示目錄已存在
        print (path,'目錄已存在')
        return False
    

