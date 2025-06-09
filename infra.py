
# Docker Compose setup (simplified)
version: '3'
services:
  ingestor:
    build: ./ingestor-agent
    ports:
      - "8001:8000"
  extractor:
    build: ./extractor-agent
    ports:
      - "8002:8000"
