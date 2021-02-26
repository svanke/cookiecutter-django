# Pull official base image
FROM python:3.8-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install postgres client
RUN apk add --update --no-cache postgresql-client jpeg-dev

# Install individual dependencies to avoid x-tra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev \
        zlib zlib-dev

# Copying and installing dependencies requirements
COPY ./requirements ./requirements
RUN pip install --upgrade pip
RUN pip install -r ./requirements/local.txt

# Remove dependencies
RUN apk del .tmp-build-deps

# Creating working directory
RUN mkdir /code
WORKDIR /code

# Copy entrypoint.sh
COPY ./src/entrypoint.sh /code

# Adds our application code to the image
COPY ./src /code

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

# Run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

USER user

