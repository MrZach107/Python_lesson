#!/usr/bin/env python
# coding: utf-8

# In[41]:


# 發requests取得原始碼
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = { "cookie":"over18=1",
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    
}
res = requests.get(url,headers = headers)
print(res.text)


# In[96]:


#利用 BeautifulSoup 做 html 解析
soup = bs(res.text,'lxml')
data = soup.select('div.r-ent')

for ele in data:
    title = ele.select('div.title')[0].text.strip()  #抓標題
    print("標題 :",title)
    print('-'*100)


# In[121]:


#解析標題/時間/推文數量/連結

def get_parsing_data(soup):
    data = soup.select("div.r-ent")
    
    result = []
    
    for sample in data:

        #標題
        raw_title = sample.select("div.title")[0].text.strip()
        title = raw_title.replace("\u3000"," ") if "\u3000" in raw_title else raw_title
        
        #作者
        author = sample.select("div.author")[0].text.strip()
        
        #時間
        date = sample.select("div.date")[0].text.strip() 

        #推文數量
        try:
            push_num = sample.select("span.hl")[0].text
        except IndexError:
            push_num = 0
            
        #連結
        try:
            raw_link = sample.select("div.title a")[0]["href"]
            domain_link = "https://www.ptt.cc"
            link = domain_link + raw_link
        except IndexError:
            link = "None"

        result.append({
            "title":title,
            "author":author,
            "date":date,
            "push_num":push_num,
            "link":link
        })
    return result
                
get_parsing_data(soup)


# In[47]:


# 發 requests 取得原始碼
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = { "cookie":"over18=1",
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    
}
res = requests.get(url,headers = headers)
soup = bs(res.text,"lxml")

print(soup)


# In[70]:


#取得分頁的 index 值

raw_previous_page = soup.select("div#action-bar-container div.btn-group-paging a")[1]["href"]
previous_page = "https://www.ptt.cc" + raw_previous_page
print(previous_page)
print(previous_page.replace("https://www.ptt.cc/bbs/Gossiping/index","").replace(".html",""))
page_num = previous_page.replace("https://www.ptt.cc/bbs/Gossiping/index","").replace(".html","")


for i in range(5):
    print("https://www.ptt.cc/bbs/Gossiping/index{}.html".format(temp-i))


# In[106]:


#抓取 前五頁 文章列表的資料
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = { "cookie":"over18=1",
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    
}
res = requests.get(url,headers = headers)
soup = bs(res.text,"lxml")

raw_previous_page = soup.select("div#action-bar-container div.btn-group-paging a")[1]["href"]
previous_page = "https://www.ptt.cc" + raw_previous_page

page_num = previous_page.replace("https://www.ptt.cc/bbs/Gossiping/index","").replace(".html","")


for i in range(5):
    print("https://www.ptt.cc/bbs/Gossiping/index{}.html".format(temp-i))


# In[122]:


#抓取 首頁資料
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
headers = { "cookie":"over18=1",
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    
}
res = requests.get(url,headers = headers)
soup = bs(res.text,"lxml")


#解析 首頁資料
output = []
result = get_parsing_data(soup)
output += result


#擷取 分頁資料
raw_previous_page = soup.select("div#action-bar-container div.btn-group-paging a")[1]["href"]
previous_page = "https://www.ptt.cc" + raw_previous_page

page_num = previous_page.replace("https://www.ptt.cc/bbs/Gossiping/index","").replace(".html","")


for i in range(5):
    url = "https://www.ptt.cc/bbs/Gossiping/index{}.html".format(temp-i)
    res = requests.get(url,headers = headers)
    soup = bs(res.text,"lxml")
    
    result = get_parsing_data(soup)
    output += result
    
    print('{} is ok'.format(url))
    
print("Done")


# In[123]:


output


# In[124]:


# 利用 pandas 製作出一個 DataFrame
import pandas as pd
df = pd.DataFrame(output)
df


# In[125]:


# 匯出成 excel 並命名為 "ppt-gossip"
df.to_excel("ppt-gossip.xlsx")

