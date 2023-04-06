self.assertIn('class="month"', local_month)
cal.cssclass_month_head = "text-center month"
local_month = cal.formatmonthname(2010, 10)
self.assertIn('class="text-center month"', local_month)