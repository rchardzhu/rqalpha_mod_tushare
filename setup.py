import sys
from setuptools import find_packages, setup

requirements = [
    'rqalpha',
    'tushare'
]

setup(
    name='rqalpha-mod-tushare',     #mod名
    version="0.1.0",
    description='RQAlpha Mod to tushare',
    packages=find_packages(exclude=[]),
    author='Richard Zhu',
    author_email='rchardzhu@gmail.com',
    license='Apache License v2',
    package_data={'rqalpha-mod-tushare': ['*.*']},
    url='https://github.com/rchardzhu/rqalpha-mod-tushare',
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
    ],
)