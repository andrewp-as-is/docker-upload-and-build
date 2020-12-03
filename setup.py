import setuptools

setuptools.setup(
    name='docker-upload-and-build',
    version='2020.12.3',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/docker-upload-and-build']
)
