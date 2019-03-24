import os

print(os.getcwd())  # F:\PythonProject
os.chdir(r'D:\\python')
print(os.getcwd())  # D:\python
print(os.path.abspath('.'))  # D:\python

# 由于工作目录切换到D:\python，所以这个aa.txt就在其下生成
with open('aa.txt', 'w', encoding='utf-8') as f:
    f.write('你好')
print(os.path.getsize(os.getcwd()+"\\aa.txt"))