#coding=gbk      ###��������������
import csv
# with open('E:\\PycharmProjects\\ForTest\\1.csv',newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# with open('E:\\PycharmProjects\\ForTest\\1.csv','a',newline='',encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['jieshu','34','4'])
# with open('E:\\PycharmProjects\\ForTest\\1.csv',newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# #######�����ʼ������ı���#######
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# mail_host='smtp.isoftstone.com'
# mail_user='kehana'
# mail_pass='1QAZ@2WSX'
# sender='kehana@isoftstone.com'
# receivers=['cainiaoke@163.com']
# content=input('�������ʼ����ģ�')
# message=MIMEText(content,'plain','utf-8')   #�������ĸ�ʽ
# subject=input('�������ʼ����⣺')
# message['Subject']=Header(subject,'utf-8')    #���������ʽ
# message['From']=sender
# message['To']=receivers[0]
# try:
#     smtpObj=smtplib.SMTP()
#     smtpObj.connect(mail_host,25)
#     ##��Щ���俪����SSl��֤��������������Ҫ�滻Ϊ
#     # smtpObj=smtplib.SMTP_SSL(mail_host)
#     smtpObj.login(mail_user,mail_pass)
#     smtpObj.sendmail(sender,receivers,message.as_string())
#     smtpObj.quit()
#     print('success')
# except smtplib.SMTPException as e:
#     print('error',e)

# #######�����ʼ�����������#######
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# from email.header import Header
# #���õ�¼�Լ���������Ϣ
# mail_host='smtp.isoftstone.com'
# mail_user='kehana'
# mail_pass='1QAZ@2WSX'
# sender='kehana@isoftstone.com'
# receivers='cainiaoke@163.com'
# #����email��Ϣ�����һ��MIME������������Ϣ
# message=MIMEMultipart()
# message['From']=sender
# message['To']=receivers
# biaoti=input('�������ʼ����⣺')
# message['Subject']=biaoti
# #������ĺ�2������
# with open('E:\\PycharmProjects\\ForTest\\zhihu.html','r',encoding='utf-8') as h:  #encoding='utf-8'��ֹ���ֱ�������
#     content=h.read()
# Content=MIMEText(content,'html','utf-8')
# with open('E:\\PycharmProjects\\ForTest\\tmp1.txt','r') as t:
#     content2=t.read()
# fujian1=MIMEText(content2,'plain','utf-8')
# fujian1['Content-Type']='application/octet-stream'
# fujian1['Content-disposition']='attachment;filename="tmp.txt"'
# with open('E:\\PycharmProjects\\ForTest\\1.JPG','rb') as j:
#     picture=MIMEImage(j.read())
#     picture['Content-Type']='application/octet-stream'
#     picture['Content-disposition']='attachment;filename="1.jpg"'
# message.attach(Content)
# message.attach(fujian1)
# message.attach(picture)
# try:
#     smtpObj=smtplib.SMTP()
#     smtpObj.connect(mail_host,25)
#     smtpObj.login(mail_user,mail_pass)
#     smtpObj.sendmail(sender,receivers,message.as_string())
#     print('success')
#     smtpObj.quit()
# except smtplib.SMTPException as e:
#     print('error',e)

# #����Ƿ�װpythonģ�顣��һ�ַ�����
# try:
#     import requests
# except ImportError:
#     print("ģ�鲻����")
# #����Ƿ�װpythonģ�顣�ڶ��ַ�����
# name=input("������ģ�����ƣ�")
# try:
#     import name
# except ImportError:
#     print("ģ�鲻����")
# #����Ƿ�װpythonģ�顣�����ַ�����
# name=input("������ģ�����ƣ�")
# code="import "+name
# try:
#     exec(code)
# except ImportError:
#     print("ģ�鲻����")
# #����Ƿ�װpythonģ�顣�����ַ�����
# import os
# name=input("������ģ������")
# all=os.popen("pip list").read()
# if name in all:
#     print("ģ���Ѱ�װ")
# else:
#     print("ģ��δ��װ")

# import requests
# res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# print(res.encoding)  #�鿴��ҳ�ı����ʽ
# # res.encoding='gbk'   #�޸���ҳ�ı����ʽ
# novel=res.text   #text��ʾת��Ϊ�ı���ʽ
# #novel=res.status_code  #status_code��ʾ��������Ƿ�ɹ���200���ɹ���100�������������403����ֹ���ʣ�503��������������
# #print(novel[:800])  #��ӡǰ800��
# # novel1=novel[:100]
# # print(novel1)
# S=open('���������塷.txt','a')
# S.write(novel)
# S.close()

# import requests
# res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# print(res.status_code)
# novel=res.text
# print(novel[:200])
# s=open("���������塷.txt","a+")
# s.write(novel)
# s.close()

# import requests
# res=requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
# p=res.content   #������ͼƬ��content
# file=open("ͼƬ.jpg","wb")   #t��������wb
# file.write(p)
# file.close()

# import requests
# huoqu = requests.get ( 'https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html' )
# print ( huoqu.text )
# from bs4 import BeautifulSoup
# jiexi=BeautifulSoup(huoqu.text,'html.parser')
# # print(jiexi)
# tiqus=jiexi.find_all(class_='books')
# print(tiqus)
# for tiqu in tiqus:
#     kind=tiqu.find('h2')
#     title=tiqu.find(class_="title")
#     info=tiqu.find(class_="info")
#     print(kind,'\n',title,'\n',info,'\n')
    # print(' ',kind.text,'\n',title['href'],'\n',title.text,'\n',info.text,'\n')

