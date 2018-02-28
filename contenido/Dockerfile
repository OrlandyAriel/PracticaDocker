FROM python:3.6.3-jessie
ADD ./codigo /codigo
WORKDIR /codigo 
RUN pip install -r requirements.txt
CMD ["python", "app_web.py"]