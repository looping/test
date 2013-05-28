<!DOCTYPE html>
<html lang = "zh-cn">
<head>
<title>
        Tiny Blog v0.0.1
</title>
</head>
<body>
%if post_status == 'OK':
    	<h1>Post success!</h1>
	<p>{{title}}</p>
    	<p>{{content}}</p>
	<a href = ".">Home</a>
%else:
    	<h1>Post failed!</h1>
	<a href = ".">Home</a>
	<a href = "javascript.history.goback()">Go back</a>
%end
</body>
</html>
