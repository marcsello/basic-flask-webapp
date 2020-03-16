FROM python:3

ADD {{cookiecutter.app_name}} requirements.txt /{{cookiecutter.app_name}}/
WORKDIR /{{cookiecutter.app_name}}/

RUN pip3 install -r requirements.txt && pip3 install gunicorn

EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

