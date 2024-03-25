# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Optional, final

from dataclasses_json import DataClassJsonMixin, LetterCase, cfg, dataclass_json

cfg.global_config.encoders[date] = date.isoformat
cfg.global_config.decoders[date] = date.fromisoformat

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Link:
    url: str
    title: Optional[str] = None
    icon: Optional[str] = None
    type: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Metadata:
    # required
    name: str
    provider: str
    namespace: str = 'default'
    # optional
    title: Optional[str] = None
    description: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    links: Optional[List[Link]] = None
    tags: Optional[List[str]] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Spec:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Status:
    pass


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Relation:
    type: str
    target_ref: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Entity(DataClassJsonMixin):
    kind: str
    metadata: Metadata
    spec: Spec = field(default_factory=dict)
    api_version: str = 'developer.microsoft.com/v1'
    status: Optional[Status] = None
    relations: Optional[List[Relation]] = None

    @final
    def ref(self) -> str:
        return f'{self.kind}:{self.metadata.provider}/{self.metadata.namespace}/{self.metadata.name}'.lower()


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EntityPlan:
    kind: str
    namespace: str = 'default'
    labels: Optional[Dict[str, str]] = None


# Environment

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class EnvironmentSpec(Spec):
  type: Optional[str] = None
  resource_id: Optional[str] = None
  subscription: Optional[str] = None
  resource_group: Optional[str] = None
  location: Optional[str] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Environment(Entity):
    spec: EnvironmentSpec


# Operation

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class OperationSpec:
    user: Optional[str] = None
    created_at: Optional[date] = None
    last_updated_at: Optional[date] = None
    state: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Operation(Entity):
    spec: OperationSpec


# kind: Provider

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ProviderSpec:
    version: Optional[str] = None
    kinds: Optional[List[str]] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Provider(Entity):
    spec: ProviderSpec


# kind: Repository

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class RepositorySpec:
  git_url: str
  html_url: Optional[str] = None

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Repository(Entity):
    spec: RepositorySpec


# Template

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TemplateSpec(Spec):
    input_json_schema: str
    input_ui_schema: Optional[str] = None
    creates: Optional[List[EntityPlan]] = None


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Template(Entity):
    spec: TemplateSpec
