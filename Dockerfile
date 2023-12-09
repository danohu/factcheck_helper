# Use an official Python runtime as a parent image
FROM python:3.8-slim


# Set the working directory in the container
WORKDIR /app

COPY pyproject.toml /app/pyproject.toml

# Install poetry
RUN pip install -e .


# Copy the pyproject.toml and poetry.lock files to the working directory
COPY ./ /app

## Configure poetry to install packages into system
#RUN poetry config virtualenvs.create false
#
## Install dependencies using poetry
## Note:e If you don't have a poetry.lock file, you can remove `--no-dev`
#RUN poetry install --no-dev

# Copy the content of the local src directory to the working directory

# Command to run on container start
CMD ["uvicorn", "factcheck_helper:app", "--host", "0.0.0.0", "--port", "8080"]
