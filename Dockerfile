FROM python:3.10

RUN mkdir -p /usr/src/location_app/
WORKDIR /usr/src/location_app/

COPY . /usr/src/location_app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "run.py"]