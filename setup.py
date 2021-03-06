#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ncc',
    version="0.1",
    description='ncc is the Nuxeo Cloud Controller',
    author='Stefane Fermigier',
    author_email='sf@nuxeo.com',
    url='https://github.com/compatible/nuxeo-cloud-controler',
    packages=find_packages(),
    # Not needed (yet?)
    #data_files=[('ncc', ['config/nginx.conf']),],
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points={
        'console_scripts': [
            'ncc = ncc.main:main',
            'nuxeowrapper = ncc.nuxeowrapper:main',
        ]
    },
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development',
          'Topic :: System :: Systems Administration',
    ],
)
