from setuptools import setup

#with open('README.md') as f:
       # long_description = f.read()
from pathlib import Path
this_directory = Path(__file__).parent
long_description = ("README.md").read_text()

setup(
	name='cwutils',
	version='1.2.0',
	description='test',
    #long_description=long_description,
	author='Chaos and whoami.exe',
	author_email='nonono@nono.no',
	url='https://xllmoon.web.app',
	install_requires = [
		'humanfriendly',
        'num2words'
	],
	packages=['cwutils'],
	long_description=long_description,
	long_description_content_type='text/markdown'
)
