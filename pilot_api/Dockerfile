FROM python:3.8 
WORKDIR /pilot_api 
COPY . . 
RUN pip install -r requirements.txt
RUN pytest
EXPOSE 5000 
ENTRYPOINT ["python3", "app.py"]