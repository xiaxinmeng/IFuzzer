# File downloaded with “urlopen”, also possible with TarFile.addbuffer API:
with tf.get_file_writer(download_tarinfo) as writer:
    shutil.copyfileobj(urlopen_response, writer)

# SVG file generated on the fly, encoded with UTF-8 and Gzip compressed; not possible with “addbuffer”:
writer = tf.get_file_writer(svgz_tarinfo)
gzip_writer = gzip.GzipFile(fileobj=writer, mode='w')
with io.TextIOWrapper(gzip_writer, 'utf-8') as text_writer:
    svg = xml.sax.saxutils.XMLGenerator(text_writer, 'UTF-8')
    svg.startDocument()
    ...