import faulthandler
import locale
from zipfile import ZipFile

faulthandler.enable()

locale.setlocale(locale.LC_ALL, 'de_DE')
out = open("out.zip", "wb") 
archive = ZipFile(out, "w")
archive.writestr("properties.xml", b"<workbookPr/>")
