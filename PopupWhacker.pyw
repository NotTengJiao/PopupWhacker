#auto_close_popups.py
from pywinauto import Desktop
import os.path as op
from os import system
import threading
import re


WAIT_FOR_WINDOW_TIMEOUT = 30

def load_titles():
    #读取文件初始化title_list、文件不存在时新建文件
    file = "titles.txt"
    titles = []
    if not op.exists(file):
        with open(file,"w",encoding="utf-8") as f:
           f.write("在此输入所有需要关闭的窗口标题名,换行符为分隔符")
           system(f"notepad {file}")
           return None
    else:
        with open(file,"r",encoding="utf-8") as f:
            for line in f:
                titles.append(line.rstrip("\n"))
        return titles

def close_window(title):
    #等待窗口出现并关闭
    pattern = "(?i)" + re.escape(title)
    window = Desktop(backend="uia").window(title_re=pattern)
    try:
        #等待窗口出现必须是存在且可见的（exists visible）
        window.wait("exists visible",WAIT_FOR_WINDOW_TIMEOUT,1)
        window.close()
    except Exception as e:
        print(f"出现错误:{e}")

if __name__ == '__main__':
    titles = load_titles()
    if titles:
        for title in titles:
            t = threading.Thread(target=close_window,args=(title,))
            t.start()

            
