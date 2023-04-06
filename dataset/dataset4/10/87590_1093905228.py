# In Crostini Chrome OS Linux, the default browser is set to an
# intermediary called `garcon-url-handler`.
# It opens URLs in Chrome running outside the linux VM. This 
# browser does not have access to the Linux filesystem. Some references:
# https://chromium.googlesource.com/chromiumos/platform2/+/master/vm_tools/garcon/#opening-urls
# https://source.chromium.org/search?q=garcon-url-handler

if "garcon-url-handler" in webbrowser.get().name:
  webbrowser.open("http://external-url.com/docs.html")
else:
  webbrowser.open("file:///usr/share/doc/docs.html")