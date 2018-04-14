FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Install requirement to compile messages


# Creating working directory
RUN mkdir /code
WORKDIR /code

# Copying requirements
COPY ./requirements ./requirements
RUN pip install -r ./requirements/base.txt

# Adds our application code to the image
COPY . code
WORKDIR code

