# See https://docs.astral.sh/uv/guides/integration/docker/
# See also https://github.com/astral-sh/uv-docker-example/tree/main

# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Expose Zensical development server port
EXPOSE 8000

# Run the Zensical dev server via uv
# Uses `zensical serve` to run the dev server
# Uses `--dev-addr=0.0.0.0:8000` to allow access from outside the container
ENTRYPOINT ["uv", "run", "zensical"]
CMD ["serve", "--dev-addr=0.0.0.0:8000"]
