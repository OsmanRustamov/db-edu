FROM python:3.11.3-bullseye as builder

WORKDIR /backend

COPY ./backend/requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend .

CMD ["python", "main.py"]
