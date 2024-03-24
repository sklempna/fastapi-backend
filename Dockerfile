# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages
# RUN python -m pip install --upgrade pip
RUN pip install poetry

COPY ./poetry.lock .
COPY ./pyproject.toml .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Define environment variable
ENV PORT=8000
ENV TENANT_ID=my-tenant-id
ENV CLIENT_ID=my-client-id
ENV CLIENT_CREDENTIALS=my-client-secret

# Run app.py when the container launches
CMD poetry run uvicorn main:app --host 0.0.0.0 --port $PORT