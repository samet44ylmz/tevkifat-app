from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# Uygulama versiyonunu __init__.py icinden okur
from tevkifat import __version__ as version

setup(
	name="tevkifat",
	version=version,
	description="Tevkifat Modulu",
	author="PrimeIT",
	author_email="sametyilmaz4444@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
