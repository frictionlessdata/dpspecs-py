# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typer import Option

Source = Option(None, "--source", "-s", help="Source notation e.g. ckan")
Target = Option(None, "--target", "-t", help="Target notation e.g. dcat")
