FROM python:3.12-slim

# 安裝 Playwright 及其瀏覽器
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN playwright install --with-deps

# 複製專案檔案
COPY . /app
WORKDIR /app

# 啟動 FastAPI 服務
CMD ["uvicorn", "playwright_api:app", "--host", "0.0.0.0", "--port", "8020"] 