# syntax=docker/dockerfile:1
FROM python
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "object_detection.py", "run"]