import codecs
import os.path
import re

from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='mygit-protyotype',
    version=find_version('mygit', '__init__.py'),
    description='A prototype of an imitation of Git',
    packages=['mygit'],
    entry_points={
        'console_scripts': [
            'mygit = mygit.__main__:main',
        ]
    },
    install_requires=[],
)
