from typing import Optional

from ...model import Model
from ..metadata.convert import INotation, convert_metadata


def convert_resource(
    path: str,
    *,
    format: Optional[str] = None,
    source: Optional[INotation] = None,
    target: Optional[INotation] = None,
) -> Model:
    return convert_metadata(
        path, type="resource", format=format, source=source, target=target
    )
