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
    author='Mohammad Saquib Daiyan',
    author_email='shadmanshahin6@gmail.com',
    description='A library for processing and analyzing EDA signals.',
    url='https://github.com/saquib34/NeuroKit_Eda_Analaysis',
    classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.11',
)
