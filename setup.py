from setuptools import setup, find_packages

setup(
    name='xpdsim',
    version='1.0.2',
    packages=find_packages(),
    description='simulators',
    zip_safe=False,
    package_data={'xpdsim.data': ['XPD/ni/*.tif*']},
    include_package_data=True,
    url='https://github.com/xpdAcq/xpdSim'
)
