FROM python:3.9-slim

WORKDIR /app

# Set PYTHONPATH to include the current directory and app_cmd
ENV PYTHONPATH="${PYTHONPATH}:/app:/app/app_cmd"

# Copy the entire app into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the application
CMD ["python", "cmd/server/main.py"]
