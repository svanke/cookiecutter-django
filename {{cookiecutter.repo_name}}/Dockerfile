FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Install requirement to compile messages
RUN apt-get update && apt-get install -y gettext libgettextpo-dev

# Creating working directory
RUN mkdir /code
WORKDIR /code

# Copying requirements
COPY ./{{cookiecutter.project_slug}}/requirements/local.txt .
RUN pip install -r ./{{cookiecutter.project_name}}/requirements/local.txt

# Copying manage.py file
COPY ./{{cookiecutter.project_name}}/manage.py .

# Copying source
COPY {{cookiecutter.project_name}} ./{{cookiecutter.project_name}}

# Compile messages for translation
RUN python ./{{cookiecutter.project_name}}/manage.py compilemessages