#!/usr/bin/env python3
import shutil
import os

remove_api_views = '{{cookiecutter.generate_api_view}}' == 'n'
remove_models = '{{cookiecutter.use_sqlalchemy}}' == 'n'

if remove_api_views:
	shutil.rmtree("{{cookiecutter.app_name}}/api_views")

if remove_models:
   	shutil.rmtree("{{cookiecutter.app_name}}/model")


os.system('python3 -m venv venv')
os.system('venv/bin/pip3 install -r requirements.txt')
