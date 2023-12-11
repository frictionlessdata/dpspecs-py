from typing import List, Union

from ... import types
from ...errors.metadata import MetadataError
from ...helpers.data import read_data
from ...helpers.path import infer_basepath
from ..metadata.check import check_metadata


def check_package(package: Union[str, types.IDict]) -> List[MetadataError]:
    basepath = None
    if isinstance(package, str):
        basepath = infer_basepath(package)
        package = read_data(package)

    # Dereference resources[].dialect/schema
    resources = package.get("resources", [])
    if isinstance(resources, list):
        for resource in resources:  # type: ignore
            for name in ["dialect", "schema"]:
                value = resource.get(name)  # type: ignore
                if value and isinstance(value, str):
                    resource[name] = read_data(value, basepath=basepath)

    return check_metadata(package, profile_name="data-package")
