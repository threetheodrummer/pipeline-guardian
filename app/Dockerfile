FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM gcr.io/distroless/python3-debian12

WORKDIR /app
COPY --from=builder /install /usr/local
COPY src/ .

CMD ["-m", "http.server", "8080"]
