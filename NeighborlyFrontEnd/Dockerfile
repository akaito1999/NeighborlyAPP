# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

ENV host:logger:consoleLoggingMode=always

WORKDIR /app
#COPY . /app

# Add files from this repo to the root site folder.
COPY . /home/site/wwwroot

EXPOSE 5000

#RUN pip install -r requirements.txt
# Install requirements
RUN cd /home/site/wwwroot && pip install -r requirements.txt

COPY . .
ENTRYPOINT ["python"]
CMD ["app.py"]