FROM python:3.7

ADD main.py /
ADD SparseArray.py /

ENV STRINGS "ab,abcd,bc,ab"
ENV QUERIES "ab,bd,abcd"

ENTRYPOINT ["python", "./main.py"]