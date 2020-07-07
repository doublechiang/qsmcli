import os,sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

sys.path.insert(0, (os.path.join(os.path.dirname(__file__),'src')))

import version

setuptools.setup(
    name='qsmcli',  
    version=version.Version(),
    author="Jiang Junyu",
    author_email="double.chiang@gmail.com",
    description="A ipmitool wrapper to enhance daily operation among servers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doublechiang/qsmcli",
    packages=['qsmcli'],
    # package_dir def: key is the name and values is the directory
    # mapping '' root package to a folder. or mapping package to 'src' folder

    package_dir={'qsmcli': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='ipmitool qsm',
    install_requires=['elevate', 'cmd2'],
 )



install_requires=[
'cmd2>=1,<2',
]
