FROM python:3.7
WORKDIR /usr/src/app
EXPOSE 80
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["./manage.py", "testserver", "--addrport", "0.0.0.0:80", "fixtures/init.json"]
