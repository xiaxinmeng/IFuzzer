
import string
str.format("{[0]}", "hello")  # => "h"
string.Formatter().format("{[0]}", "hello")  # => KeyError("")
