<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/docker-upload-and-build.svg?maxAge=3600)](https://pypi.org/project/docker-upload-and-build/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/docker-upload-and-build.svg?branch=master)](https://travis-ci.org/andrewp-as-is/docker-upload-and-build/)

#### Installation
```bash
$ [sudo] pip install docker-upload-and-build
```

#### Pros
+   upload sources to server and build docker image with one command
+   no need docker hub and docker desktop

#### Features
+   `.dockerignore` as rsync `exclude-from` file (optional)

#### Scripts usage
command|`usage`
-|-
`docker-upload-and-build` |`usage: docker-upload-and-build user@hostname name path`

#### Examples
```bash
docker-upload-and-build user@hostname tag .
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>