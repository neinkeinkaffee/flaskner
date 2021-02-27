from distutils.core import setup
from setuptools import find_packages
from pip._internal.req import parse_requirements

def load_requirements(file_name):
    requirements = parse_requirements(file_name, session='test')
    return [str(r.requirement) for r in requirements]

setup(
    name='flaskner',
    version='0.0.1',
    description='A simple NER API',
    install_requires=load_requirements('requirements.txt'),
    extras_require={'dev': ['pytest', 'selenium']}
)
