from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aws-config-utils",
    version="0.1.0",
    author="Jon Price",
    author_email="jon@zer0day.net",
    description="Utilities for working with AWS Config resource types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jon-the-dev/aws-config-utils",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "aws-config-utils=aws_config_utils.cli:main",
        ],
    },
)
