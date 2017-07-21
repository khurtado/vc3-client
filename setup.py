#!/usr/bin/env python
#
# Setup prog for vc3-client
#
#

release_version='0.9.1'

import sys

from setuptools import setup

etc_files = ['etc/vc3-client.conf']

scripts = ['scripts/vc3-client', ]

rpm_data_files = [('/usr/bin', scripts),
                ('/etc/vc3', etc_files),
               ]

home_data_files = [
                 #('etc', libexec_files),
                 ('etc', etc_files),
                ]


def choose_data_files():
    rpminstall = True
    userinstall = False
     
    if 'bdist_rpm' in sys.argv:
        rpminstall = True

    elif 'install' in sys.argv:
        for a in sys.argv:
            if a.lower().startswith('--home'):
                rpminstall = False
                userinstall = True
                
    if rpminstall:
        return rpm_data_files
    elif userinstall:
        return home_data_files
    else:
        # Something probably went wrong, so punt
        return rpm_data_files
       
# ===========================================================

# setup for distutils
print(choose_data_files())
print(scripts)
setup(
    name="vc3-client",
    version=release_version,
    description='vc3-client package',
    long_description='''This package contains vc3 client''',
    license='GPL',
    author='VC3 Team',
    author_email='vc3-project@googlegroups.com',
    maintainer='VC3 team',
    maintainer_email='vc3-project@googlegroups.com',
    url='http://virtualclusters.org/',
    packages=['vc3client'],
    scripts=scripts,
    data_files=['etc/vc3-client.conf'],
    install_requires=['requests', 'pyopenssl', 'cherrypy', 'pyyaml']
)
