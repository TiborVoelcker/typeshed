from _typeshed import Incomplete
from typing import Any

from numpy.typing import NDArray
from OpenGL.GL import *  # type: ignore[import-not-found, import-untyped]  # pyright: ignore[reportMissingImports]

from ...functions import _ColorArg
from ..GLGraphicsItem import GLGraphicsItem
from ..shaders import ShaderProgram

__all__ = ["GLMeshItem"]

class GLMeshItem(GLGraphicsItem):
    # Keys: 'meshdata', 'color', 'drawEdges', 'drawFaces', 'edgeColor', 'shader',
    # 'smooth', 'computeNormals'.
    opts: dict[str, Incomplete]
    vertexes: NDArray[Any] | None
    normals: NDArray[Any] | None
    colors: NDArray[Any] | None
    faces: NDArray[Any] | None
    # Takes the `setMeshData()` keys plus 'shader' and 'glOptions'.
    def __init__(self, parentItem: GLGraphicsItem | None = None, **kwds) -> None: ...
    def setShader(self, shader: str | ShaderProgram | None) -> None: ...
    def shader(self) -> ShaderProgram: ...
    def setColor(self, c: _ColorArg) -> None: ...
    # Either a `meshdata` MeshData instance, or keyword arguments for `MeshData()`
    # ('vertexes', 'faces', 'edges', 'vertexColors', 'faceColors'), plus any of the
    # `opts` keys.
    def setMeshData(self, **kwds) -> None: ...
    edges: NDArray[Any] | None
    edgeColors: NDArray[Any] | None
    def meshDataChanged(self) -> None: ...
    edgeVerts: NDArray[Any] | None
    def parseMeshData(self) -> None: ...
    def paint(self) -> None: ...
