from datetime import date, datetime, timedelta
(datetime.now()-timedelta((date.today()-date(1,1,1)).days+364)).ctime()