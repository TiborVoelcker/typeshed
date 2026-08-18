# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from _typeshed import Incomplete, StrPath
from typing import ClassVar

from ..Qt import QtWidgets
from .Exporter import Exporter

__all__ = ["MatplotlibExporter"]

class MatplotlibExporter(Exporter):
    Name: ClassVar[str]
    windows: ClassVar[list[MatplotlibWindow]]
    def __init__(self, item) -> None: ...
    def parameters(self) -> None: ...
    def cleanAxes(self, axl) -> None: ...
    def export(self, fileName: StrPath | None = None) -> None: ...  # type: ignore[override]

class MatplotlibWindow(QtWidgets.QMainWindow):
    mpl: Incomplete
    def __init__(self) -> None: ...
    def __getattr__(self, attr: str): ...
    def closeEvent(self, ev) -> None: ...
