# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import logging

import azure.functions as func

provider_id = 'python.provider'

bp = func.Blueprint()

@bp.function_name("ExecuteTemplate")
@bp.route(route="entities/template/{namespace}/{name}", methods=[func.HttpMethod.POST], auth_level=func.AuthLevel.ANONYMOUS)
def execute_template(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    namespace = req.route_params.get('namespace').lower()
    name = req.route_params.get('name').lower()

    ref = f'template:{provider_id}/{namespace}/{name}'

    return func.HttpResponse(f"Ref = {ref}")