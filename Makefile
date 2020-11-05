VERSION=0.0.5

all:
	@echo "Select target"

ver:
	find . -type f -name "*.py" -exec \
			sed -i "s/^__version__ = .*/__version__ = '${VERSION}'/g" {} \;
	find ./bin -type f -exec sed -i "s/^__version__ = .*/__version__ = '${VERSION}'/g" {} \;

clean:
	rm -rf dist build sshare.egg-info

d: clean sdist

sdist:
	python3 setup.py sdist

build: clean build-packages

build-packages:
	python3 setup.py build

pub: d pub-pypi

pub-pypi:
	twine upload dist/*
