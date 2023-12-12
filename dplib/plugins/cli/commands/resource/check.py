from dplib.actions.resource.check import check_resource

from ...helpers.check import print_check_results
from ...options.path import path_arg
from .main import program


@program.command(name="check")
def command(
    path: str = path_arg,
):
    errors = check_resource(path)
    print_check_results(path, errors)