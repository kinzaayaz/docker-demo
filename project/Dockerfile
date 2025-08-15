# FROM nginx:alpine

# WORKDIR /myapp

# COPY . .

# EXPOSE 80


FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy Python file into container
COPY test.py .

# Run the Python file when container starts
CMD ["python", "test.py"]
