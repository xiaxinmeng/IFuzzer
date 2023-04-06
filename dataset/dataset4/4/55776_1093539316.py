DEFAULT_ERROR_MESSAGE = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
		<title>Error response</title>
	</head>
	<body>
		<h1>Error response</h1>
		<p>Error code %(code)d.</p>
		<p>Message: %(message)s.</p>
		<p>Error code explanation: %(code)s = %(explain)s.</p>
	</body>
</html>
"""