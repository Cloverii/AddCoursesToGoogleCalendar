# -*- coding: utf-8 -*-
import json
import urllib  
import urllib2
import hashlib
import cookielib

def md5(str):
    return hashlib.md5(str).hexdigest()

def getCourses(stuID, password):
    schoolcode='10611'
    #var s=md5(yhm+md5(obj.value).substring(0,30).toUpperCase()+schoolcode).substring(0,30).toUpperCase();
    pswdMd5 = md5(stuID + md5(password)[0:30].upper()+schoolcode)[0:30].upper()
    #print pswdMd5
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({  
        'Sel_Type':'STU',
        'txt_dsdsdsdjkjkjc':stuID,
        'efdfdfuuyyuuckjg':pswdMd5
    })
    req = urllib2.Request(url = 'http://222.198.128.126/_data/index_login.aspx', data = postdata)
    res = opener.open(req)
    #print res.read()

    postdata = urllib.urlencode({  
        'Sel_XNXQ':'20161',
        'rad':'on',
        'px':'1'
    })
    req = urllib2.Request(url = 'http://222.198.128.126/znpk/Pri_StuSel_rpt.aspx', data = postdata)
    res = opener.open(req)
    #res = opener.open('http://202.202.1.176:8080/znpk/Pri_StuSel_rpt.aspx',data = postdata)
    str = res.read()
    return str.decode('gb2312').encode('utf-8')
    
def getExCourses():
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdata = urllib.urlencode({
        'stuNum':'20144666'
    })
    req = urllib2.Request(url = 'http://syjx.cqu.edu.cn/admin/schedule/getStudentSchedule', data = postdata)
    res = opener.open(req)
    str = res.read()
    return str

    
def main():
    with open('conf.json', 'r') as f:    
        conf = json.load(f)
        stuID = ""
        password = conf['password']
    courses = getCourses(stuID, password)
    #print courses
    exCourses = getExCourses()
    #print exCourses
    path = 'course.txt'
    with open(path, "w") as f:
        f.write(courses)

if __name__ == '__main__':
    main()
