FROM python:3.10-bookworm

# Create application directory
WORKDIR /app

RUN pip install poetry

ADD pyproject.toml .
ADD poetry.lock .

RUN poetry install --no-dev --no-root --remove-untracked

# Install and run the program
ENTRYPOINT python3 -m python-template