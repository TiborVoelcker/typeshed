# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from .Qt import QtCore  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["SignalProxy"]

class SignalProxy(QtCore.QObject):
    sigDelayed: Incomplete
    delay: Incomplete
    rateLimit: Incomplete
    args: Incomplete
    timer: Incomplete
    lastFlushTime: Incomplete
    signal: Incomplete
    blockSignal: bool
    slot: Incomplete
    def __init__(self, signal, delay: float = 0.3, rateLimit: int = 0, slot=None, *, threadSafe: bool = True) -> None: ...
    def setDelay(self, delay) -> None: ...
    def signalReceived(self, *args) -> None: ...
    def flush(self): ...
    def disconnect(self) -> None: ...
    def connectSlot(self, slot) -> None: ...
    def block(self): ...
