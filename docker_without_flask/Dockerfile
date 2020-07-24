FROM python:3.7

COPY . /

ENV STRINGS "ab,abcd,bc,ab"
ENV QUERIES "ab,bd,abcd"

ENTRYPOINT ["python", "./main.py"]