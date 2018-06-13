# -*- coding: utf-8 -*-
import multiprocessing
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import sys


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


CLASSIFIERS = ['Environment :: Web Environment',
'Framework :: Django',
'Intended Audience :: Science/Research',
'Intended Audience :: Education',
'Programming Language :: Python',
'Programming Language :: JavaScript',
'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
'Topic :: Multimedia :: Sound/Audio',
'Topic :: Multimedia :: Sound/Audio :: Analysis',
'Topic :: Multimedia :: Sound/Audio :: Players',
'Topic :: Scientific/Engineering :: Information Analysis',
'Topic :: System :: Archiving',  ]


setup(
  name = "Telemeta",
  url = "http://telemeta.org",
  description = "Open web audio application with semantics",
  long_description = open('README.rst').read(),
  author = "Guillaume Pellerin",
  author_email = "yomguy@parisson.com",
  version = '1.7.0',
  install_requires = [
        'django==1.8.*',
        'django-registration-redux',
        'django-extensions',
        'django-timezones',
        #'django-jqchat',
        'django-debug-toolbar==1.6',
        'django-extra-views',
        'django-breadcrumbs',
        'django-bootstrap3==8.1.0',
        'django-bootstrap_datepicker',
        'django-bootstrap-pagination',
        'django-json-rpc',
        'django-suit',
        'django-ipauth',
        'django-celery',
        'timeside>=0.7',
        'docutils',
        'psutil',
        'pyyaml',
        'python-ebml',
        'zipstream',
        'elasticsearch==1.6.0',
        'django-haystack',
        'ebooklib',
        'django-environ',
        'redis',
        'Werkzeug',
        'django-dirtyfields',
        'sqlparse==0.2.2',
        'django_select2==5.11.1',
        'lxml',
        'django-leaflet',
        'django-geojson',
        'django-markdownx',
    ],
  tests_require=['pytest-django', 'pytest-cov', 'factory-boy'],
  # Provide a test command through django-setuptest
  cmdclass={'test': PyTest},
  platforms=['OS Independent'],
  license='CeCILL v2',
  classifiers = CLASSIFIERS,
  packages = find_packages(),
  include_package_data = True,
  zip_safe = False,
)
