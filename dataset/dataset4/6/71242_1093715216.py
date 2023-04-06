
import zipfile


if __name__ == '__main__':
    with open('__main__.py', "w") as m:
      m.write("print('hello')")
    

    zipf = zipfile.ZipFile('zipapp_bad.zip', 'w', zipfile.ZIP_DEFLATED)
    #add zip comment
    zipf.comment=b"123321"
    zipf.write("__main__.py")
    zipf.close()

    zipf = zipfile.ZipFile('zipapp_good.zip', 'w', zipfile.ZIP_DEFLATED)
    zipf.write("__main__.py")
    zipf.close()
