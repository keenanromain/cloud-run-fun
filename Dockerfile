FROM python:3.7-slim

# Copy local into the container image
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install dependencies
RUN pip install --upgrade -r requirements.txt

# Run the web service on container startup via gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --chdir app app:app
