
class DoneAndNotDoneFutures(NamedTuple, Generic[_T]):
    done: set[Future[_T]]
    not_done: set[Future[_T]]
