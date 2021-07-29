# syntax=docker/dockerfile:1

FROM python

WORKDIR /cvlib-detection

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "-m" , "face_detection.py", "run", "--host=0.0.0.0"]