##
# all: do all the typical steps.
##
.PHONY: all
all: install sync build run ;

##
# help: display this help message.
##
.PHONY: help
help:
	@awk '/^##/{a=1-a}a' $(MAKEFILE_LIST) | cut -c3-

##
# install: install any project aspects; this will install the command `uv`.
##
.PHONY: install
install: 
	curl -LsSf https://astral.sh/uv/install.sh | sh
	@echo "The uv command should now be installed and available."

##
# sync: synchronize the project aspects; this will run the command `uv sync`.
##
.PHONY: sync
sync: 
	uv sync
	@echo "The uv command should now be synchronized and configured."

##
# build: build the site; this will build the documentation site ready to serve.
# This will ignore WARNINGS about README.md duplicating index.md because we have
# a convention of symlinking index.md and README.md which mkdocs interprets as
# a duplicate file to ignore (which is is) but we don't want this 'noise' in the
# output as genuine warnings will be lost. 
##
.PHONY: build
build: 
	uv run mkdocs build 2>&1 | grep -v "README\.md' from the site because it conflicts with.*index\.md'"
	@echo "The documentation should now be built"

##
# run: run the project aspects; this will launch the documentation server.
# Note this suppresses WARNINGS, use make build to check for WARNINGS.
##
.PHONY: run
run: 
	uv run mkdocs serve --quiet
	@echo "The documentation should now be available by browsing http://127.0.0.1:8000/"

##
# deploy: build and deploy the latest docs to GitHub pages (gh_pages branch push)
##
.PHONY: deploy
deploy:
	uv run mkdocs gh-deploy --force
	@echo "The documentation should now be available by browsing https://gigcymru.github.io/architecture/"

##
# lint: lint the project documentation using markdownlint-cli2
##
.PHONY: lint
lint:
	npx markdownlint-cli2 "doc/**/*.md" --config ".github/config/custom.markdownlint.jsonc"
	@echo "The markdownlint-cli2 command should now be complete."

##
# newline: display a newline character so we can print prettier messages.
##
.PHONY: newline
define newline


endef
