# Use the official Python 3.11 slim image as a lightweight base
FROM python:3.11-slim

# Set the working directory inside the container
# All subsequent commands will be executed in this directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install all dependencies listed in requirements.txt
# --no-cache-dir avoids saving package cache to reduce space usage
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose port 5000, the one used by Flask
EXPOSE 5000

# Set environment variables for Flask
# FLASK_APP specifies the module and the function that creates the Flask app
# FLASK_RUN_HOST 0.0.0.0 allows Flask to be accessible from outside the container
ENV FLASK_APP=app:crea_app
ENV FLASK_RUN_HOST=0.0.0.0

# Command executed when the container starts
# Launches the Flask app in development server mode
CMD ["flask", "run"]
