from setuptools import setup, find_packages

with open("README.md","r") as f:
    long_description = f.read()
    
    
setup(
    name='finseriestools',                       # Required
    version='0.1.0',                                # Required
    description='Tools for Financial Time Series',  # Optional
    long_description=long_description,              # Optional
    packages=find_packages()                        # Required
)