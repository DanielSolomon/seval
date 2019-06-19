import pathlib
import setuptools

reqs_file = pathlib.Path(__file__).parent / 'requirements.txt'
reqs = []
if reqs_file.is_file():
    with open('requirements.txt', 'r') as reader:
        reqs = reader.read().splitlines()

setuptools.setup(
    name                = 'seval',
    version             = '1.1.0',
    url                 = 'http://github.com/DanielSolomon/seval',
    author              = 'Daniel Solomon',
    author_email        = 'DanielSolomon94.ds@gmail.com',
    license             = 'MIT',
    packages            = ['seval'],
    zip_safe            = False,
    install_requires    = reqs,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)