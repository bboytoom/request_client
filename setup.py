import pathlib
from setuptools import setup, find_packages

PATH = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'request-helper'
DESCRIPTION = 'request-helper simplify the construction of HTTP requests'
LONG_DESCRIPTION = (PATH / 'README.md').read_text(encoding='utf-8')
LONG_DESC_TYPE = 'text/markdown'

AUTHOR = 'Tomas Rosas'
AUTHOR_EMAIL = 'thomasrosber@gmail.com'
URL = 'https://github.com/bboytoom/request-helper'

LICENSE = 'MIT'

INSTALL_REQUIRES = [
    'requests'
    ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    install_requires=[],
    keywords=['python', 'requests', 'helper', 'oauth2'],
    packages=find_packages(),
    include_package_data=True
    )
