from datetime import date, datetime
format = "%Y-%m-%d"
formatted = date.min.strftime("%Y-%m-%d")
datetime.strptime(formatted, format).date()