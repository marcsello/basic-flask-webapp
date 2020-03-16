#!/usr/bin/env python3
from flask import request, abort, jsonify
from flask_classful import FlaskView
from utils import json_required, apikey_required
{% if cookiecutter.use_sqlalchemy == 'y' %}
from model import db
{%endif%}

class HelloView(FlaskView):

    decorators = [apikey_required]

    def index(self):
        return jsonify({"hello" : "world"})

    @json_required
    def post(self):
        return jsonify({"hello" : "world"})

