from _typeshed import StrPath

from ..Parameter import Parameter
from .str import StrParameterItem

# `**kwargs` takes any QFileDialog enum setter name and its value as a string or list of strings,
# e.g. fileMode="AnyFile", options=["ShowDirsOnly", "DontResolveSymlinks"], acceptMode="AcceptSave".
def popupFilePicker(
    parent=None,
    windowTitle: str = "",
    nameFilter: str = "",
    directory: StrPath | None = None,
    selectFile: StrPath | None = None,
    relativeTo: StrPath | None = None,
    **kwargs,
) -> str | list[str] | None: ...

class FileParameterItem(StrParameterItem):
    def __init__(self, param: Parameter, depth: int) -> None: ...
    # Returns a QLineEdit.
    def makeWidget(self): ...
    def setValue(self, value) -> None: ...
    def value(self) -> str | list[str] | None: ...
    def updateDefaultBtn(self) -> None: ...
    def updateDisplayLabel(self, value=None) -> None: ...

class FileParameter(Parameter):
    itemClass: type[FileParameterItem]
    # `**opts` adds the `popupFilePicker` options -- parent, winTitle, nameFilter, directory,
    # selectFile, relativeTo and any QFileDialog enum -- to the standard Parameter options.
    def __init__(self, **opts) -> None: ...