# import requests
# huoqu=requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
# # print(huoqu.text)
# from bs4 import BeautifulSoup
# jiexi=BeautifulSoup(huoqu.text,'html.parser')
# tiqus=jiexi.find_all(class_='comment-content')
# print(tiqus)
# for tiqu in tiqus:
#     print(tiqu.text)

# import requests
# from bs4 import BeautifulSoup
# url=('http://books.toscrape.com/')
# huoqu=requests.get(url)
# jiexi=BeautifulSoup(huoqu.text,"html.parser")
# tiqus=jiexi.find('ul',class_="nav").find('ul').find_all('li')
# # print(tiqus)
# for tiqu in tiqus:
#     name=tiqu.find('a')
#     print(name.text.strip()) #strip()��ʾȥ���ո�Ϳ���

# #��ӡ��������star���۸�
# import requests
# from bs4 import BeautifulSoup
# url=('http://books.toscrape.com/')
# huoqu=requests.get(url)
# jiexi=BeautifulSoup(huoqu.text,'html.parser')
# tiqus=jiexi.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
# # print(tiqus)
# for tiqu in tiqus:
#     name=tiqu.find('h3').find('a')
#     price=tiqu.find(class_="price_color")
#     star=tiqu.find('p',class_="star-rating")
#     print(name['title'],price.text,star['class'][1])

# import requests
# from bs4 import BeautifulSoup
# huoqu=requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/')
# jiexi=BeautifulSoup(huoqu.text,'html.parser')
# tiqus=jiexi.find_all('header',class_="entry-header")
# # print(tiqus)
# for tiqu in tiqus:
#     shijian=tiqu.find('time')
#     biaoti=tiqu.find('h2')
#     lianjie=tiqu.find('a')
#     print(biaoti.text,'\n',lianjie['href'],'\n',shijian.text,'\n')

##�Ѷ���TOP250����� ���/��Ӱ��/����/�Ƽ���/���� ����ȡ����
# import requests
# from bs4 import BeautifulSoup
# #requests.get����418��404��ctrl+shift+i����Network,ALL,����һ��Name����������ұ߻����Requetst Headers,������������user-agent:��ֵ��headers��ע��{ }����������������
# headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url='https://movie.douban.com/top250?start=0&filter='
# huoqu=requests.get(url,headers=headers)
# jiexi=BeautifulSoup(huoqu.text,'html.parser')
# tiqus=jiexi.find('ol',class_="grid_view").find_all('li')
# #print(tiqus)
# for tiqu in tiqus:
#     xuhao=tiqu.find('em',class_="").text
    # name=tiqu.find_all('span',class_="title")
    # pingfen=tiqu.find('span',class_="rating_num")
    # tuijianyu=tiqu.find('span',class_="inq")
    # lianjie=tiqu.find('a',class_="")
    # print(' ',xuhao.text,'\n',name.text,'\n',tuijianyu.text,'\n',pingfen.text,'\n',lianjie['href'],'\n')
    # print(xuhao.text)

## ������ԭ���ϡ���ϸ������̵�URL
# import requests
# from bs4 import BeautifulSoup
# url='http://www.xiachufang.com'
# headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# huoqu=requests.get(url+'/explore/',headers=headers)
# jiexi=BeautifulSoup(huoqu.text,'html.parser')
# tiqus=jiexi.find(class_="normal-recipe-list").find_all('li')
# for tiqu in tiqus:
#     name=tiqu.find('img')
#     yuanliao=tiqu.find(class_="ing ellipsis")
#     lianjie1=tiqu.find(class_="name").find('a')
#     lianjie2=lianjie1['href']
#     # print(name['alt'])
#     # print(yuanliao.text.strip())
#     print(' ��  ����'+name['alt'],'\n','ԭ���ϣ�'+yuanliao.text.strip(),'\n','��  �ӣ�',url+lianjie2,'\n')

##���/��Ӱ��/����/�Ƽ���/����
# import requests
# from bs4 import BeautifulSoup
# for i in range(10):  ##��ȡ����ҳ����
#     url='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
#     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#     huoqu=requests.get(url,headers=headers)
#     jiexi=BeautifulSoup(huoqu.text,'html.parser')
#     tiqus=jiexi.find(class_="grid_view").find_all('li')
#     for tiqu in tiqus:
#         xuhao=tiqu.find(class_="").text
#         name=tiqu.find(class_="title").text
#         pingfen=tiqu.find(class_="rating_num").text
#         lianjie=tiqu.find('a')['href']
#         if tiqu.find('span',class_="inq") != None:  ##�ж��Ƽ����Ƿ�Ϊ��
#             tuijianyu=tiqu.find('span',class_="inq").text
#             print(' ��  �ţ�'+str(xuhao),'\n','��Ӱ����'+name,'\n','��  �֣�'+str(pingfen),'\n','�Ƽ��'+tuijianyu,'\n','��  �ӣ�'+str(lianjie),'\n')
#         else:
#             print(' ��  �ţ�'+str(xuhao),'\n','��Ӱ����'+name,'\n','��  �֣�'+str(pingfen),'\n','��  �ӣ�'+str(lianjie),'\n')

