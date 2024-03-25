# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import logging

import azure.functions as func

from api.create_entities import bp as create_entities
from api.get_entities import bp as get_entities
from api.version import bp as get_version

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

app.register_functions(get_entities)
app.register_functions(create_entities)
app.register_functions(get_version)
