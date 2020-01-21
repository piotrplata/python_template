FROM python:3.6.4

RUN adduser --disabled-password --gecos '' tmpuser

ADD . .
RUN pip install --upgrade pip
RUN ls -all
RUN pip install -r requirements.txt
RUN python setup.py install

CMD ["python_template_run"]