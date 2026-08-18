# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete

from ..parametertree.parameterTypes.pen import PenParameter
from ..Qt import QtWidgets

class PenPreviewLabel(QtWidgets.QLabel):
    param: PenParameter
    pen: Incomplete  # QPen
    def __init__(self, param: PenParameter) -> None: ...
    def onPenChanging(self, param: PenParameter, val) -> None: ...
    def paintEvent(self, ev) -> None: ...
