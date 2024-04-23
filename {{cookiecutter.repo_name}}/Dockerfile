# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install postgres client
RUN apk add --update --no-cache postgresql-client jpeg-dev

# Install individual dependencies to avoid x-tra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev \
        zlib zlib-dev
# Set the working directory in the container
WORKDIR /code

# Install system dependencies
RUN apk add --no-cache \
        nodejs \
        npm \
        yarn

# Copy the Django project files into the container
COPY . /code/

# Install Python dependencies
COPY requirements /code/requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements/local.txt

# Remove dependencies
RUN apk del .tmp-build-deps

# Install Node.js dependencies
RUN cd src && npm install

# Determine the path to npm binaries
RUN NPM_BIN_PATH=$(which npm) \
    && echo "export NPM_BIN_PATH=$NPM_BIN_PATH" >> /etc/profile.d/npm_path.sh \
    && chmod +x /etc/profile.d/npm_path.sh

# Initialize Tailwind CSS <-- uncomment these when creating new project
RUN cd src && echo -e "\n" | python manage.py tailwind init

# Uncomment 'theme' app in Django settings <-- uncomment these when creating new project
RUN cd src && sed -i 's/^# \(.*theme.*\)/\1/' config/settings/base.py

# Install Tailwind CSS dependencies
RUN npm install tailwindcss@latest postcss@latest autoprefixer@latest

# Run `python manage.py tailwind start`
CMD ["python", "manage.py", "tailwind", "start"]

# [Security] Limit the scope of user who run the docker image
RUN adduser -D user

# Run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]

USER user
