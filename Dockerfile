FROM tiangolo/uwsgi-nginx-flask:python3.9

WORKDIR /app

COPY ./app /app/app

COPY ./requirements.txt /app
COPY ./db_creator.py /app
COPY ./run.py /app

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN python /app/db_creator.py

CMD ["python", "/app/run.py"]
