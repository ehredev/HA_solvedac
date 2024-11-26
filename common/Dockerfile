FROM python:3.9-slim

WORKDIR /app

# 의존성 설치
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 애드온 파일 복사
COPY app /app
COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# 서버 실행
CMD ["/app/run.sh"]