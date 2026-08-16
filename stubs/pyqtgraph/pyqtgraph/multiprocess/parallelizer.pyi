from _typeshed import Incomplete
from collections.abc import Iterator, Sequence

class CanceledError(Exception): ...

class Parallelize:
    showProgress: bool
    progressDlg: Incomplete
    workers: int
    tasks: Sequence[Incomplete]
    reseed: bool
    kwds: dict[str, Incomplete]
    def __init__(
        self,
        tasks: Sequence[Incomplete] | None = None,
        workers: int | None = None,
        block: bool = True,
        progressDialog=None,
        randomReseed: bool = True,
        **kwds,
    ) -> None: ...
    proc: Incomplete
    def __enter__(self) -> Tasker: ...
    def __exit__(self, *exc_info: object) -> None: ...
    progress: Incomplete
    def runSerial(self) -> Tasker: ...
    childs: list[Incomplete]
    exitCodes: list[int]
    def runParallel(self) -> Tasker: ...
    @staticmethod
    def suggestedWorkerCount() -> int: ...

class Tasker:
    proc: Incomplete
    par: Parallelize
    tasks: Sequence[Incomplete]
    def __init__(self, parallelizer: Parallelize, process, tasks: Sequence[Incomplete], kwds) -> None: ...
    index: int
    def __iter__(self) -> Iterator[Incomplete]: ...
    def process(self) -> None: ...
    def numWorkers(self) -> int: ...
