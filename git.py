#最常用git指令

"""    

加到本地端
  git add .
  git add (file)  
  >> git add HW1.py
  
  
"提交"檔案到本地  #單次提交到專案內 通常一個專案會提交很多次
  git commit -m "mmessage" 
  >> git commit -m "add HW1.py"
  
  
"發布"檔案到遠端  #一次性發布
  git push (remote_URL) (branch)
  >> git push https://github.com/MrZach107/Python_lesson main

  
查詢遠端repository的URL位置
  git remote -v
  >> [output:]  origin  https://github.com/MrZach107/Python_lesson.git (fetch)

    
從遠端拉檔案到本地端
  git pull
  

查詢git狀態
  git status
  
  
先拉再推 #本地端版本過舊 所以需要先 git pull --rebase 再 git push
  git pull --rebase    # --rebase 參數是表示「內容抓下來之後請使用 Rebase 方式合併」
  
"""
 
