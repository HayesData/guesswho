import os
from setuptools import setup
import guesswho

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "GuessWho",
	version = guesswho.__version__,
	author = "Chris Hayes",
	author_email = "chris@hayesdata.com",
	description = "A python wrapper for the unix/linux whois command.",
	license="Apache License, Version 2.0",
	keywords = "whois",
	url = "https://github.com/HayesData/guesswho",
	packages=['guesswho'],
	long_description=read('README.md'),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Topic :: Utilities",
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: POSIX",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.1",
		"Programming Language :: Python :: 3.2",
		"Programming Language :: Python :: 3.3",
	],
)