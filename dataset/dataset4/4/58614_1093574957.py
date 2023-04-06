def _decrement_pending_calls(self):
    if self.num_pending_calls == len(self.finished_futures):
         self.event.set()