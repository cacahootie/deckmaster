"""
deckmaster
------------
Deckmaster is a server which can provide static assets via jinja2 templating.
"""
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]


setup(
    name='deckmaster',
    version='0.0.1',
    url='http://github.com/cacahootie/deckmaster/',
    license='MIT',
    author='Bradley Alan Smith',
    author_email='brad.alan.smith@gmail.com',
    description='Serving static assets to support SPA using Flask and Jinja2.',
    long_description=__doc__,
    packages=['deckmaster',],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=reqs,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points='''
        [console_scripts]
        flask=flask.cli:main
    '''
)