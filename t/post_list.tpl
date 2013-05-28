<!DOCTYPE html>
<html lang = "zh-cn">
<head>
<title>
        Tiny Blog v0.0.1
</title>
</head>
<body>
<a href = './p'>Add new posts</a>
%for blog in blogs:
	<fieldset>
		<legend><strong>{{blog.title}}</strong></legend> 
		<p>{{blog.content}}</p>
	</fieldset>
%end

</body>
</html>
