"""Setup script for object_detection."""

from setuptools import setup
from setuptools import find_packages

REQUIRED_PACKAGES = ['Pillow>=1.0']

setup(
    name='object_detection',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('object_detection')],
    description='Tensorflow Object Detection Library',
)


setup(
    name='slim',
    version='0.1',
    install_requires=REQUIRED_PACKAGES,
    include_package_data=True,
    packages=[p for p in find_packages() if p.startswith('slim')],
    description='Tensorflow Object Detection Library',
)
