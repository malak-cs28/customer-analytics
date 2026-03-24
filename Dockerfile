FROM python:3.11-slim

# Create working directory
RUN mkdir -p /app/pipeline
WORKDIR /app/pipeline

# Copy project files
COPY . /app/pipeline

# Install required libraries
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn scikit-learn scipy requests six==1.16.0 python-dateutil==2.8.2

# Make summary.sh executable
RUN chmod +x summary.sh

# Start interactive shell
CMD ["bash"]