# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from .Qt import QtCore

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
