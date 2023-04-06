output = io.StringIO()
csvData = [1, 2, 'a', 'He said "what do you mean?"', "Whoa!\rNewlines!"]
writer = csv.writer(output,lineterminator='\n')
writer.writerow(csvData)
print(repr(output.getvalue())) #does not escape \r as expected