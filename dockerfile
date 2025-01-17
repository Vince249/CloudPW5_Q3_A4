FROM python:3.7

EXPOSE 5000

WORKDIR /app

COPY . . 

RUN pip install -r requirements.txt

CMD python3 app.py