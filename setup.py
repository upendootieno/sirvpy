import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SirvPy",
    version="1.2",
    author="TechniCollins",
    author_email="technicollins.business@gmail.com",
    description="A python library for the Sirv REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TechniCollins/SirvPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires =[
    'requests'
    ],
    include_package_data=True,
    python_requires='>=3.8',
)