import pathlib
import setuptools

#The directory containing this file
BASE = pathlib.Path(__file__).parent

# The text of the readme file
README = (BASE / "README.md").read_text()

#This call to setup does all the work
setuptools.setup(
    name="cvc-xls-generator",
    version="1.0.3",
    deecription="It generates xls file",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/devarajug/cvc-xls-generator",
    author="Devaraju Garigapati",
    author_email="devarajugarigapati@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["pandas", "openpyxl"],
    python_requires='>=3.6'
)