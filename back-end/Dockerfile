FROM python:3

ADD requirements.txt /iNex/
RUN pip install -r /iNex/requirements.txt

ADD /src/siteapp /iNex/src/siteapp
ADD /src/inex_page_home /iNex/src/inex_page_home
ADD /src/product /iNex/src/product
ADD /src/solutions /iNex/src/solutions
ADD /src/offer /iNex/src/offer
ADD /src/search /iNex/src/search
ADD /src/contact /iNex/src/contact
ADD /src/about /iNex/src/about

ADD src/manage.py /iNex/src

WORKDIR /iNex/src

EXPOSE 8000

CMD python manage.py runserver  0.0.0.0:8000