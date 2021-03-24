FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./src/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY ./src .

#Production Setup
# CMD ["uwsgi", "--ini", "app.ini"]
#Dev EnvironmentSetups
#CMD ["flask", "run"]
CMD ["python", "app.py"]
