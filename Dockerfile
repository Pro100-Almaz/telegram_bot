FROM python:3.7-slim 


WORKDIR /botname 


COPY requirments.txt /botname/ 
RUN pip install -r /botname/requirments.txt
COPY . /botname/

CMD python3 /botname/app.py