from _typeshed import Incomplete

from . import QtCore as QtCore, QtGui as QtGui, QtWidgets as QtWidgets

PYSIDE: str
PYSIDE2: str
PYSIDE6: str
PYQT4: str
PYQT5: str
PYQT6: str

QT_LIB: str
QtVersion: str
VERSION_INFO: str
# Set by `mkQApp`; `QAPP` is the older spelling kept for backwards compatibility.
App: Incomplete
QAPP: Incomplete

class FailedImport:  # undocumented
    err: BaseException
    def __init__(self, err: BaseException) -> None: ...
    def __getattr__(self, attr: str): ...

def exec_(): ...
def mkQApp(name: str | None = None): ...
def isQObjectAlive(obj) -> bool: ...

# The remaining names are injected at import time and are not importable
# submodules: `QtSvg`, `QtTest`, `QtOpenGLWidgets`, `loadUiType`, `sip`, ...
# See the note in `QtCore/__init__.pyi`.
def __getattr__(name: str): ...  # incomplete module
