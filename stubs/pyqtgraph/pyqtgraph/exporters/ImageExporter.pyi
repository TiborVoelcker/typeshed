from _typeshed import Incomplete, StrPath
from typing import ClassVar

from ..parametertree import Parameter
from .Exporter import Exporter

__all__ = ["ImageExporter"]

class ImageExporter(Exporter):
    Name: ClassVar[str]
    allowCopy: bool
    params: Parameter
    def __init__(self, item) -> None: ...
    def widthChanged(self) -> None: ...
    def heightChanged(self) -> None: ...
    def parameters(self) -> Parameter: ...
    @staticmethod
    def getSupportedImageFormats() -> list[str]: ...
    png: Incomplete
    # Returns a `QImage` when *toBytes* is set, the result of `QImage.save()` when
    # writing to a file, and None otherwise.
    def export(self, fileName: StrPath | None = None, toBytes: bool = False, copy: bool = False): ...
