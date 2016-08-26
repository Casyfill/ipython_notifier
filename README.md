# Ipython Notifyer

Ipython notifyer is dependent on **pync**  package and meant as a tiny decorator for your heavy long functions.
It is especially useful in the Ipython, as web browser can lead to the massive destruction :-)

## Dependency

- [pync](https://github.com/setem/pync), which, in its turn, is a wrapper around [terminal-notifier](https://github.com/julienXX/terminal-notifier)

## Installation

	pip install git+https://github.com/Casyfill/ipython_notifier@master

## Example

[ipython example](example.ipynb)

## Roadmap

- [x] initial sketch
- [x] example and screen-shot
- [x] check pip install
- [x] exception
- [x] timer
- [x] now wrapper inherits docstring, name and module metadata from original function (for debugging purposes)
- [x] simple nosetests
- [ ] print job name
- [ ] check licenses
- [ ] create wheel
- [ ] create anaconda package 
