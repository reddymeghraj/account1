from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='account1',
    version=version,
    description='Account for medical Equipment',
    author='wayzontech',
    author_email='wayzon@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
