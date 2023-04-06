
locals()['arg'] = 123  # or locals().setdefault('arg', 123)
# ^ it's okay

locals()[123] = 123  # or locals().setdefault(123, 123)
# ^ completion window is not shown
