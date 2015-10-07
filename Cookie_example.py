#-*-coding:utf-8 -*-
import urllib
import urllib2
import json
import cookielib
import sys
type = sys.getfilesystemencoding()

yuanshi_url = "http://www.zhihu.com"

#声明一个MozillaCookieJar对象实例来保存cookie
cookie_jar = cookielib.MozillaCookieJar()

#读取本地cookie文件   
cookies = open('cookies.txt').read()

#加载Cookie数据到cookie_jar
for cookie in json.loads(cookies):  
	cookie_jar.set_cookie(cookielib.Cookie(version=0, name=cookie['name'], value=cookie['value'], port=None, port_specified=False, domain=cookie['domain'], domain_specified=False, domain_initial_dot=False, path=cookie['path'], path_specified=True, secure=cookie['secure'], expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False))      

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
cookie_handler = urllib2.HTTPCookieProcessor(cookie_jar)

#添加HTTP头部，模拟浏览器
headers = {
			"GET":"http://www.zhihu.com",
			"Host":"www.zhihu.com",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36"
			}
request = urllib2.Request(yuanshi_url)
for key in headers:
	request.add_header(key,headers[key])

#绑定handler，创建一个自定义的opener	
opener = urllib2.build_opener(cookie_handler)

#请求网页，返回句柄
response = opener.open(request)

#读取并返回网页内容
page = response.read()

print page.decode('UTF-8').encode(type)