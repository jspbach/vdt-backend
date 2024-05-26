# Use Python 3.11 image
FROM python:3.11-bookworm

# Removes buffering for more efficient logging
ENV PYTHONUNBUFFERED 1

# Set up the working directory in the container and copy its current directory

RUN pip install poetry
RUN poetry config virtualenvs.create false

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . $APP_HOME

# Install packages from poetry.lock
RUN poetry install --only main

# Run application
CMD ["/bin/bash", "./deployment/entrypoint.sh"]

