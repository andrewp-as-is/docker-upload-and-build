from setuptools import setup

setup(
    name='docker-upload-and-build',
    version='2020.5.27',
    install_requires=[
        'setuptools',
    ],
    scripts=[
        'scripts/docker-upload-and-build',
    ],
)
