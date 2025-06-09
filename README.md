# Document Ingestion & Classification

An AI-powered multi-agent system to automatically ingest, extract, classify, and route enterprise documents using Gen AI and modular architecture.

## 🧠 Features
- Modular agents (Ingestor, Extractor, Classifier, Router)
- Gen AI for OCR cleanup, entity extraction, classification
- Event-driven architecture with message bus
- Web-based dashboard for real-time tracking and manual overrides

## 📁 Folder Structure
- `ingestor-agent/` – Handles document uploads and email ingestion
- `extractor-agent/` – Applies OCR and extracts structured entities using LLMs
- `classifier-agent/` – Classifies documents using Gen AI / ML models
- `router-agent/` – Routes documents to ERP, DMS, or alert systems
- `frontend-dashboard/` – ReactJS UI for tracking and manual overrides
- `configs/` – YAML/config files
- `infra/` – Docker/K8s setup
- `docs/` – Design documents, diagrams
