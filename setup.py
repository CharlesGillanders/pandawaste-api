from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="alphaess",
    version="0.0.1",
    author="Charles Gillanders",
    author_email="charles@charlesgillanders.com",
    description="A python library to retrieve waste collection information from Panda Waste in Ireland by scraping the Panda Waste customer portal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CharlesGillanders/pandawaste",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
