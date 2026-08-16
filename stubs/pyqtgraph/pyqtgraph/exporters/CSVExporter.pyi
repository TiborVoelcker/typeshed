import itertools
from _typeshed import Incomplete, StrPath
from typing import ClassVar

from ..parametertree import Parameter
from .Exporter import Exporter

__all__ = ["CSVExporter"]

class CSVExporter(Exporter):
    Name: ClassVar[str]
    windows: ClassVar[list[Incomplete]]
    params: Parameter
    index_counter: itertools.count[int]
    header: list[str]
    data: list[tuple[Incomplete, ...]]
    def __init__(self, item) -> None: ...
    def parameters(self) -> Parameter: ...
    def export(self, fileName: StrPath | None = None) -> None: ...  # type: ignore[override]
