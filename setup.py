from setuptools import setup, find_packages

# Usage: python setup.py sdist bdist_wheel

links = []  # for repo urls (dependency_links)

with open('requirements.txt') as fp:
    install_requires = fp.read()

DESCRIPTION = "A python module to manage AWS EC2 instances."
LONG_DESCRIPTION = open('README.md').read()
VERSION = "0.8"


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ec2-task",
    version=VERSION,
    author="Shubham Dipt",
    author_email="shubham.dipt@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/shubhamdipt/aws-ec2-task",
    license=open('LICENSE').read(),
    packages=['ec2_task'],
    platforms=["any"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=install_requires,
    dependency_links=links,
)