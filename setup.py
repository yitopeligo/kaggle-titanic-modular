from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['sklearn', 'pandas', 'matplotlib', 'numpy', 'statsmodels', 'patsy']

setup(
    name='trainer',
    version='0.3',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description='Custom MLOps package.'
)