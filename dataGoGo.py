import requests
import json
from threading import Thread
succ_num = 0
def getCur(url,headers):
    global succ_num
    rsp = requests.get(url,headers=headers)
    js = json.loads(rsp.text)
    if js['code'] == -1:
        succ_num + 1
    else:
        succ_num += 1


def get_data(stu_num):
    stu_num = str(stu_num)
    if stu_num.isnumeric() is False:
        return ' 别捣乱哦  '

    global succ_num
    succ_num = 0
    if len(stu_num)!=10:
        return '-1'
    #print("开始学号为："+stu_num+" 的任务")
    thread_num = 100
    #print("已经开启线程数量："+str(thread_num))
 

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    url = stu_num


    threads = []
    for i in range(thread_num):
        t = Thread(target=getCur,name=str(i),args=(url,headers,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()
    #print("成功次数为:",succ_num)
    #print("You have get Data "+str(succ_num*5.4)+"G")
    return str(succ_num*5.4)

print(get_data('asd1112121'))
