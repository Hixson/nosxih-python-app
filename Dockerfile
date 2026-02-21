# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install Flask
RUN pip install flask

# Copy our code into the container
COPY app.py .

# Create the directory where the QNAP will be mounted
RUN mkdir -p /app/data

# Expose the port Flask runs on
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
