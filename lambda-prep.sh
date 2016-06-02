#!/bin/bash -O extglob

if [ ! -d env ]; then
    LC_ALL=C virtualenv env
    env/bin/pip install -e .
fi

if [ -f lambda-deploy.zip ]; then
    rm lambda-deploy.zip
fi

zip lambda-deploy *.py *.json cjkvi-ids/ids.txt -x \*.pyc

cd env/lib/python2.7/site-packages
zip -r ../../../../lambda-deploy ./!(pip*|wheel*|setuptools*|easy_install*) \
    -x \*.pyc