# import requests
# from bs4 import BeautifulSoup
# from urllib.request import quote   ###����ת��ΪURL
# a=input('�������Ӱ����')
# b=a.encode('gbk')
# url1='http://s.ygdy8.com/plus/s0.php?typeid=1&keyword='+quote(b)
# huoqu1=requests.get(url1)
# huoqu1.encoding='gbk'
# jiexi1=BeautifulSoup(huoqu1.text,'html.parser')
# try:
#     tiqu1=jiexi1.find(class_="co_content8").find('table').find('a')['href']
#     # print(tiqu1)
#     if tiqu1:
#         url2='https://www.ygdy8.com'+tiqu1
#         # print(url2)
#         huoqu2=requests.get(url2)
#         huoqu2.encoding='gbk'
#         jiexi2=BeautifulSoup(huoqu2.text,'html.parser')
#         lianjie=jiexi2.find('div',id="Zoom").find('span').find('table').find('a')['href']
#         print(lianjie)
#     else:
#         print('û�� ��'+a+'�� ����������')
# except:
#     print('û���ҵ���Ӱ')

#encoding=utf-8
# from urllib.request import quote
# from bs4 import BeautifulSoup
# import requests
# # name=input('������������֣�')
# # name1=name.encode('utf-8')
# # url='https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w='+quote(name)
# # huoqu=requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=68293098210396354&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# # tiqus=huoqu.json()
# # tiqu_list=tiqus['data']['song']['list']
# # print(tiqu_list)
# # for tiqu1 in tiqu_list:
# #     print('��������'+tiqu1['name'])
# #     print('ר������'+tiqu1['album']['name'])
# #     print('�������ӣ�'+'https://y.qq.com/n/yqq/song/'+tiqu1['mid']+'.html')
# #     url1='https://y.qq.com/n/yqq/song/'+tiqu1['mid']+'.html'
# #     huoqu1=requests.get(url1)
# #     jiexi=BeautifulSoup(huoqu1.text,'html.parser')
# #     tiqu2=jiexi.find(class_="lyric__cont_box")
# #     print('��ʣ�'+tiqu2.text)

# import json
# a=[1,2,3,4]
# b=json.dumps(a)   #dumps�ǽ��б���ֵ�ת��Ϊjson�ַ���
# print(type(a))
# print(type(b))
# c=json.loads(b)    #loads�ǽ�json�ַ���ת��Ϊ�б�����ֵ�
# print(c)
# print(type(c))

# ###��ȡ���ֵĸ�����Ϣ
# import requests
# from urllib.request import quote   ####quote�ǽ���ASCII���루ASCII����ָ�������֣���ĸ��������ţ����ַ�ת��ΪURL����
# a=input('������������֣�')
# # geshou=quote(a)
# for i in range(5):
#     params={
#     'ct':'24',
#     'qqmusic_ver':'1298',
#     'new_json':'1',
#     'remoteplace':'txt.yqq.song',
#     'searchid':'56587706012726378',
#     't':'0',
#     'aggr':'1',
#     'cr':'1',
#     'catZhida':'1',
#     'lossless':'0',
#     'flag_qc':'0',
#     'p':str(i+1),
#     'n':'10',
#     'w':a,
#     'g_tk_new_20200303':'5381',
#     'g_tk':'5381',
#     'loginUin':'0',
#     'hostUin':'0',
#     'format':'json',
#     'inCharset':'utf8',
#     'outCharset':'utf-8',
#     'notice':'0',
#     'platform':'yqq.json',
#     'needNewCode':'0',
#     }
#     url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
#     huoqu=requests.get(url,params=params)
#     tiqus=huoqu.json()
#     tiqu_list=tiqus['data']['song']['list']
#     for music in tiqu_list:
#         print('��������'+music['name'])
#         print('ר������'+music['album']['name'])
#         print('�������ӣ�'+'https://y.qq.com/n/yqq/song/'+music['mid']+'.html''\n\n')

# ###��ȡ�ܽ��׸��
# import requests
# import json
# # ����requests,jsonģ��
# url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
# headers = {
#     'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
#     # ����������ʲô�豸��ʲô������Ϸ���
#     }
# for x in range(5):
#     params = {
#     'ct':'24',
#     'qqmusic_ver': '1298',
#     'new_json':'1',
#     'remoteplace':'sizer.yqq.lyric_next',
#     'searchid':'94267071827046963',
#     'aggr':'1',
#     'cr':'1',
#     'catZhida':'1',
#     'lossless':'0',
#     'sem':'1',
#     't':'7',
#     'p':str(x+1),
#     'n':'10',
#     'w':'�ܽ���',
#     'g_tk':'1714057807',
#     'loginUin':'0',
#     'hostUin':'0',
#     'format':'json',
#     'inCharset':'utf8',
#     'outCharset':'utf-8',
#     'notice':'0',
#     'platform':'yqq.json',
#     'needNewCode':'0'
#     }
#     res = requests.get(url, params = params)
#     # print(params)
#     # ���ظ���ҳ����ֵ��res
#     jsonres = json.loads(res.text)
#     #ʹ��json������res.text
#     list_lyric = jsonres['data']['lyric']['list']
#     #һ��һ���ȡ�ֵ䣬��ȡ��ʵ��б�
#     for lyric in list_lyric:
#     #lyric��һ���б�x���������Ԫ��
#         print(lyric['content'])
#     # ��contentΪ�������Ҹ��

