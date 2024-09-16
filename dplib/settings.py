# SPDX-FileCopyrightText: 2024 Open Knowledge Foundation
#
# SPDX-License-Identifier: MIT

import os

# Version

VERSION = "1.0.0"

# Profiles

PROFILE_BASEURL = "https://datapackage.org/profiles"
PROFILE_BASEDIR = os.path.join(os.path.dirname(__file__), "profiles")

PROFILE_DEFAULT = "1.0"
PROFILE_DEFAULT_DIALECT = f"{PROFILE_BASEURL}/{PROFILE_DEFAULT}/tabledialect.json"
PROFILE_DEFAULT_SCHEMA = f"{PROFILE_BASEURL}/{PROFILE_DEFAULT}/tableschema.json"
PROFILE_DEFAULT_RESOURCE = f"{PROFILE_BASEURL}/{PROFILE_DEFAULT}/dataresource.json"
PROFILE_DEFAULT_PACKAGE = f"{PROFILE_BASEURL}/{PROFILE_DEFAULT}/datapackage.json"

PROFILE_CURRENT = "2.0"
PROFILE_CURRENT_DIALECT = f"{PROFILE_BASEURL}/{PROFILE_CURRENT}/tabledialect.json"
PROFILE_CURRENT_SCHEMA = f"{PROFILE_BASEURL}/{PROFILE_CURRENT}/tableschema.json"
PROFILE_CURRENT_RESOURCE = f"{PROFILE_BASEURL}/{PROFILE_CURRENT}/dataresource.json"
PROFILE_CURRENT_PACKAGE = f"{PROFILE_BASEURL}/{PROFILE_CURRENT}/datapackage.json"
