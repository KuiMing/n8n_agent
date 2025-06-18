FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    xvfb \
    wget \
    curl \
    fonts-liberation \
    libnss3 \
    libatk-bridge2.0-0 \
    libxss1 \
    libasound2 \
    libxshmfence-dev \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*


# install playwright
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps


COPY . /app
WORKDIR /app

# API Service
CMD xvfb-run --auto-servernum --server-args='-screen 0 1280x720x24' \
    uvicorn playwright_api:app --host 0.0.0.0 --port 8020
