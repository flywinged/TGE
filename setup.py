from distutils.core import setup

import setuptools

# pypi commands
# https://packaging.python.org/guides/using-testpypi/
# https://packaging.python.org/tutorials/packaging-projects/

setup(
    name = 'gent',
    packages = setuptools.find_packages(),
    version = '0.0.1a1',
    license = 'MIT',
    description = 'gent (Game ENgine for Terminals), is a library to allow game like interactions in user terminals',
    author = 'Clayton Brown',
    author_email = 'clayton.john.brown@gmail.com',
    url = "https://github.com/flywinged/gent",
    # download_url = 'https://github.com/flywinged/pyGEfT/archive/v_01.tar.gz',
    keywords = ['Terminal', 'Graphics', 'Game', 'Engine'],
    install_requires = [            # I get to this in a second
        'numpy',
        'colorama',
        'sty',
        "Pillow",
        "pynput"
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)