#!/usr/bin/env python3
from .require_decorators import json_required{%- if cookiecutter.generate_api_view == 'y' -%}, apikey_required{% endif %}
from .error_handlers import register_all_error_handlers
