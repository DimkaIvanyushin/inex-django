FROM python:3

ADD requirements.txt /iNex/
RUN pip install -r /iNex/requirements.txt

ADD /siteapp /iNex/src/siteapp

ADD manage.py /iNex/src

WORKDIR /iNex/src

EXPOSE 8000

CMD python manage.py runserver  0.0.0.0:8000