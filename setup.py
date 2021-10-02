from distutils.core import setup

with open('README.md') as f:
        long_descripotion = f.read()

setup(
	name='cwutils',
	version='1.1.0',
	description='test',
        long_description=long_description,
	author='Chaos and whoami.exe',
	author_email='nonono@nono.no',
	url='https://xllmoon.web.app',
	install_requires = [
		'humanfriendly',
                'num2words'
	],
	packages=['cwutils']
)
