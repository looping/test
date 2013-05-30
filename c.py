#coding: utf-8
import m
import cs
import conf
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
        msgText = MIMEText(plainText, 'plain', 'utf-8')
        msgAlternative.attach(msgText)

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
        subject = '邮箱登录验证码：%.5s' % loginCode
	login_link = 'http://%s:%s/c?de=%s' % (conf.__HOSTSERVERADDR__, conf.__LISTENPORT__, loginCode)
        plainText = '登录链接 %s' % (login_link)
        htmlText = '<br />%s,您好：<p>    欢迎使用XXX，现在您可以<B><a href="%s">点此登录</a></B>。<br />    或者在浏览器地址栏中输入 %s<br />    祝您码字愉快！</p>' % (email, login_link, login_link)
        sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText)
	return dict(email = email, code = loginCode)

def gen_token(code):
	token = code 
	return token

def auth_email_code(code):
	status = 'NO'
	m = cs.usememcache()
	is_auth_code = m.get(code)
	if is_auth_code:
		status = 'YES'
		token = gen_token(code)
		m.set(code, token)
	return dict(status = status)

def auth_public_token(token):
	status = 'NO'
	m = cs.usememcache()
	atoken = m.get(token)
	if atoken:
		status = 'YES'
	return status

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
	showblog = '内容列表'
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
