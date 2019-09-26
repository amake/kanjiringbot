SHELL := /bin/bash -O extglob
ids-txt := vendor/cjkvi-ids/ids.txt
payload := dist/lambda-deploy.zip
lambda-name := KanjinowaTwitterBot
aws-args ?=

.PHONY: zip
zip: $(payload)

.env:
	virtualenv .env
	.env/bin/pip install -e .

dist:
	mkdir -p $(@)

.PHONY: clean
clean:
	rm -rf dist

.PHONY: update
update: | .env
	.env/bin/pip install --upgrade pip
	.env/bin/pip install --upgrade --upgrade-strategy eager -e .
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

.PHONY: deploy
deploy: $(payload)
	aws $(aws-args) lambda update-function-code \
		--function-name $(lambda-name) \
		--zip-file fileb://$$(pwd)/$(<)

.PHONY: invoke
invoke:
	aws $(aws-args) lambda invoke \
		--function-name $(lambda-name) \
		/dev/null

.PHONY: test
test: | $(ids-txt) .env
	.env/bin/python kanjiring.py
