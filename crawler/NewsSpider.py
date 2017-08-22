import requests
import os
import re
from lxml import etree


def StringListSave(save_path,filename,myPageResults):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path=save_path+"/"+filename+".txt"
    with open(path,"w+") as fp:
        for r in myPageResults:
            print("this is second",r[0],r[1])
            fp.write("%s\t\t%s\n" % (r[0],r[1]))

def Page_Info(myPage):
    '''Regex'''
    mypage_info=re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>',myPage,re.S)
    return mypage_info


def New_Page_Info(new_page):
    dom=etree.HTML(new_page)
    # xpath使用路径表达式来选取文档中的节点或节点集
    new_items=dom.xpath('//tr/td/a/text()')
    new_urls=dom.xpath('//tr/td/a/@href')
    assert(len(new_items)==len(new_urls))
    return zip(new_items,new_urls)


def Spider(url):
    i=0
    print("downloading",start_url)
    myPage=requests.get(url).content.decode("gbk")
    myPageResults=Page_Info(myPage)
    save_path="wyNews"
    filename=str(i)+"_"+u"新闻排行榜"
    StringListSave(save_path,filename,myPageResults)
    i+=1
    for item,url in myPageResults:
        print("downloading url ",url)
        new_page=requests.get(url).content.decode("gbk")
        newPageResults=New_Page_Info(new_page)
        filename=str(i)+"_"+item
        StringListSave(save_path,filename,newPageResults)
        i+=1

if  __name__=="__main__":
    print("start")
    start_url="http://news.163.com/rank/"
    Spider(start_url)
    print("end")