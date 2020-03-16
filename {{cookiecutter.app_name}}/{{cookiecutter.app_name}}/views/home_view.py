#!/usr/bin/env python3
from flask import render_template, request
from flask_classful import FlaskView
{% if cookiecutter.use_sqlalchemy == 'y' %}from model import db, Visitor
{% endif %}

import requests.exceptions


class HomeView(FlaskView):

    route_base = '/'

    def index(self):

{% if cookiecutter.use_sqlalchemy == 'y' %}
            visitor = Visitor(user_agent=request.headers.get('User-Agent'))
            db.session.add(visitor)
            db.session.commit()

            all_visitor = Visitor.query.all()
{% endif %}

            return render_template('home.html', visitors={%- if cookiecutter.use_sqlalchemy == 'y' -%}all_visitor{%- else -%}[]{%- endif -%})
