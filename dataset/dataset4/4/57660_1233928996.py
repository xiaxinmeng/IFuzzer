
self._scheduler = sched.scheduler(self._harvest_timer, self._harvest_shutdown.wait)
...
self._scheduler.enter(event_harvest_config.report_period_ms / 1000.0, 1, self._harvest_flexible, ())
...
self._scheduler.run()
...