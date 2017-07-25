# pfa-lambda
A template for deploying analytical processed expressed in PFA to AWS Lambda to 
create a serverless, scalable analytical API.

## Using This Template
If you want to run PFA on AWS Lambda, just download this project as ZIP and upload 
the .zip file in the AWS console as a "function package". This project was built to be 
used with Python 2.7.

## Building This AWS Lambda Module
This module was created by following the instructions on AWS: 
http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

More specifically, by first [installing Titus](https://github.com/opendatagroup/hadrian/wiki/Installation#case-4-you-want-to-install-titus-in-python), then running the following code:

```
mkdir my-pfa-lambda-module
cd my-pfa-lambda-module
pip install titus -t .
```

If you've installed titus on OS X using Homebrew you will need to specify a `setup.cfg` file. 
Here are the complete instructions for compiling: 

```
mkdir my-pfa-lambda-module
cd my-pfa-lambda-module
touch setup.cfg
echo "[install]" >> setup.cfg
echo "prefix=" >> setup.cfg
pip install titus -t .
```
