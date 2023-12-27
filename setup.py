from setuptools import setup, find_packages

setup(
    name="pytermux",
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    package_data={"": ["LICENSE", "README.rst"]},
)
