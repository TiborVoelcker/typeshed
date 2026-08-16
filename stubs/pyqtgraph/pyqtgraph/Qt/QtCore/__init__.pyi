# `pyqtgraph.Qt` re-exports whichever of PyQt5/PyQt6/PySide2/PySide6 is installed.
# typeshed cannot depend on a Qt binding, so the contents are left untyped.
def __getattr__(name: str): ...  # incomplete module
