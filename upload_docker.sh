#!/usr/bin/env bash
# This file tags and uploads an image to Docker Hub

# Assumes that an image is built via `run_docker.sh`

# Step 1:
# Create dockerpath
dockerpath=na6an/api

# Step 2:  
# Authenticate & tag
echo "Docker ID and Image: $dockerpath"
docker tag a8d543ae30ec $dockerpath

# Step 3:
# Push image to a docker repository
docker push $dockerpath
