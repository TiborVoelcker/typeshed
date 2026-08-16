from ..Parameter import Parameter
from .basetypes import WidgetParameterItem

class ProgressBarParameterItem(WidgetParameterItem):
    hideWidget: bool
    # Returns a QProgressBar.
    def makeWidget(self): ...

class ProgressBarParameter(Parameter):
    itemClass: type[ProgressBarParameterItem]
