FROM ghcr.io/astral-sh/uv:alpine
WORKDIR /app
COPY pyproject.toml /app
COPY .python-version /app
COPY uv.lock /app
RUN uv sync
COPY . /app
EXPOSE 8000
CMD ["/app/.venv/bin/fastapi", "dev", "main.py"]

