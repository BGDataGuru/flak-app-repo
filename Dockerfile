FROM python:3.11.10-bookworm
WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

#CMD ["python3", "-m", "flask", "run", "app.py", "--host=0.0.0.0"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

#CMD ["python", "-m", "flask", "run", "-0-host=0.0.0.0"]
