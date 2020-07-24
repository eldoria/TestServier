FROM python:3.7

ADD server.py /
ADD dict.py /
ADD swagger.yml /

RUN pip install flask
RUN pip install flask_restful
RUN pip install connexion
RUN pip install connexion[swagger-ui]

CMD ["python", "server.py", "--host", "0.0.0.0"]