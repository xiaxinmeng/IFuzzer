
class DoneAndNotDoneFutures(Sequence[set[Future[_T]]]):
    @property
    def done(self) -> set[Future[_T]]: ...
    @property
    def not_done(self) -> set[Future[_T]]: ...
    def __new__(_cls, done: set[Future[_T]], not_done: set[Future[_T]]) -> DoneAndNotDoneFutures[_T]: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, __i: SupportsIndex) -> set[Future[_T]]: ...
    @overload
    def __getitem__(self, __s: slice) -> DoneAndNotDoneFutures[_T]: ...