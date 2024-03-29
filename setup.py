import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages

exec(open("sequenticon/version.py").read())  # loads __version__

setup(
    name="sequenticon",
    version=__version__,
    author="Zulko",
    description="Generate human-friendly icons from DNA sequences",
    long_description=open("pypi-readme.rst").read(),
    license="MIT",
    keywords="DNA sequence barcoding sequenticon identicon hash",
    packages=find_packages(exclude="docs"),
    include_package_data=True,
    install_requires=[
        "Biopython",
        "pydenticon",
        "snapgene_reader",
        "flametree",
        "pdf_reports",
    ],
)
