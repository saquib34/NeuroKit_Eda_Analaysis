from setuptools import setup, find_packages

setup(
    name='eda_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'neurokit2',
        'scipy'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library for processing and analyzing EDA signals.',
    url='https://github.com/yourusername/eda_analysis',
)
