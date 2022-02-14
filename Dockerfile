FROM python:3.6


# Creating Application Source Code Directory
RUN mkdir -p /application
RUN mkdir /log

# Setting Home Directory for containers
WORKDIR /application

# Installing python dependencies
COPY requirements.txt /application
COPY run.sh /run.sh
RUN pip install --no-cache-dir -r requirements.txt

# Running Python Application
CMD ["bash", "/run.sh"]
