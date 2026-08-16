# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

import types
from _typeshed import Incomplete
from typing import ClassVar
from typing_extensions import Self

from ..Qt import QtWidgets

__all__ = ["ProgressDialog"]

class ProgressDialog(QtWidgets.QProgressDialog):
    allDialogs: ClassVar[list[ProgressDialog]]
    nestedLayout: Incomplete
    nested: bool
    disabled: bool
    busyCursor: bool
    def __init__(
        self,
        labelText: str,
        minimum: int = 0,
        maximum: int = 100,
        cancelText: str | None = "Cancel",
        parent=None,
        wait: int = 250,
        busyCursor: bool = False,
        disable: bool = False,
        nested: bool = False,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exType: type[BaseException] | None, exValue: BaseException | None, exTrace: types.TracebackType | None
    ) -> None: ...
    def __iadd__(self, val: int) -> Self: ...
    def resizeEvent(self, ev) -> None: ...
    def setValue(self, val: int) -> None: ...
    def setLabelText(self, val: str) -> None: ...
    def setMaximum(self, val: int) -> None: ...
    def setMinimum(self, val: int) -> None: ...
    def wasCanceled(self) -> bool: ...
    def maximum(self) -> int: ...
    def minimum(self) -> int: ...

class ProgressWidget(QtWidgets.QWidget):
    hidden: bool
    layout: Incomplete
    label: Incomplete
    bar: Incomplete
    def __init__(self, label, bar) -> None: ...
    def eventFilter(self, obj, ev) -> bool: ...
    def hide(self) -> None: ...
