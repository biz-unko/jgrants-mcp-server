FROM python:3.10-slim

WORKDIR /app

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY . .

# MCPサーバーを起動
CMD ["python", "-m", "jgrants_mcp_server.core", "--host", "0.0.0.0", "--port", "8000"]
