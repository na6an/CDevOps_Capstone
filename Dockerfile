FROM python:3.8-slim-buster

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY . app.py /app/
# COPY . nlib /app/

# Resove "RuntimeError: Broken toolchain: cannot link a simple C program"
RUN apt-get update
RUN apt-get -y install gcc g++ python3-dev python3-pip libgl1-mesa-glx

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt
    
## Step 4:
# Expose port 80
EXPOSE 80
EXPOSE 8000

## Step 5:
# Run app.py at container launch
CMD ["python", "app.py"]
