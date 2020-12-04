from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
with open(path.join(this_directory, "keyboardlayout/version.py")) as f:
    exec(f.read(), version)

setup(
    name = 'keyboardlayout',
    install_requires = ['PyYAML >= 5.3.1', 'pygame >= 2.0.0'],
    python_requires='>=3',
    version = version['__version__'],
    description = 'A python library to display different keyboards',
    author = 'Justin Black',
    packages = find_packages(),
    package_data={'keyboardlayout': ['keyboardlayout/layouts/*.yaml']},
    url = "https://github.com/spacether/keyboardlayout",
    keywords = ["keyboard", "qwerty", "layout", "azerty"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'sphinx',
            'pytest',
        ]
    },
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Games/Entertainment :: Simulation',
        'Development Status :: 5 - Production/Stable',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
