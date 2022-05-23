import logging
from argparse import ArgumentParser
{% if cookiecutter.yaml -%}
from pathlib import Path
{%- endif %}

{% if cookiecutter.httpx -%}
from httpx import Client
{%- endif %}
{% if cookiecutter.sqlalchemy -%}
from sqlalchemy import create_engine, text
{%- endif %}
{% if cookiecutter.yaml -%}
import yaml
{%- endif %}


def add(aaa: int, bbb: int) -> int:
    return aaa + bbb


def logging_config(verbose: int):
    logging.basicConfig(
        level=[logging.WARNING, logging.INFO, logging.DEBUG][min(verbose, 2)],
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
    )
    logging.getLogger('parso').setLevel(level=[logging.WARNING, logging.INFO][min(verbose, 1)])
    {% if cookiecutter.sqlalchemy -%}
    logging.getLogger('sqlalchemy').setLevel(level=[logging.WARNING, logging.INFO][min(verbose, 1)])
    {%- endif %}


def main():
    parser = ArgumentParser()
    parser.add_argument('-V', '--version', action='version', version='0.1.0')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    {% if cookiecutter.httpx -%}
    parser.add_argument('base_url')
    {%- endif %}
    {% if cookiecutter.sqlalchemy -%}
    parser.add_argument('engine', helm='database url')
    {%- endif %}
    {% if cookiecutter.yaml -%}
    parser.add_argument('path', type=Path)
    {%- endif %}

    args = parser.parse_args()

    logging_config(args.verbose)

    {% if cookiecutter.sqlalchemy -%}
    engine = create_engine(args.engine, future=True)
    with engine.connect() as conn:
        conn.execute(text('SELECT 1'))
    {%- endif %}

    {% if cookiecutter.yaml -%}
    with args.path.open(encoding='utf-8') as f:
        print(yaml.safe_load(f))
    {%- endif %}

    {% if cookiecutter.httpx -%}
    with Client(base_url=args.base_url) as client:
        print(client.get('').text)
    {%- endif %}

    return 0
