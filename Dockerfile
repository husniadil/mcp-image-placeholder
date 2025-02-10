FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

COPY . .

RUN uv venv --python 3.12

RUN uv sync --frozen --no-dev --no-editable

FROM python:3.12-slim-bookworm

WORKDIR /app

RUN pip install uv

COPY --from=builder /app /app

CMD ["uv", "--directory", "/app", "run", "main.py"]