###���100����
# import requests
# gs=input('�������ݹ�˾���ƣ�')
# dh=input('�������ݵ��ţ�')
# mobile=input('�������ֻ�����λ��')
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# url='https://www.kuaidi100.com/query?type='+gs+'&postid='+dh+'&temp=0.8823894021412677&phone='+mobile
# print(url)
# huoqu=requests.get(url,headers=headers)
# tiqus=huoqu.json()
# print(tiqus['data'][0]['context'])
# # print(huoqu.text)

####��csv�ļ���д������
# import csv
# csv_file=open('demo.csv','a',newline='',encoding='gbk')
# xieru=csv.writer(csv_file)
# xieru.writerow(['��������','10'])
# xieru.writerow(['���Ҹ�������','9'])
# csv_file.close()
####��ȡcsv�ļ��е�����
# csv_file=open('demo.csv','r',newline='')
# du=csv.reader(csv_file)
# for row in du:
#     print(row)
# csv_file.close()

####��xlsx���д������
import openpyxl
# demo1=openpyxl.Workbook()
# sheet=demo1.active
# sheet.title='first'
# row1=[['����','�ձ�','�й�'],['����','����','ŷ��']]
# for i in row1:
#     sheet.append(i)
# demo1.save('demo1.xlsx')
####��ȡxlsx������������
# demo1=openpyxl.load_workbook('demo1.xlsx')
# sheetname=demo1.sheetnames
# print(sheetname)
# sheet=demo1['first']
# A1_cell=sheet['A1']
# A1_value=A1_cell.value
# print(A1_value)

# ###��ȡ���ֵĸ�����Ϣ��������excel
# import requests,openpyxl
# from urllib.request import quote   ####quote�ǽ���ASCII���루ASCII����ָ�������֣���ĸ��������ţ����ַ�ת��ΪURL����
#
# excel=openpyxl.Workbook()  #����һ��excel
# sheet=excel.active   #����һ�����
# sheet.title='song_list'   #���������
# sheet['A1']='������'
# sheet['B1']='ר����'
# sheet['C1']='��������'
# sheet['D1']='����ʱ����s��'
#
# a=input('������������֣�')
# print('---------------------''\n')
# # geshou=quote(a)
# for i in range(5):
#     params={
#     'ct':'24',
#     'qqmusic_ver':'1298',
#     'new_json':'1',
#     'remoteplace':'txt.yqq.song',
#     'searchid':'56587706012726378',
#     't':'0',
#     'aggr':'1',
#     'cr':'1',
#     'catZhida':'1',
#     'lossless':'0',
#     'flag_qc':'0',
#     'p':str(i+1),
#     'n':'10',
#     'w':a,
#     'g_tk_new_20200303':'5381',
#     'g_tk':'5381',
#     'loginUin':'0',
#     'hostUin':'0',
#     'format':'json',
#     'inCharset':'utf8',
#     'outCharset':'utf-8',
#     'notice':'0',
#     'platform':'yqq.json',
#     'needNewCode':'0',
#     }
#     url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
#     huoqu=requests.get(url,params=params)
#     tiqus=huoqu.json()
#     tiqu_list=tiqus['data']['song']['list']
#     for music in tiqu_list:
#         # print('��������'+music['name'])
#         # print('ר������'+music['album']['name'])
#         # print('�������ӣ�'+'https://y.qq.com/n/yqq/song/'+music['mid']+'.html')
#         # print('����ʱ����'+str(music['interval'])+'s''\n\n')
#         name=music['name']
#         zhuanji=music['album']['name']
#         link='https://y.qq.com/n/yqq/song/'+str(music['mid'])+'.html'
#         time=music['interval']
#         sheet.append([name,zhuanji,link,time])   #�����������append��sheet��
#         print('��������'+name+'\n'+'ר������'+zhuanji+'\n'+'�������ӣ�'+link+'\n'+'����ʱ����s��'+str(time)+'\n')
# excel.save('�����嵥.xlsx')  #���沢����excel���

####��ȡ����TOP250ӰƬ��Ϣ������Ϊexcel
# #encoding=utf-8
# import requests,openpyxl
# from bs4 import BeautifulSoup
# from urllib.request import quote
#
# excel=openpyxl.Workbook()
# sheet=excel.active
# sheet.title='list'
# sheet['A1']='���'
# sheet['B1']='ӰƬ��'
# sheet['C1']='����'
# sheet['D1']='����'
# sheet['E1']='����'
#
# for i in range(10):
#     url='https://movie.douban.com/top250?start='+str(i*25)+'&filter='
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#     huoqu=requests.get(url,headers=headers)
#     huoqu.encoding='utf-8'
#     jiexi=BeautifulSoup(huoqu.text,'html.parser')
#     tiqus=jiexi.find(class_="grid_view").find_all('li')
#     for tiqu in tiqus:
#         xuhao=tiqu.find('em').text
#         name=tiqu.find(class_="title").text
#         pingfen=tiqu.find(class_="rating_num").text
#         lianjie=tiqu.find('a')['href']
#         if tiqu.find('span',class_="inq") != None:
#             pingyu=tiqu.find('span',class_="inq").text
#             sheet.append([xuhao,name,pingfen,pingyu,lianjie])
#             print(' ��  �ţ�'+str(xuhao),'\n','ӰƬ����'+name,'\n','��  �֣�'+str(pingfen),'\n','��  �'+pingyu,'\n','��  �ӣ�'+str(lianjie),'\n')
#         else:
#             sheet.append([xuhao,name,pingfen,'������',lianjie])
#             print(' ��  �ţ�'+str(xuhao),'\n','ӰƬ����'+name,'\n','��  �֣�'+str(pingfen),'\n','��  �������','\n','��  �ӣ�'+str(lianjie),'\n')
#
# excel.save('����TOP250.xlsx')

