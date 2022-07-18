from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tb_theme/__init__.py
from tb_theme import __version__ as version

setup(
	name="tb_theme",
	version=version,
	description="Techno Builders Theme",
	author="Techno Builders",
	author_email="techno-builders.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
