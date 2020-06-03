FROM python:alpine
WORKDIR /usr/src/app
EXPOSE 80
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["./manage.py", "testserver", "--addrport", "0.0.0.0:80", "fixtures/init.json"]