###��֪�û������¼ĳ��վ
# import requests
# from bs4 import BeautifulSoup
# url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# data={
#     'og': 'heheh',
#     'pwd': 'abcd1234',
#     'wp-submit': '��¼',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# login=requests.post(url,headers=headers,data=data)   ##��Ҫ�����û��������ʱ����post����
# print(login)

#selenium�з������÷�
# # ���·��������Դ���ҳ����ȡ��'��ã�֩������'�������
#
# find_element_by_tag_name��ͨ��Ԫ�ص�����ѡ��
# # ��<h1>��ã�֩������</h1>
# # ����ʹ��find_element_by_tag_name('h1')
#
# find_element_by_class_name��ͨ��Ԫ�ص�class����ѡ��
# # ��<h1 class="title">��ã�֩������</h1>
# # ����ʹ��find_element_by_class_name('title')
#
# find_element_by_id��ͨ��Ԫ�ص�idѡ��
# # ��<h1 id="title">��ã�֩������</h1>
# # ����ʹ��find_element_by_id('title')
#
# find_element_by_name��ͨ��Ԫ�ص�name����ѡ��
# # ��<h1 name="hello">��ã�֩������</h1>
# # ����ʹ��find_element_by_name('hello')
#
# #������������������ȡ��������
#
# find_element_by_link_text��ͨ�������ı���ȡ������
# # ��<a href="spidermen.html">��ã�֩������</a>
# # ����ʹ��find_element_by_link_text('��ã�֩������')
#
# find_element_by_partial_link_text��ͨ�����ӵĲ����ı���ȡ������
# # ��<a href="https://localprod.pandateacher.com/python-manuscript/hello-spiderman/">��ã�֩������</a>
# # ����ʹ��find_element_by_partial_link_text('���')

# def pri(n):   #def����һ��������(n)��ʾ�����Ĳ���
#     print(n)    #�˺���ִ�еĹ���
# pri('����')   #����pri�������������

# print('��ɨ������������')
# def step_1():
#     print('ȡ��ɨ��')
# def step_2():
#     print('��ʼ��ɨ����')
# def step_3():
#     print('�Ż�ɨ��')
# step_1()
# step_2()
# step_3()

# class Cat:     #����һ����Cat
#     def __init__(self,new_name,new_age):    #����һ����ʼ�����������Զ����ã�����Ҫ�ֶ�
#         self.name=new_name
#         self.age=new_age
#     def eat(self):   #����һ����ͨ����
#         print('è�ڳ���')
#     def drink(self):   #����һ����ͨ����
#         print('è�ںȰ���')
#     def introduce(self):   #����һ����ͨ����
#         print('%s����%d��'%(self.name,self.age))
# Tom=Cat('��ķ',18)   #ʵ����һ������Tom��������Cat�࣬��ʼ�������е�self�ͱ����Tom,��ʼ�������е�new_name�ͱ����'��ķ',new_age�ͱ����18
# Tom.eat()    #����Tom����Cat������ķ���
# Tom.drink()   #����Tom����Cat������ķ���
# Tom.introduce()    #����Tom����Cat������ķ���

# class Student:    #����һ����Student
#     def __init__(self):    #��ʼ������û�м������
#         self.name=None
#         self.age=None
#     def introduce(self):
#         print(self.name)
# student=Student()    #ʵ����һ�����󣬳�ʼ�������е�self�ͱ����student
# student.name='��ķ'
# student.age=18
# student.introduce()
#
# class Student1:
#     def __init__(self,new_name,new_age):  #��ʼ�������м�����������
#         self.name=new_name
#         self.age=new_age
#     def introduce(self):
#         print(self.name,'\n',self.age)
# student1=Student1('��ķ1',19)
# student1.introduce()

# ###��֪�û������¼ĳ��վ������cookies
# import requests
# url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# data={
#     'og': 'heheh',
#     'pwd': 'abcd1234',
#     'wp-submit': '��¼',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# login=requests.post(url,headers=headers,data=data)   ##��Ҫ�����û��������ʱ����post����
# cookies=login.cookies  ###����requests����login��cookies���ԣ�������ֵ��cookies
# #####���������cookies���벩�ͷ�������
# url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-content/uploads/2019/01/cropped-cobweb-1698801_1920-1-32x32.jpg'
# data_1={
#     'comment': input('�������������ݣ�'),
#     'submit': '��������',
#     'comment_post_ID': '13',
#     'comment_parent': '0'
# }
# comment=requests.post(url_1,headers=headers,cookies=cookies,data=data_1)  ###���ø��ֲ�������
# print(comment.status_code)

