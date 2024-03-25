# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import logging
import os

import azure.functions as func

bp = func.Blueprint()

@bp.function_name("Version")
@bp.route(route="version", methods=[func.HttpMethod.GET], auth_level=func.AuthLevel.ANONYMOUS)
def get_version(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    version = os.getenv('DEVELOPER_PLATFORM_IMAGE_VERSION', 'debug')

    return func.HttpResponse(version)