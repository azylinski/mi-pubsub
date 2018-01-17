FROM python:3.6.4-alpine

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN mkdir -p /usr/src/app
COPY src /usr/src/app

WORKDIR /usr/src/app

CMD ["python", "main.py"]