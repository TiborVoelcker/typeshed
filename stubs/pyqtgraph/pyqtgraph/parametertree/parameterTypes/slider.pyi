from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np
from numpy.typing import NDArray

from ...Qt import QtWidgets
from ..Parameter import Parameter
from .basetypes import Emitter, WidgetParameterItem

class SliderParameterItem(WidgetParameterItem):
    slider: QtWidgets.QSlider
    span: NDArray[Any]
    charSpan: np.char.chararray[Any, np.dtype[np.bytes_]]
    emitter: Emitter
    sigChanging: Any
    def __init__(self, param: Parameter, depth: int) -> None: ...
    def updateDisplayLabel(self, value=None) -> None: ...
    def setSuffix(self, suffix: str | None) -> None: ...
    # Returns a QWidget holding a QLabel and the QSlider.
    def makeWidget(self): ...
    def spanToSliderValue(self, v: float) -> int: ...
    def prettyTextValue(self, v: int) -> str: ...
    def optsChanged(self, param: Parameter, opts: Mapping[str, Any]) -> None: ...
    def limitsChanged(self, param: Parameter, limits: Sequence[float]) -> None: ...

class SliderParameter(Parameter):
    # `**opts` adds "limits" ([start, stop]), "step", "span", "format" and "precision" to the
    # standard Parameter options.
    itemClass: type[SliderParameterItem]
