from _typeshed import Incomplete

from .Qt import QtCore  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

__all__ = ["ThreadsafeTimer"]

class ThreadsafeTimer(QtCore.QObject):
    timeout: Incomplete
    sigTimerStopRequested: Incomplete
    sigTimerStartRequested: Incomplete
    timer: Incomplete
    def __init__(self) -> None: ...
    def start(self, timeout) -> None: ...
    def stop(self) -> None: ...
    def timerFinished(self) -> None: ...