# import requests,json
# session=requests.session()
# url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# data={
#     'log': input('�������û�����'),
#     'pwd': input('���������룺'),
#     'wp-submit': '��¼',
#     'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#     'testcookie': '1'
# }
# session.post(url,headers=headers,data=data)
# print(session.cookies)
# cookies_dic=requests.utils.dict_from_cookiejar(session.cookies)   ####��cookiesת��Ϊ�ֵ�
# print(cookies_dic)
# cookies_str=json.dumps(cookies_dic)   ####���ֵ�ת��Ϊjson�ַ���
# print(cookies_str)
# f=open('cookies.txt','w')
# f.write(cookies_str)
# f.close()
# url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# data_1={
#     'comment': input('���������ۣ�'),
#     'submit': '��������',
#     'comment_post_ID': '15',
#     'comment_parent': '0'
# }
# comment=session.post(url_1,headers=headers,data=data_1)
# print(comment.status_code)

###��ȡ����cookies��¼���Ͳ�����
# import requests,json
# session=requests.session()
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
# try:
#     cookies_txt=open('cookies.txt','r')
#     cookies_dic=json.loads(cookies_txt.read())
#     cookies=requests.utils.cookiejar_from_dict(cookies_dic)
#     session.cookies=cookies
# except FileNotFoundError:
#     url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
#     data={
#         'log': input('�������û�����'),
#         'pwd': input('���������룺'),
#         'wp-submit': '��¼',
#         'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
#         'testcookie': '1'
#     }
#     session.post(url,headers=headers,data=data)
#     cookies_dic=requests.utils.dict_from_cookiejar(session.cookies)
#     cookies_str=json.dumps(cookies_dic)
#     f=open('cookies.txt','w')
#     f.write(cookies_str)
#     f.close()
# url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
# data_1={
#     'comment': input('���������ۣ�'),
#     'submit': '��������',
#     'comment_post_ID': '15',
#     'comment_parent': '0'
# }
# comment=session.post(url_1,headers=headers,data=data_1)
# print(comment.status_code)

# #####����С����
# import requests
# import json
# from tkinter import Tk,Button,Entry,Label,Text,END
#
# class YouDaoFanyi(object):
#     def __init__(self):
#         pass
#     def crawl(self,word):
#         url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#         #ʹ��post��Ҫһ������
#         data={'i': word,
#               'from': 'AUTO',
#               'to': 'AUTO',
#               'smartresult': 'dict',
#               'client': 'fanyideskweb',
#               'doctype': 'json',
#               'version': '2.1',
#               'keyfrom': 'fanyi.web',
#               'action': 'FY_BY_REALTIME',
#               'typoResult': 'false'}
#         #����Ҫpost�����ݣ����ֵ����ʽ��¼��data�ڡ�
#         r = requests.post(url, data)
#         #post��Ҫ��������������һ���Ǹղŵ����ӣ�һ����data�����ص���һ��Response����
#         answer=json.loads(r.text)
#         #������Լ�����printһ��r.text�����ݣ�Ȼ�����Ķ�����Ĵ��롣
#         result = answer['translateResult'][0][0]['tgt']
#         return result
#
#
#
# class Application(object):
#     def __init__(self):
#         self.window = Tk()
#         self.fanyi = YouDaoFanyi()
#
#
#         self.window.title(u'�ҵķ���')
#         #���ô��ڴ�С��λ��
#         self.window.geometry('310x370+500+300')
#         self.window.minsize(310,370)
#         self.window.maxsize(310,370)
#         #����һ���ı���
#         #self.entry = Entry(self.window)
#         #self.entry.place(x=10,y=10,width=200,height=25)
#         #self.entry.bind("<Key-Return>",self.submit1)
#         self.result_text1 = Text(self.window,background = 'azure')
#         # ϲ��ʲô����ɫ������������Ŷ��������ɫ��ö����ԣ�http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
#         self.result_text1.place(x = 10,y = 5,width = 285,height = 155)
#         self.result_text1.bind("<Key-Return>",self.submit1)
#
#         #����һ����ť
#         #Ϊ��ť����¼�
#         self.submit_btn = Button(self.window,text=u'����',command=self.submit)
#         self.submit_btn.place(x=205,y=165,width=35,height=25)
#         self.submit_btn2 = Button(self.window,text=u'���',command = self.clean)
#         self.submit_btn2.place(x=250,y=165,width=35,height=25)
#
#         #����������
#         self.title_label = Label(self.window,text=u'������:')
#         self.title_label.place(x=10,y=165)
#         #������
#
#         self.result_text = Text(self.window,background = 'light cyan')
#         self.result_text.place(x = 10,y = 190,width = 285,height = 165)
#         #�س�����
#     def submit1(self,event):
#         #��������ȡ�û������ֵ
#         content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
#         #�����ֵ���͸����������з���
#
#         result = self.fanyi.crawl(content)
#         #�������ʾ�ڴ����е��ı�����
#
#         self.result_text.delete(0.0,END)
#         self.result_text.insert(END,result)
#
#         #print(content)
#
#     def submit(self):
#         #��������ȡ�û������ֵ
#         content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
#         #�����ֵ���͸����������з���
#
#         result = self.fanyi.crawl(content)
#         #�������ʾ�ڴ����е��ı�����
#
#         self.result_text.delete(0.0,END)
#         self.result_text.insert(END,result)
#         print(content)
#     #����ı����е�����
#     def clean(self):
#         self.result_text1.delete(0.0,END)
#         self.result_text.delete(0.0,END)
#
#     def run(self):
#         self.window.mainloop()
#
#
# if __name__=="__main__":
#     app = Application()
#     app.run()

