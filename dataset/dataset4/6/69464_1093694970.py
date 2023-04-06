pthread_sigmask(SIG_BLOCK, {signum})
try:
    t0 = ...
    ...  # Spawn child, call sigwaitinfo(), etc
finally:
    pthread_sigmask(SIG_UNBLOCK, {signum})
self.assertGreaterEqual(dt, ...)