from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory/"README.md").read_text()

setup(
	name='cwutils',
	version='1.1.1a',
	description='Utils by Chaos and Whoami.',
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
