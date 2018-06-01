SHELL := /bin/bash -O extglob
ids-txt := vendor/cjkvi-ids/ids.txt
payload := dist/lambda-deploy.zip
lambda-name := KanjinowaTwitterBot

.PHONY = zip clean update deploy test

zip: $(payload)

.env:
	virtualenv .env
	.env/bin/pip install -e .

dist:
	mkdir -p $(@)

clean:
	rm -rf dist

update: | .env
	.env/bin/pip install --upgrade -e .
	cd vendor/cjkvi-ids; git checkout master && git pull

$(payload): *.py credentials.json $(ids-txt) | .env dist
	rm -rf $(@)
	zip $(@) $(^) -x \*.pyc
	root=$$(pwd); cd .env/lib/python3.6/site-packages; \
		zip -r $$root/$(@) ./!(pip*|wheel*|setuptools*|easy_install*) -x \*.pyc

credentials.json:
	.env/bin/python auth_setup.py

$(ids-txt):
	git submodule sync
	git submodule update

deploy: $(payload)
	aws lambda update-function-code \
		--function-name $(lambda-name) \
		--zip-file fileb://$$(pwd)/$(<)

test: | .env
	.env/bin/python kanjiring.py
