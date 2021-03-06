from setuptools import setup


setup(
    name = 'pypdb',
    packages = ['pypdb'],  # same as 'name'
    version = '1.102',
    install_requires=[
        'xmltodict',
        'beautifulsoup4'
    ],
    description = 'A Python wrapper for the RCSB Protein Data Bank (PDB) API',
    author = 'William Gilpin',
    author_email = 'firstnamelastname(as one word)@googleemailservice',
    url = 'https://github.com/williamgilpin/pypdb',
    download_url = 'https://github.com/williamgilpin/pypdb/tarball/0.6',
    keywords = ['protein', 'data', 'RESTful', 'api'],
    classifiers = [],
)
