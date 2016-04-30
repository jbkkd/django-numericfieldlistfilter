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
    license='MIT',
    description='A NumericFieldListFilter for Django admin',
    long_description=README,
    author='Omer Korner',
    author_email='omerkorner@gmail.com',
    url='https://github.com/jbkkd/django-numericfieldlistfilter',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Operating System :: OS Independent',
    ],
    keywords='django plugin fieldlistfilter'
)
