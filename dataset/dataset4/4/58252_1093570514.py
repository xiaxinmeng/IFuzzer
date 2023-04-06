# FAILS - Python 2.7, 2.6, 2.5
import urllib2
url = "http://info.kingcounty.gov/health/ehs/foodsafety/inspections/XmlRest.aspx?Zip_Code=98199"
xml_str = urllib2.urlopen(url).read() # Raises httplib.IncompleteRead

# FAILS - Python 3.2, 3.1
import urllib.request
url = "http://info.kingcounty.gov/health/ehs/foodsafety/inspections/XmlRest.aspx?Zip_Code=98199"
xml_str = urllib.request.urlopen(url).read() # Raises http.client.IncompleteRead

# SUCCEEDS - Python 2.7, 2.6, 2.5
import urllib
url = "http://info.kingcounty.gov/health/ehs/foodsafety/inspections/XmlRest.aspx?Zip_Code=98199"
xml_str = urllib.urlopen(url).read()
dom = xml.dom.minidom.parseString(xml_str) # Verify XML is complete
print("urllib:  %d bytes received and parsed successfully"%len(xml_str))