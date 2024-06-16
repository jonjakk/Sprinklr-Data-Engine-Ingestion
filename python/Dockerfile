FROM python:3.9-slim

WORKDIR /app

# Install dependencies
RUN pip install requests paramiko

# Copy the script into the container
COPY script.py .

CMD ["python","-u", "script.py"]
