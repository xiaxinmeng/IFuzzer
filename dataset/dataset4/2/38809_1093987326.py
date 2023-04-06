import urllib

url = "http://adds.aviationweather.noaa.gov/metars/index.php"

params = urllib.urlencode({ "station_ids" : "KJFK", 
				"hoursStr" : "most recent only", 
				"std_trans" : "standard", 
				"chk_metars" : "on",
				"submit":"Submit"})