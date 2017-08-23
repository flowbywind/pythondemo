
import  urllib.request
import re
import tool
class BDTB:

    def  __init__(self,baseUrl,seeLZ,floorTag):
        self.baseUrl=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)
        self.floorTag=floorTag
        self.tool=tool.Tool()
        #文件写入对象
        self.file=None
        #楼层标号 初始为1
        self.floor=1
        #默认的标题 如果没有成功获取到标题 则用这个
        self.defaultTitle='bdtb'

    #传入页码 获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            #构建URL
            url=self.baseUrl+self.seeLZ+"&pn="+str(pageNum)
            print("构建后的URL",url)
            request=urllib.request.Request(url)
            response=urllib.request.urlopen(request)
            #返回UTF-8格式编码内容
            result= response.read().decode('utf-8')
            return result
        #无法连接 报错
        except urllib.request.URLError as e:
            if hasattr(e,"reason"):
                print(u"连接百度贴吧失败，错误原因",e.reason)
                return None

    #获取帖子标题
    def getTitle(self,page):
        #得到的标题的正则表达式
        pattern=re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>')
        result=re.search(pattern,page)
        print("getTitle:",result)
        if result:
            return result.group(1).strip()
        else:
            return None

    #获取帖子一共有多少页
    def getPageNum(self,page):
        #获取帖子页数的正则表达式
        pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        result=re.search(pattern,page)
        print("getpageNum:",result)
        if result:
            return result.group(1).strip()
        else:
            return None


    #获取每一层楼的内容，传入页面内容
    def getContent(self,page):
        pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items=re.findall(pattern,page)
        contents=[]
        for item in items:
            #去除标签 同时加换行符
            content="\n"+self.tool.replace(item)+"\n"
            contents.append(content)
        return contents


    def setFileTitle(self,title):
        if title is not None:
            self.file=open(title+".txt","w+",encoding='utf-8')
        else:
            self.file=open(self.defaultTitle+".txt","w+",encoding='utf-8')


    def writeData(self,contents):
        res="";
        try:
            for item in contents:
                if self.floorTag == 1:
                    floorLine="\n"+str(self.floor)+u"-----------------------\n"
                    self.file.write(floorLine)
                res=str(item);
                self.file.write(res)
                self.floor+=1
        except Exception as e:
            print("res:"+res)
            print(e)


    def start(self):
        indexPage=self.getPage(1)
        pageNum=self.getPageNum(indexPage)
        title=self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum==None:
            print("Url已经失效，请重试")
            return
        try:
            print("该帖子共有"+str(pageNum)+"页")
            for i in range(1,int(pageNum)+1):
                print ("正在写入第"+str(i)+"页数据")
                page=self.getPage(i)
                contents=self.getContent(page)
                self.writeData(contents)
        except IOError as e:
            print("写入异常，原因",e.message)
        finally:
            print("写入任务完成")

if  __name__=="__main__":
    print(u"请输入帖子代号")
    # baseURL='http://tieba.baidu.com/p/'+str(input(u'http://tieba.baidu.com/p/')).strip()
    # print("baseUrl",baseURL)
    # seeLZ=input("是否只获取楼主发言，是输入1，否输入0\n")
    # floorTag=input("是否写入楼层信息，是输入1，否输入0\n")
    baseURL="http://tieba.baidu.com/p/4341776212"
    seeLZ=0;
    floorTag=1;
    bdtb=BDTB(baseURL,seeLZ,floorTag)
    bdtb.start()


