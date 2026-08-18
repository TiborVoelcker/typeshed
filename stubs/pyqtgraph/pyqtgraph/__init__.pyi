from _typeshed import Incomplete, StrPath
from typing import Literal, NoReturn
from typing_extensions import TypeAlias

from .colormap import *
from .colors import palette as palette
from .functions import *
from .graphicsItems.ArrowItem import *
from .graphicsItems.AxisItem import *
from .graphicsItems.BarGraphItem import *
from .graphicsItems.ButtonItem import *
from .graphicsItems.ColorBarItem import *
from .graphicsItems.CurvePoint import *
from .graphicsItems.DateAxisItem import *
from .graphicsItems.ErrorBarItem import *
from .graphicsItems.FillBetweenItem import *
from .graphicsItems.GradientEditorItem import *
from .graphicsItems.GradientLegend import *
from .graphicsItems.GraphicsItem import *
from .graphicsItems.GraphicsLayout import *
from .graphicsItems.GraphicsObject import *
from .graphicsItems.GraphicsWidget import *
from .graphicsItems.GraphicsWidgetAnchor import *
from .graphicsItems.GraphItem import *
from .graphicsItems.GridItem import *
from .graphicsItems.HistogramLUTItem import *
from .graphicsItems.ImageItem import *
from .graphicsItems.InfiniteLine import *
from .graphicsItems.IsocurveItem import *
from .graphicsItems.ItemGroup import *
from .graphicsItems.LabelItem import *
from .graphicsItems.LegendItem import *
from .graphicsItems.LinearRegionItem import *
from .graphicsItems.MultiPlotItem import *
from .graphicsItems.PColorMeshItem import *
from .graphicsItems.PlotCurveItem import *
from .graphicsItems.PlotDataItem import *
from .graphicsItems.PlotItem import *
from .graphicsItems.ROI import *
from .graphicsItems.ScaleBar import *
from .graphicsItems.ScatterPlotItem import *
from .graphicsItems.TargetItem import *
from .graphicsItems.TextItem import *
from .graphicsItems.UIGraphicsItem import *
from .graphicsItems.ViewBox import *
from .graphicsItems.VTickGroup import *
from .GraphicsScene import GraphicsScene as GraphicsScene
from .imageview import *
from .metaarray import MetaArray as MetaArray
from .Point import Point as Point
from .Qt import (
    QtCore as QtCore,
    QtGui as QtGui,
    QtWidgets as QtWidgets,
    exec_,
    isQObjectAlive as isQObjectAlive,
    mkQApp as mkQApp,
)
from .SignalProxy import *
from .SRTTransform import SRTTransform as SRTTransform
from .SRTTransform3D import SRTTransform3D as SRTTransform3D
from .ThreadsafeTimer import *
from .Transform3D import Transform3D as Transform3D
from .util.cupy_helper import getCupy as getCupy
from .Vector import Vector as Vector
from .WidgetGroup import *
from .widgets.BusyCursor import *
from .widgets.CheckTable import *
from .widgets.ColorButton import *
from .widgets.ColorMapMenu import ColorMapMenu as ColorMapMenu
from .widgets.ColorMapWidget import *
from .widgets.ComboBox import *
from .widgets.DataFilterWidget import *
from .widgets.DataTreeWidget import *
from .widgets.DiffTreeWidget import *
from .widgets.FeedbackButton import *
from .widgets.FileDialog import *
from .widgets.GradientWidget import *
from .widgets.GraphicsLayoutWidget import *
from .widgets.GraphicsView import *
from .widgets.GroupBox import GroupBox as GroupBox
from .widgets.HistogramLUTWidget import *
from .widgets.JoystickButton import *
from .widgets.LayoutWidget import *
from .widgets.MultiPlotWidget import *
from .widgets.PathButton import *
from .widgets.PlotWidget import *
from .widgets.ProgressDialog import *
from .widgets.RawImageWidget import *
from .widgets.RemoteGraphicsView import RemoteGraphicsView as RemoteGraphicsView
from .widgets.ScatterPlotWidget import *
from .widgets.SpinBox import *
from .widgets.TableWidget import *
from .widgets.TreeWidget import *
from .widgets.ValueLabel import *
from .widgets.VerticalLabel import *

__version__: str
useOpenGL: bool

# The keys accepted by `setConfigOption`/`getConfigOption`; see
# https://pyqtgraph.readthedocs.io/en/latest/api_reference/config_options.html
_ConfigOption: TypeAlias = Literal[
    "useOpenGL",
    "leftButtonPan",
    "foreground",
    "background",
    "antialias",
    "editorCommand",
    "exitCleanup",
    "enableExperimental",
    "crashWarning",
    "mouseRateLimit",
    "imageAxisOrder",
    "useCupy",
    "useNumba",
    "segmentedLineMode",
]

CONFIG_OPTIONS: dict[str, Incomplete]

def setConfigOption(opt: _ConfigOption, value: object) -> None: ...
def setConfigOptions(**opts: object) -> None: ...
def getConfigOption(opt: _ConfigOption): ...
def systemInfo() -> None: ...
def renamePyc(startDir: StrPath) -> None: ...  # undocumented

path: str  # undocumented

def cleanup() -> None: ...  # undocumented

exec = exec_

def exit() -> NoReturn: ...

plots: list[PlotWidget]  # undocumented
images: list[ImageView]  # undocumented
consoles: list[Incomplete]  # undocumented
QAPP: Incomplete  # undocumented

def plot(*args, **kargs) -> PlotWidget: ...
def image(*args, **kargs) -> ImageView: ...

show = image

def dbg(*args, **kwds): ...
def stack(*args, **kwds): ...
def setPalette(app, style: str | Incomplete) -> None: ...  # undocumented
