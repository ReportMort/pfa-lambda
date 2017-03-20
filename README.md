# lambda-testpfa
A repository containing test of running PFA scoring on AWS Lambda

## Description
This is the simplest possible example of utilizing the Python package 
[titus](https://github.com/opendatagroup/hadrian) that provides 
a scoring engine for the Portable Format for Analytics. If you would 
like to utilize, then make a copy of this project, keep all of the dependency 
folders of this repository and modify the .py 
file in the root of the project to contain your Lambda logic. 

## Module building
This module was created by following the instructions on AWS: 
http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

Simply by creating the folder, then running the following command 
to install the dependencies in the project folder.

```
cd lambda-testpfa
pip install titus -t .
```
