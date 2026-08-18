# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from .functions import SignalBlock
from .Qt import QtCore

__all__ = ["SignalProxy"]

class SignalProxy(QtCore.QObject):
    sigDelayed: Incomplete
    delay: float
    rateLimit: float
    args: tuple[Incomplete, ...] | None
    timer: Incomplete
    lastFlushTime: float | None
    signal: Incomplete
    blockSignal: bool
    slot: Incomplete
    def __init__(self, signal, delay: float = 0.3, rateLimit: int = 0, slot=None, *, threadSafe: bool = True) -> None: ...
    def setDelay(self, delay: float) -> None: ...
    def signalReceived(self, *args) -> None: ...
    def flush(self) -> bool: ...
    def disconnect(self) -> None: ...
    def connectSlot(self, slot) -> None: ...
    def block(self) -> SignalBlock: ...
