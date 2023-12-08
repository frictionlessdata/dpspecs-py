from __future__ import annotations

from typing import List, Optional

from ...model import Model
from ..contributor import Contributor
from ..license import License
from ..resource import Resource
from ..source import Source


class Package(Model):
    id: Optional[str] = None
    name: Optional[str] = None
    profile: Optional[str] = None
    resources: List[Resource] = []

    title: Optional[str] = None
    description: Optional[str] = None
    homepage: Optional[str] = None
    version: Optional[str] = None
    licenses: List[License] = []
    sources: List[Source] = []
    contributors: List[Contributor] = []
    keywords: List[str] = []
    image: Optional[str] = None
    created: Optional[str] = None