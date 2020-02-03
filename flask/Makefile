UNAME := $(shell uname)

all: install_python setup_env


install_python:
ifeq (, $(shell which python3))

ifeq ($(UNAME), Linux)
apt-get_python
endif

ifeq ($(UNAME), Darwin)
install_hombrew brew_python
endif

endif
		@echo "Python setup complete."


setup_env: install_pipenv
		pipenv --three
		pipenv run pipenv install
		pipenv run pre-commit install
		@echo "Environment setup complete."
		pipenv shell


install_hombrew:
ifeq (, $(shell which brew))
$(shell /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)")
else
		@echo "Homewbrew already installed."
endif


brew_python:
ifeq (, $(shell which python3))
brew install python
else
		@echo "Python already installed."
endif


apt-get_python:
ifeq (, $(shell which python3))
apt-get install python3 pip
else
		@echo "Python already installed."
endif


install_pipenv:
ifeq (, $(shell which pipenv))
pip3 install pipenv
else
		@echo "Pipenv already installed."
endif

