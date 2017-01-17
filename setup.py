from setuptools import setup, find_packages
from os.path import join, dirname

install_requires = [
    'lxml==3.7.2',
]

setup(
    name='ngenix_test',
    version='1.0.0',
    description='Test task for NGENIX',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    url='https://github.com/frankegoesdown/ngenix_test',
    author='Alexander Chernikov',
    author_email='frankich@mail.ru',
    install_requires=install_requires
)
