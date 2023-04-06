
import ScriptingBridge

command = """cd '' && '/Library/Frameworks/Python.framework/Versions/3.10/bin/python3'  '/Users/ronald/issuequery.py'  && echo Exit status: $? && exit 1"""

app = ScriptingBridge.SBApplication.applicationWithBundleIdentifier_("com.apple.Terminal")

app.activate()
res = app.doScript_in_(command, None)
print(res)