###����Chrome��������÷���
# import time
# from bs4 import BeautifulSoup
# from selenium import webdriver    #����webdirver
# driver=webdriver.Chrome()   #������������Ϊ�ȸ�
# driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')  #����ҳ
# time.sleep(2)
# # label=driver.find_element_by_tag_name('label')  ###��������ȡ��label��ǩ�е��ַ���
# # print(label.text)
# # labels=driver.find_elements_by_tag_name('label')
# # print(type(labels))
# # for i in labels:
# #     print(i)
# teacher=driver.find_element_by_id('teacher')
# teacher.send_keys('�����Ǻ��ɰ�')   ###���������������
# time.sleep(3)
# assistant=driver.find_element_by_name('assistant')
# assistant.send_keys('��ϲ��')
# time.sleep(3)
# button=driver.find_element_by_cldsadass_name('sub')   #�ҵ��ύ��ť
# button.click()      #����ύ����
# time.sleep(5)
# driver.close()

# ##��ȡĳ�׸����������ǰ��ҳ,����ȡ��Ĭģʽ
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options  #��optionsģ�����Options��
# chrome_options=Options()  #ʵ����Options����
# chrome_options.add_argument('--headless')  #�ɹȸ����������Ϊ��Ĭģʽ����ʾ����
# driver=webdriver.Chrome(options=chrome_options)   #���ùȸ�����������ں�̨����
# driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')   #��ȡ��������
# time.sleep(2)
# button=driver.find_element_by_class_name('js_get_more_hot')    #�����������ظ��ࡱ
# button.click()    #ִ�е������
# time.sleep(2)
# comments=driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
# ###��������find��Ϊ���ҵ����۵���������
# print(len(comments))   #��ӡ�ж���������
# for comment in comments:
#     sweet=comment.find_element_by_tag_name('p')  #��ȡÿһ���������������
#     print('���ۣ�%s\n ---\n'%sweet.text)
# driver.close()   #�ر������

#���ýӿڲ���ҳ��
# from flask import Flask,request
# app=Flask(__name__)
# @app.route('/helloo')
# def index():
#     name=request.args.get('name')
#     return '��ã�'+name
# if __name__=='__main__':
#     app.run()

# import re
# text='asdfsahanke,hankekekke,hankehanke'   #�ַ���
# pattern=r'hanke'    #��ʾ��ƥ�������
# pattern=r','  #��ƥ�������
# repl='��'   #�滻����
# print('search:',re.search(pattern,text).group())  #search���ַ���������λ�ÿ�ʼƥ��
# print('match:',re.match(pattern,text).group())   #match��ͷ��ʼƥ��
# print('findall:',re.fullmatch(pattern,text).group())  #fullmatch��Ҫ��ȫƥ��
# print('dinfall:',re.findall(pattern,text))   #ƥ����
# print('finditer:',list(re.finditer(pattern,text)))   #ƥ����
# print('sub-repl�ַ�����',re.sub(pattern,repl,text,count=2))  #�滻ƥ�䵽��
# print('sub-repl�ַ�����',re.subn(pattern,repl,text,count=2))  #�滻ƥ�䵽��,��ͳ�ƴ���

# ########ÿ�춨ʱ��ȡ���ݷ��͵�ָ������
# import requests,schedule,time,smtplib
# from bs4 import BeautifulSoup
# from email.mime.text import MIMEText
# from email.header import Header
# ##��ȡÿ�������Ԥ��
# def weather():
#     headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#     url='http://www.weather.com.cn/weather/101280601.shtml'
#     huoqu=requests.get(url,headers=headers)
#     # print(huoqu.status_code)
#     huoqu.encoding='utf-8'
#     # print(huoqu.text)
#     jiexi=BeautifulSoup(huoqu.text,'html.parser')
#     tiqus=jiexi.find(class_="t clearfix").find(class_="sky skyid lv1 on")
#     # print(tiqus)
#     wendu=tiqus.find(class_="tem").text
#     tianqi=tiqus.find(class_="wea").text
#     fengli=tiqus.find(class_="win").text
#     wind=tiqus.find(class_="win").find('span')
#     # print(wind['title'])
#     report=('�����¶�Ϊ��'+str(wendu)+'  '+'����Ϊ��'+tianqi+' '+wind['title']+' '+fengli).replace('\n','')  ##replaceȥ����ȡ�����еĻ��з�
#     return report
# ##������Ԥ��������ָ������
# def mail(report):   ##������һ����������һ������
#     mail_host='smtp.isoftstone.com'
#     mail_user='kehana'
#     mail_pass='1QAZ@2WSX'
#     sender='kehana@isoftstone.com'
#     receivers='cainiaoke@163.com'
#     message=MIMEText(report,'plain','utf-8')
#     subject='��������Ԥ��'
#     message['Subject']=Header(subject,'utf-8')
#     message['From']=sender
#     message['To']=receivers
#     try:
#         smtpObj=smtplib.SMTP()
#         smtpObj.connect(mail_host,25)
#         smtpObj.login(mail_user,mail_pass)
#         smtpObj.sendmail(sender,receivers,message.as_string())
#         smtpObj.quit()
#         print('success')
#     except smtplib.SMTPException as e:
#         print('error',e)
# ##���ö�ʱ����
# def task():
#     print('��ʼ����')
#     report=weather()
#     mail(report)
#     print('�������')
# schedule.every().day.at("15:51").do(task)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

