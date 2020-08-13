#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=na6an/api

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run api --image=na6an/api --port=80

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
# kubectl port-forward deployment/api  8000:80
kubectl expose deployment api --type=LoadBalancer --port=8000 --target-port=80
