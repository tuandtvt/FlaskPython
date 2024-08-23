FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# install mysql client
RUN apt-get update && apt-get install -y default-mysql-client

# Install firefox
RUN apt-get update && apt-get install firefox-esr -y

COPY . .
EXPOSE 5000
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
# CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["gunicorn","--reload", "--workers=4", "--bind=0.0.0.0:5000","--timeout=6000", "app:app","debug=True"]
