#coding: utf-8
import m
import cs
from bottle import template

##
#Just a Email sending tester,
##
# -*- coding: utf-8 -*-

import email
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib


import smtplib,email,sys
from email.Message import Message

smtpserver='smtp.126.com'
smtpuser='uiemail@126.com'
smtppass='uiemail@126'
smtpport='25'

def connect():
    "connect to smtp server and return a smtplib.SMTP instance object"
    server=smtplib.SMTP(smtpserver,smtpport)
    server.ehlo()
    server.login(smtpuser,smtppass)
    return server
    
def sendmessage(server,to,subj,content):
    "using server send a email"
    msg = MIMEMultipart()
    msg['Mime-Version']='1.0'
    msg['From']    = smtpuser
    msg['To']      = to
    msg['Subject'] = subj
    msg['Date']    = email.Utils.formatdate()          # curr datetime, rfc2822
    msg.set_payload(content)
  #  try:    
    failed = server.sendmail(smtpuser,to,msg.as_string())   # may also raise exc


   # except Exception ,ex:
    #    print Exception,ex
     #   print 'Error - send failed'
    #else:
     #   print "send success!"

def sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText):

        strFrom = fromAdd
        strTo = ', '.join(toAdd)

        server = authInfo.get('server')
        user = authInfo.get('user')
        passwd = authInfo.get('password')

        if not (server and user and passwd) :
                print 'incomplete login info, exit now'
                return

        # 设定root信息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        #设定纯文本信息
#        msgText = MIMEText(plainText, 'plain', 'utf-8')
#        msgAlternative.attach(msgText)

        #设定HTML信息
        msgText = MIMEText(htmlText, 'html', 'utf-8')
        msgAlternative.attach(msgText)

       #设定内置图片信息
#        fp = open('test.jpg', 'rb')
#        msgImage = MIMEImage(fp.read())
#        fp.close()
#        msgImage.add_header('Content-ID', '<image1>')
#        msgRoot.attach(msgImage)

       #发送邮件
        smtp = smtplib.SMTP()
       #设定调试级别，依情况而定
        smtp.set_debuglevel(1)
        smtp.connect(server)
        smtp.login(user, passwd)
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
#        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()
        return

def get_login_code(email):
	m = cs.usememcache()
	import hashlib
	import time

	conflictCode = 0
	timestamp = int(time.time())
	code = hashlib.md5('%s_%d_%d' % (email, timestamp, conflictCode)).hexdigest().upper()
	while(m.get(code)):
		conflictCode += 1
		code = hashlib.md5('%s_%d_%d' % (email, timestamp, conflictCode)).hexdigest().upper()

	m.set('login_code_%s' % email, code)
	m.set(code, '1')
	return code

def send_ui_email(email):
        authInfo = {}
        authInfo['server'] = 'smtp.126.com'
        authInfo['user'] = 'uiemail@126.com'
        authInfo['password'] = 'uiemail@126'
        fromAdd = 'uiemail@126.com'
        toAdd = [email]
	loginCode = get_login_code(email)
        subject = 'A new login code:', loginCode
        plainText = '测试登录 http://192.168.0.3:8888/c?de=%s' % loginCode
        htmlText = '<B><a href="http://192.168.0.3:8888/c?de=%s">点此登录</a></B>' % loginCode
        #sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText)
	to = toAdd
	subj = subject
	text = plainText
    	server=connect()
    	sendmessage(server,to,subj,text)    
	return dict(email = email, code = loginCode)
##
#Just a DB tester, ORM:MySQL, PostgreSQLi...
##
def hello():
#	m.db.connect()
	users = m.User().select().limit(10)
#	m.db.close()
	username = ''
	for user in users:
		 username = username + user.username		
	
	return template('<b>Hello {{name}}</b>!', name=username)

def save_post(title = ' ', content = ' '):
#	m.db.connect()
	status = 'OK'
	try:
		blog = m.Blog()
		blog.title = title
		blog.content = content
		blog.save()
	except:
		status = 'NO'
#	m.db.close()
	return dict(post_status = status, title = title, content = content)

def list_post(page = 0):
	page_index = int(page)
	m.db.connect()
	blogs = m.Blog.select().limit(20).order_by(m.Blog.title.desc())
	showblog = 'Blog list'
	return dict(blogs = blogs)

def show_post_form():
	return 'hi'

##
#Just a cache tester, Memcached, Redis...
##
def test_redis_set(key = ' ', value = ' '):
	r = cs.useredis()
	r.set(key, value)
	return r.get(key)

def test_redis_get(key):
	r = cs.useredis()
	return r.get(key)

def test_memcache_set(key = ' ', value = ' '):
	m = cs.usememcache()
	m.set(key, value)
	return m.get(key)

def test_memcache_get(key):
	m = cs.usememcache()
	m.disconnect_all()
	return m.get(key)
