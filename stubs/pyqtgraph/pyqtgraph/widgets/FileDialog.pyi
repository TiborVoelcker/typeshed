# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from ..Qt import QtWidgets

__all__ = ["FileDialog"]

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args) -> None: ...
