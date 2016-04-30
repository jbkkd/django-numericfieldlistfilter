import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-numericfieldlistfilter',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A NumericFieldListFilter for Django admin',
    long_description=README,
    author='Omer Korner',
    author_email='omerkorner@gmail.com',
)
