FROM python:3-alpine

WORKDIR /usr/src/app

RUN apk add make

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app

CMD [ "python"]
