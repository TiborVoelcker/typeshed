from ..Qt import QtWidgets  # type: ignore[import-not-found]  # pyright: ignore[reportMissingImports]

__all__ = ["FileDialog"]

class FileDialog(QtWidgets.QFileDialog):
    def __init__(self, *args) -> None: ...
