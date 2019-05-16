"""
Fast implementation of pattern matching in Python(using gestalt approach).
"""
import os
from setuptools import setup, Extension

HERE = os.path.abspath(os.path.dirname(__file__))
source = ['pyymatcher/accel.cpp']


def get_description():
    README = os.path.join(HERE, 'README.md')
    with open(README, 'r') as f:
        return f.read()


cpp_module = Extension('accel', sources=source)

setup(
    name='pyymatcher',
    packages=['pyymatcher'],  # this must be the same as the name above
    ext_modules=[cpp_module],
    version="0.0.3",
    description="Fast implementation of pattern matching in Python(using gestalt approach)",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    author='Abdul Niyas P M',
    author_email='abdulniyaspm@gmail.com',
    url='https://github.com/abdulniyaspm/pyymatcher',
    license='MIT',
    keywords=['pattern-matching', 'pyymatcher'],  # arbitrary keywords
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
    python_requires='>=3.6',
)
