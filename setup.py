from setuptools import find_packages, setup

setup(
    name='binary',
    version='0.3.0',
    license='BSD',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=['click', 'requests', 'pytest','tox'],
    entry_points={
        'console_scripts': [
            'binary = binary.binary:cli',
        ],
    },
)
