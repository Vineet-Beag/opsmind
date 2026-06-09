# OpsMind

OpsMind is an AI-powered Infrastructure Provisioning Platform that converts natural language requests into production-ready Terraform code.

## Overview

OpsMind helps DevOps, SRE, and Platform Engineering teams provision infrastructure using AI.

Example:

Input:

```text
Create an OCI VM with 2 CPUs and 16GB RAM
```

Output:

```text
Terraform configuration for Oracle Cloud Infrastructure (OCI)
```

---

## Architecture

```text
User
  ↓
FastAPI
  ↓
AI Gateway
  ↓
Terraform Agent
  ↓
Gemini
  ↓
Terraform Output
```

---

## Features

- Natural Language → Terraform
- FastAPI REST API
- AI Gateway Architecture
- Terraform Agent
- Gemini Integration
- OCI Infrastructure Generation

---

## Project Structure

```text
opsmind/
└── backend/
    ├── app/
    │   ├── agents/
    │   ├── gateway/
    │   ├── providers/
    │   └── main.py
    ├── requirements.txt
    └── .env
```

---

## API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "status": "healthy",
  "service": "OpsMind"
}
```

### Generate Terraform

```http
POST /api/v1/generate
```

Request:

```json
{
  "prompt": "Create an OCI VM with 2 CPUs and 16GB RAM"
}
```

---

## Tech Stack

- Python
- FastAPI
- Google Gemini
- Terraform
- Oracle Cloud Infrastructure (OCI)
- Docker (Upcoming)

---

## Roadmap

### v0.1
- [x] FastAPI Backend
- [x] Gemini Integration
- [x] AI Gateway
- [x] Terraform Agent
- [x] OCI Terraform Generation

### v0.2
- [ ] Structured Terraform Output
- [ ] File Generation
- [ ] Terraform Validation
- [ ] Request Logging

### v0.3
- [ ] PostgreSQL
- [ ] Prompt History
- [ ] User Sessions

### v0.4
- [ ] Security Review Agent
- [ ] Kubernetes Agent
- [ ] Cost Optimization Agent

### v1.0
- [ ] React Frontend
- [ ] Authentication
- [ ] Multi-Agent Routing
- [ ] Infrastructure Deployment Workflows

---
## Current Features

### Day 1
- FastAPI backend
- AI Gateway
- Gemini integration

### Day 2
- Terraform file generation
- main.tf generation
- variables.tf generation
- outputs.tf generation

### Day 3
- Terraform validation engine
- Automatic terraform init
- Automatic terraform validate

### Day 4
- AutoFix Agent
- Validation error analysis
- Self-healing workflow framework
- Retry mechanism
- Error handling for LLM failures

## Roadmap

### Day 5
- Complete self-healing Terraform loop
- Multi-attempt auto-remediation
- Validation history

### Day 6
- Architecture diagram
- Dockerization improvements
- Project documentation
## Author

Vineet Pal

AI + Platform Engineering + Cloud Automation
