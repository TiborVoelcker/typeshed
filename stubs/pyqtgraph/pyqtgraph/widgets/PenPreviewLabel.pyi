from _typeshed import Incomplete

from ..Qt import QtWidgets  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

class PenPreviewLabel(QtWidgets.QLabel):
    param: Incomplete
    pen: Incomplete
    def __init__(self, param) -> None: ...
    def onPenChanging(self, param, val) -> None: ...
    def paintEvent(self, ev) -> None: ...
