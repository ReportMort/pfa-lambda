# pfa-lambda
A template for executing PFA on AWS Lambda to create a serverless, scalable analytical API.

## Getting Started Quickly
If you want to test running PFA on AWS Lambda, clone this project, then zip it 
and upload to the AWS Console.

```
git clone git@github.com:ReportMort/pfa-lambda.git
zip -r my-lambda-deploy.zip .
```

If you test this package in the AWS console, it should return `103.14` the result 
of our function which is hard-coded to accept `3.14` and then apply a PFA routine 
that adds `100` to return `103.14`. You can use the AWS Hello World testing template 
which provides 3 dummy key-value pairs, but no key-values are required.

## A More Realistic Example 

In the script `lambda_function.py` a simple PFA routine is supplied directly as 
hand-writter, hard-coded text. Many machine learning models are complex algorithms 
that would not be hard-coded text. The model would be created and translated to 
PFA using a producer so that the logic would be saved in a separate file. Your 
model could be saved in an S3 bucket (with versioning) and called. For an example, 
check out `model-from-s3.py`. If you want to use this function, make sure to update 
the handler on AWS to be `model-from-s3.py.lambda_handler` and replace the bucket 
and key with the bucket and filename of your model on S3. This function depends on 
the `event` JSON input, therefore, the key-values for each model predictor variable 
must be provided and are directly paseed into the PFA engine to produce the score.

## Troubleshooting

1. Check the selected Runtime for your lambda is Python 2.7
2. Check the name of the `.py` file in your root directory and ensure that it matches 
the handler specification in the AWS console (i.e. The filename.handler-method value 
in your function.)
3. If you see the message `"errorMessage": "Unable to import module 'lambda_function'"`, 
make sure that the permissions of all files inside your `.zip` package are at least 444. 
The file and directory permissions every file in your deployment package (the .zip file) 
must be readable globally.

## How This Deployment Package Was Made
This deployment package was created by following the instructions on AWS: 
http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

More specifically, by running the following code:

```
mkdir my-pfa-lambda-module
cd my-pfa-lambda-module
pip install titus -t .
```

If you're using OS X and Homebrew you will need to specify a `setup.cfg` file. 
Here are the complete instructions for compiling: 

```
mkdir my-pfa-lambda-module
cd my-pfa-lambda-module
touch setup.cfg
echo "[install]" >> setup.cfg
echo "prefix=" >> setup.cfg
pip install titus -t .
```
