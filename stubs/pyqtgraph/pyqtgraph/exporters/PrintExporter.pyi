from _typeshed import StrPath
from typing import ClassVar

from ..parametertree import Parameter
from .Exporter import Exporter

__all__ = ["PrintExporter"]

class PrintExporter(Exporter):
    Name: ClassVar[str]
    params: Parameter
    def __init__(self, item) -> None: ...
    def widthChanged(self) -> None: ...
    def heightChanged(self) -> None: ...
    def parameters(self) -> Parameter: ...
    def export(self, fileName: StrPath | None = None) -> None: ...  # type: ignore[override]
