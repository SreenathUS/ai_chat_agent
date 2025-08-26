# AI Chat Agent with Context Memory

This is a **conversational AI agent** that maintains context across multiple interactions using a language model and Redis for session memory. The project is containerized with Docker and deployed on Kubernetes (Minikube) with auto-scaling (HPA).

## Features
- Multi-turn conversational AI with memory
- RESTful API using FastAPI
- Session memory stored in Redis
- Dockerized for easy deployment
- Kubernetes deployment with Horizontal Pod Autoscaler (HPA) for auto-scaling
- NodePort service for external access

## Tech Stack
- **Python:** FastAPI, OpenAI API, Redis
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **AI:** Language models (OpenAI)

## Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ai-chat-agent-project
```

### 2. Set OpenAI API Key
```bash
export OPENAI_API_KEY=<your_openai_api_key>
```

### 3. Build Docker image
```bash
eval $(minikube docker-env)
docker build -t chat-agent:latest -f docker/Dockerfile .
```

### 4. Deploy to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

### 5. Access API
```bash
minikube service chat-agent-service --url
```

### 6. Test API
```bash
python3 test_request.py
```

## Personal Project Notes
This project demonstrates:
- AI agent development with memory
- Cloud-native deployment and scaling
- MLOps practices
