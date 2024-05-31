# Use a base Python image
FROM python:3.12.3

# Set working directory
WORKDIR /myproject

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the Django project code
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
