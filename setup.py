from setuptools import setup, find_packages

setup(
    name="testpypi",
    version="0.1.0",
    author="aminsadeghi",
    author_email="aminsadeghi1990z@gmail.com",
    description="A short description of the package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/aminsadeghi1990/testpypi.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your dependencies here
    ],
)
