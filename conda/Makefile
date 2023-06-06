BUCKET=wfp-vam-www
VERSION=0.1.1
BUILD=0
HDC_INDEX=../../hdc-conda-index

.PHONY: all
all: pkg

.PHONY: pkg
pkg: |build
	env VERSION=$(VERSION) BUILD=$(BUILD) conda build --no-test --no-anaconda-upload --output-folder ./build recipe

.PHONY: index-local
index-local:
	conda index -s noarch -n hdc $(HDC_INDEX)
	cp ./build/noarch/*tar.bz2 $(HDC_INDEX)/noarch/
	conda index -s noarch -n hdc $(HDC_INDEX)

build:
	mkdir $@