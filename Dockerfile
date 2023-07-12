FROM python:3.10.0

WORKDIR /root/Barath

COPY . .

RUN pip3 install --upgrade pip setuptools

RUN pip3 install -U pip && pip3 install -U -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

CMD ["python3", "-m", "Barath"]
