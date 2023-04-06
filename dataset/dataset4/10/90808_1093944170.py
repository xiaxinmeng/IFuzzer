
for priority in [1, 2, 3, 4, 5]:
  z = scheduler.enterabs(0.01, priority, fun, (priority,))
scheduler.run()
self.assertEqual(l, [1, 2, 3, 4, 5])
