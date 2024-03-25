# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from entities import Metadata, Provider, ProviderSpec, Repository, RepositorySpec, Template, TemplateSpec


def get_provider() -> Provider:
    return Provider(
        kind='provider',
        metadata=Metadata(
            name='PythonProvider',
            provider='python.provider',
            namespace='default',
            title='Python Provider',
            description='Example provider implementation in python'
        ),
        spec=ProviderSpec(
            version='v0.0.0',
            kinds=['Provider', 'Operation', 'Template', 'Repository']
        ),
    )

def get_template(name: str = 'python-template'):
    return Template(
        kind='template',
        metadata=Metadata(
            name=name,
            provider='python.provider',
            namespace='sample',
            title='Python Template',
            description='Example template entity'
        ),
        spec=TemplateSpec(
            input_json_schema='{\"type\":\"object\",\"properties\":{}}'
        ),
    )


def get_repository(name: str = 'python-repository'):
    return Repository(
        kind='repository',
        metadata=Metadata(
            name=name,
            provider='python.provider',
            namespace='sample',
            title='Python Repo',
            description='Example repository entity.'
        ),
        spec=RepositorySpec(
            git_url='git://github.com/microsoft/developer-platform.git',
            html_url='https://github.com/microsoft/developer-platform'
        ),
    )