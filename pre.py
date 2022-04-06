import os

def DFS_file_search(dict_name):
    stack = []
    result_txt = []
    stack.append(dict_name)
    while len(stack) != 0:
        temp_name = stack.pop()
        try:
            temp_name2 = os.listdir(temp_name)
            for eve in temp_name2:
                stack.append(temp_name + "\\" + eve)  # 维持绝对路径的表达
        except NotADirectoryError:
            result_txt.append(temp_name)
    return result_txt

p1=['.\全集\天龙八部.txt']
p2=['.\全集\神雕侠侣.txt']
path_list = DFS_file_search(r".\全集")

path_list=p2
# path_list=p2

# path_list 为包含所有小说文件的路径列表
ttext = []
for path in path_list:
    with open(path, "r", encoding="ANSI") as file:
        text = [line.strip("\n").replace("\u3000", "").replace("\t", "") for line in file][3:]
        ttext += text
# ttext 存储语料库，其中以每一个行读取，删除无效字符



# 汉语、标点符号都当作有效的字符
String_str=["\u3002","\uff1b","\uff0c","\uff1a","\u201c","\u201d","\uff08","\uff09","\u3001","\uff1f","\u300a","\u300b"]
# 让文本只保留汉字与汉字标点
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    elif uchar in String_str:
        return True
    else:
        return False
def format_str(content):
    content_str = ''
    for i in content:
        if is_chinese(i):
            content_str = content_str + i
    return content_str


ttext0=[]
for j in range(len(ttext)):
    ttext0.append(format_str(ttext[j]))
with open("preprocess.txt", "w", encoding="utf-8") as f:
    for line in ttext0:
        if len(line) > 1:
            print(line, file=f)
