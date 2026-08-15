# Qt base classes come from `pyqtgraph.Qt`, which typeshed cannot resolve; see README.md.
# pyright: reportUntypedBaseClass=false

from ..Qt import QtWidgets  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

__all__ = ["FileDialog"]

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args) -> None: ...
