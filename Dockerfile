FROM python:3.9.18 
WORKDIR /jkphotoApp
COPY requirements.txt /jkphotoApp/
RUN pip install -r requirements.txt
COPY . .
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
