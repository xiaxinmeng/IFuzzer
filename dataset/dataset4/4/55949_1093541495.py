sourceText = open("source.xml", "rU").readlines()
targetText = open("target.xml", "rU").readlines()

html_diff = difflib.HtmlDiff(tabsize=4)
result = html_diff.make_file(sourceText, targetText, "Source", "Target", context=True, numlines=10)
f = open('c:/libdiff_html.html', 'w')
f.write(result)
finish()