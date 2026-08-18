# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete
from typing import Literal
from typing_extensions import TypeAlias

from ..Qt import QtWidgets

__all__ = ["VerticalLabel"]

# Any value other than `"vertical"` is drawn horizontally.
_Orientation: TypeAlias = Literal["vertical", "horizontal"]

class VerticalLabel(QtWidgets.QLabel):
    forceWidth: bool
    orientation: _Orientation
    def __init__(self, text: str, orientation: _Orientation = "vertical", forceWidth: bool = True) -> None: ...
    def setOrientation(self, o: _Orientation) -> None: ...
    hint: Incomplete  # the QRect the text was last drawn into
    def paintEvent(self, ev) -> None: ...
    def sizeHint(self): ...
