FROM python:3.8-slim-buster

WORKDIR /flask_app

RUN apt-get update && apt-get install git -y && git clone https://github.com/navodissa/pipeline_test.git
RUN cd pipeline_test && pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "application.py"]