from __future__ import annotations

from typing import Optional

from ...helpers.resource import path_to_name
from ...model import Model
from ...models import Resource


class CkanResource(Model):
    name: str
    created: Optional[str] = None
    description: Optional[str] = None
    format: Optional[str] = None  # NOTE: uppercased
    hash: Optional[str] = None
    id: Optional[str] = None
    last_modified: Optional[str] = None
    metadata_modified: Optional[str] = None
    mimetype: Optional[str] = None
    size: Optional[int] = None

    # Mappers

    def to_dp(self) -> Resource:
        resource = Resource(path=self.name, name=path_to_name(self.name))

        # General
        if self.id:
            resource.custom["ckan:id"] = self.id
        if self.format:
            resource.format = self.format.lower()
        if self.mimetype:
            resource.mediatype = self.mimetype
        if self.size:
            resource.bytes = self.size

        return resource

    @classmethod
    def from_dp(cls, resource: Resource) -> Optional[CkanResource]:
        if not resource.path:
            return
        ckan = CkanResource(name=resource.path)

        # General
        if resource.format:
            ckan.format = resource.format.upper()
        if resource.mediatype:
            ckan.mimetype = resource.mediatype
        if resource.bytes:
            ckan.size = resource.bytes

        return ckan
