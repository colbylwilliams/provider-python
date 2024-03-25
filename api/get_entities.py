# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import json
import logging

import azure.functions as func

from entities import Provider, Repository, Template
from sample_entities import get_provider, get_repository, get_template

bp = func.Blueprint()

@bp.function_name("GetEntities")
@bp.route(route="entities", methods=[func.HttpMethod.GET], auth_level=func.AuthLevel.ANONYMOUS)
def get_entities(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    entities = [
        get_provider().to_dict(),
        get_repository().to_dict(),
        get_template().to_dict()
    ]

    return func.HttpResponse(json.dumps(entities, indent=4))


@bp.function_name("GetEntitiesByKind")
@bp.route(route="entities/{kind}", methods=[func.HttpMethod.GET], auth_level=func.AuthLevel.ANONYMOUS)
def get_entities_by_kind(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    kind = req.route_params.get('kind').lower()

    if kind == 'provider':
        return func.HttpResponse(Provider.schema().dumps([get_provider()], many=True))
    elif kind == 'repository':
        return func.HttpResponse(Repository.schema().dumps([get_repository()], many=True))
    elif kind == 'template':
        return func.HttpResponse(Template.schema().dumps([get_template()], many=True))

    return func.HttpResponse([])


@bp.function_name("GetEntity")
@bp.route(route="entities/{kind}/{namespace}/{name}", methods=[func.HttpMethod.GET], auth_level=func.AuthLevel.ANONYMOUS)
def get_entity(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    kind = req.route_params.get('kind').lower()
    namespace = req.route_params.get('namespace').lower()
    name = req.route_params.get('name').lower()

    if kind == 'provider' and (provider := get_provider()) \
        and provider.metadata.namespace == namespace and provider.metadata.name == name:
        return func.HttpResponse(provider.to_json(indent=4))

    if kind == 'repository' and (repository := get_repository()) \
        and repository.metadata.namespace == namespace and repository.metadata.name == name:
        return func.HttpResponse(repository.to_json(indent=4))

    if kind == 'template' and (template := get_template()) \
        and template.metadata.namespace == namespace and template.metadata.name == name:
        return func.HttpResponse(template.to_json(indent=4))

    return func.HttpResponse(status_code=404)

