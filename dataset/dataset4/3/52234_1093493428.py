posturl='https://sinojellycn:123456@storage.msn.com/storageservice/MetaWeblog.rpc'
username="sinojellycn"
password="123456"

blog = pyblog.WordPress(posturl, username, password)
content = {"description":'Test description6', "title":'Test article6'}
blog.new_post(content, blogid = "1") 