FROM Python:3.10

RUN -p mkdir /usr/src/location_app/
WORKDIR /usr/src/location_app/

COPY . /usr/src/location_app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
