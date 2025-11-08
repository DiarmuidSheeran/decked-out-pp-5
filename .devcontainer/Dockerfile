FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Install Python 3 and required dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    postgresql-client \
    libpq-dev \
    build-essential \
    && ln -sf /usr/bin/python3 /usr/bin/python \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python -m pip install --upgrade pip --break-system-packages