####����ͬ�����ʶ����վ���º�ʱ
# import requests,time
# start=time.time()   #���ÿ�ʼʱ��   time.time()��ʾ��ǰʱ��
# url_list=['https://www.baidu.com/',
#           'https://www.sina.com/',
#           'https://www.qq.com/',
#           'https://www.163.com/',
#           'http://www.iqiyi.com/',
#           'https://www.tmall.com/',
#           'http://www.sohu.com/',
#           'https://www.dogedoge.com/'
#           ]
# for url in url_list:
#     huoqu=requests.get(url)
#     print(url,huoqu.status_code)
# end=time.time()  #���ý���ʱ��
# print(end-start)   #���������ʱ

####�����첽���ʶ����վ���º�ʱ
# from gevent import monkey  #��gevent���е���monkeyģ��
# monkey.patch_all()    #�����첽����̶���ʽ
# import gevent,time,requests  #����gevent
# start = time.time()    #��¼��ʼʱ��
# url_list = ['https://www.baidu.com/',
#             'https://www.sina.com.cn/',
#             'http://www.sohu.com/',
#             'https://www.qq.com/',
#             'https://www.163.com/',
#             'http://www.iqiyi.com/',
#             'https://www.tmall.com/',
#             'https://www.dogedoge.com/'
#             ]
# def crawler(url):    #����һ������������url����
#     r = requests.get(url)   #��ȡ��վ
#     print(url,time.time()-start,r.status_code)   #��ӡ��Ϣ
# tasks_list = []   #����һ���յ������б�
# for url in url_list:
#     task = gevent.spawn(crawler,url)    #��gevent.spawn����������������
#     tasks_list.append(task)     #������ӵ������б�
# gevent.joinall(tasks_list)    #ִ�������б��е���������Ҳ���ǿ�ʼ��ȡÿһ����վ
# end = time.time()  #��¼����ʱ��
# print(end-start)

#�Ƶ�ʽȥ��һ���б�
# old_list=[1,1,1,2,3,4,5,8,6,7,0,0]
# new_list={item for item in old_list}
# print(new_list)

#ȡ���б��е�ż��
# old_list=[0,1,2,3,4,5,6,7,8,9]
# new_list=[item for item in old_list if item % 2 ==0]   # %2==0��ʾ����2������Ϊ0��Ҳ����ż��
# print(new_list)

#������ɸѡ��ѧ���ɼ�
# old_student_score={
#     '����':{
#         '����':97,
#         '��ѧ':83,
#         'Ӣ��':89
#     },
#     '����':{
#         '����':95,
#         '��ѧ':89,
#         'Ӣ��':80
#     },
#     '�Ǻ�':{
#         '����':100,
#         '��ѧ':93,
#         'Ӣ��':75
#     }
# }
# new_student_score={name:scores for name,scores in old_student_score.items() if scores['��ѧ'] >= 85 }
# print(new_student_score)

#�˷��ھ���
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}x{}={}'.format(j,i,j*i),end=' ')  #format��ʽ������
#     print("")

#windows���ں�̨����.py�ļ�     pythonw test.py > test.log
#windows�²鿴��̨����     tasklist
#windows��ɱ����̨����    taskkill /f /im python.exe

# ###�����첽���ʶ����վ���º�ʱ
# from gevent import monkey  #��gevent���е���monkeyģ��
# monkey.patch_all()    #�����첽����̶���ʽ
# import gevent,time,requests  #����gevent
# start = time.time()    #��¼��ʼʱ��
# url_list = ['https://www.baidu.com/',
#             'https://www.sina.com.cn/',
#             'http://www.sohu.com/',
#             'https://www.qq.com/',
#             'https://www.163.com/',
#             'http://www.iqiyi.com/',
#             'https://www.tmall.com/',
#             'https://www.dogedoge.com/'
#             ]
# def crawler(url):    #����һ������������url����
#     r = requests.get(url)   #��ȡ��վ
#     print(url,time.time()-start,r.status_code)   #��ӡ��Ϣ
# tasks_list = []   #����һ���յ������б�
# for url in url_list:
#     task = gevent.spawn(crawler,url)    #��gevent.spawn����������������
#     tasks_list.append(task)     #������ӵ������б�
# gevent.joinall(tasks_list)    #ִ�������б��е���������Ҳ���ǿ�ʼ��ȡÿһ����վ
# end = time.time()  #��¼����ʱ��
# print(end-start)

#�������
# from gevent import monkey
# monkey.patch_all()
# from gevent.queue import Queue
# import gevent,requests,time
# start=time.time()
# url_list=['https://www.baidu.com/',
#         'https://www.sina.com.cn/',
#         'http://www.sohu.com/',
#         'https://www.qq.com/',
#         'https://www.163.com/',
#         'http://www.iqiyi.com/',
#         'https://www.tmall.com/',
#         'https://www.dogedoge.com/']
# work=Queue()    #�������ж���work
# for url in url_list:
#     work.put_nowait(url)   #��url���������
# def crawler():    #�����������
#     while not work.empty():   #������в�Ϊ��զִ������Ĳ���
#         url=work.get_nowait()   #�Ӷ����ж�ȡurl
#         huoqu=requests.get(url)   #requestsȥ����url
#         print(url,work.qsize(),huoqu.status_code)
# tasks_list=[]   #����һ���������б�
# for x in range(2):   #������������
#     task=gevent.spawn(crawler)    #������������
#     tasks_list.append(task)    #������ӵ��б���
# gevent.joinall(tasks_list)   #joinallִ�������б��е���������
# end=time.time()
# print(end-start)
####