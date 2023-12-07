FROM python:3.9
WORKDIR /app

# Install dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    git \
    build-essential \
    libsndfile1-dev \
    tesseract-ocr \
    espeak-ng python3 \
    python3-pip \
    ffmpeg \
    git-lfs \
    cmake \
    nodejs \
    npm \
    # Remove apt cache again to reduce image size
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/* \
    && rm -rf /usr/share/doc/*

# Copy requirements.txt to the image
COPY requirements.txt* /tmp/requirements.txt

# Update pip and Install dependencies
RUN python -m pip install --no-cache-dir --upgrade -r /tmp/requirements.txt pip


# Tell system to use this venv as default
RUN mkdir -p \
    /entrypoint \
    /app

# Copy entrypoint script into the image
COPY .devcontainer/entrypoint.sh* /entrypoint/entrypoint.sh

# Change permissions to make it executable
RUN chmod +x /entrypoint/entrypoint.sh
RUN chown root:root /entrypoint/entrypoint.sh

# Create a process to check if the app is running
HEALTHCHECK --interval=15s --timeout=15s --start-period=30s \
    CMD curl -X POST -H "Content-Type: application/json" -d '{"message":"healthcheck"}' http://localhost:5000/healthcheck || exit 1

# Start the app
ENTRYPOINT ["/bin/bash", "/entrypoint/entrypoint.sh"]
