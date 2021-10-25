SHELL := /bin/bash -O extglob
venv := .env
ids-txt := vendor/cjkvi-ids/ids.txt
payload := dist/lambda-deploy.zip
lambda-name := KanjinowaTwitterBot
python := python3.9
aws-args ?=

.PHONY: zip
zip: $(payload)

$(venv):
	virtualenv -p $(python) $(@)
	$(@)/bin/pip install -e .

dist:
	mkdir -p $(@)

.PHONY: clean
clean: ## Clean generated files
clean:
	rm -rf dist

.PHONY: update
update: ## Update dependencies and data
update: | $(venv)
	$(venv)/bin/pip install --upgrade pip
	$(venv)/bin/pip install --upgrade --upgrade-strategy eager -e .
	cd vendor/cjkvi-ids; git checkout master && git pull

$(payload): *.py credentials.json $(ids-txt) | $(venv) dist
	rm -rf $(@)
	zip $(@) $(^) -x \*.pyc
	root=$$(pwd); cd $(venv)/lib/$(python)/site-packages; \
		zip -r $$root/$(@) ./!(pip*|wheel*|setuptools*|easy_install*) -x \*.pyc

credentials.json: | $(venv)
	$(venv)/bin/python auth_setup.py

$(ids-txt):
	git submodule sync
	git submodule update --init

.PHONY: deploy
deploy: ## Deploy to AWS Lambda
deploy: $(payload)
	aws $(aws-args) lambda update-function-code \
		--function-name $(lambda-name) \
		--zip-file fileb://$$(pwd)/$(<)

.PHONY: invoke
invoke: ## Invoke AWS Lambda
invoke:
	aws $(aws-args) lambda invoke \
		--function-name $(lambda-name) \
		/dev/null

.PHONY: test
test: ## Test locally
test: | $(ids-txt) $(venv)
	$(venv)/bin/python kanjiring.py

.PHONY: help
help: ## Show this help text
	$(info usage: make [target])
	$(info )
	$(info Available targets:)
	@awk -F ':.*?## *' '/^[^\t].+?:.*?##/ \
         {printf "  %-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
