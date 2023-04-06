with f._condition: # Lock the Future; yield if completed or add our Waiter
                if f._state in [CANCELLED_AND_NOTIFIED, FINISHED]:
                    yield f