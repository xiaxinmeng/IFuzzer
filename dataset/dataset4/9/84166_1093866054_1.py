
import string
str.format("{0[0]}", "hello")  # => "h"
string.Formatter().format("{0[0]}", "hello")  # => "h"
str.format("{a[0]}", a="hello")  # => "h"
string.Formatter().format("{a[0]}", a="hello")  # => "h"
