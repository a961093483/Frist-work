import urllib.parse
import urllib.request
import  re
def get_text(a_href):
    #调用函数构建请求对象
    request = handle_request(a_href)
    #发送请求，获得相应
    content = urllib.request.urlopen(request).read().decode()
    #用正则解析内容
    pattern = re.compile(r'<div class="neirong">(.*?)</div>',re.S)
    lt = pattern.findall(content)
    print(lt)
    return lt[0]
def parse_content(content):
    #写正则
    pattern = re.compile(r'<h3><a href="(/lizhi/qianming/\d+\.html)"><b>(.*?)</b></a></h3>')
    #返回的it是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中第一个小括号匹配到的内容，元组中第二个元素就是正则中第二个小括号内容
    it = pattern.findall(content)
    # print(it)
    #遍历列表
    for href_title in it:
        a_href = 'http://www.yikexun.cn' + href_title[0]
        #获取标题
        title = href_title[-1]
        #想a_href发送请求，获取相应内容
        text = get_text(a_href)
        #写入到html文件中
        string = '<h1>%s</h1>%s'%(title,text)
        with open('lizhi7.html','a',encoding = 'utf8')as fp:
            fp.write(string)

    # print(it)
    # print(len(it))

def handle_request(url,page=None):
    if page!=None:
        url = url + str(page) + '.html'
    #构建一个请求对象
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    #print(url)
    request = urllib.request.Request(url=url,headers=headers)
    return request
def main():
    url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
    stage_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码:'))
    for page in range(stage_page,end_page+1):
        #根据url和page去生成指定的request
        request = handle_request(url,page)
        #发送请求
        content = urllib.request.urlopen(request).read().decode()
        #解析内容
        parse_content(content)



if __name__ == '__main__':
    main()
