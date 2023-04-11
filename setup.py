import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Tom Toolbox",
    version="0.0.1",
    author="Tom5521",
    description="A collection of utilities for python 3.10 and above",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tom5521/Toolbox",
    packages=setuptools.find_packages(exclude=["test.py", ".gitignore"]),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)