# Base image with Python 3.12 + CUDA + dev tools
FROM mcr.microsoft.com/devcontainers/python:3.12-cuda

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    gcc \
    make \
    pciutils \
    curl \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Optional: Set a working directory
WORKDIR /workspace

# Copy project files
COPY requirements.txt ./requirements.txt

# Install Python dependencies globally
RUN pip install --upgrade pip && pip install -r requirements.txt

# Optional: install whisper (editable install)
RUN pip install git+https://github.com/openai/whisper.git

# Optional: Add a non-root user (only if needed)
# RUN useradd -m -s /bin/bash devuser
# USER devuser
