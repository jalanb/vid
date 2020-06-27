import os
from dataclasses import dataclass
from setuptools import find_packages
from setuptools import setup

import vid as project




description = "vid is a visual editor"
headline = description.splitlines()[0]
name = project.__name__,
version = project.__version__,

@dataclass
class User:
    service: str
    username: str
    email: str
    name: str

    def url(self, name):
        return f'https://{self.service}/{self.username}/{name}'

user = User('github.com', 'jalanb', github@al-got-rhythm.net', 'J Alan Brogan')

setup(
    name=name,
    version=version,
    description=headline,
    long_description=description,
    url=user.url(name),
    packages=find_packages(),
    package_data={'': package_files('{name}')},
    download_url='{user.url(name)}/tarball/v{version}',
    license='MIT License',
    author=user.name,
    author_email='github@al-got-rhythm.net',
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
    ],
    install_requires=[
        'pysyte',
        'zatso',
    ],
    tests_require=['pytest'],
    extras_require={
        'testing': ['pytest'],
    }
)
