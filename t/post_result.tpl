<!DOCTYPE html>
<html lang = "zh-cn">
<head>
<title>
        Tiny Blog v0.0.1
</title>
</head>
<body>
%if post_status == 'OK':
    	<h1>发布成功</h1>
	<p>标题：{{title}}</p>
    	<p>内容：{{content}}</p>
	<a href = "../">返回首页</a>
%else:
    	<h1>发布失败</h1>
	<a href = "../">返回首页</a>
	<a href = "javascript.history.goback()">返回发布页面</a>
%end
</body>
</html>
