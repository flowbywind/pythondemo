
import  urllib.request
import re
import  tool

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

    def getPage(self,pageNum):
        try:
            url=self.baseUrl+self.seeLZ+"&pn="+str(pageNum)
            request=urllib.request.Request(url)
            response=urllib.request.urlopen(request)
            return response.read().decode('utf-8')
        except urllib.request.URLError,e:
            if hasattr(e,"reason"):
                print(u"连接百度贴吧失败，错误原因",e.reason)
                return None


    def getTitle(self,page):
        pattern=re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>')
        result=re.search
