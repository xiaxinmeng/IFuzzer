db_credentials = "SECRET"
sys.stdout.write("Content-type: text/json\r\n\r\n")
sys.stdout.write(json.dumps({"text": "This is a Test"}))