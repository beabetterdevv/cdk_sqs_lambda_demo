#!/usr/bin/env python3

from aws_cdk import core

from sqs_lambda_demo.sqs_lambda_demo_stack import SqsLambdaDemoStack


app = core.App()
SqsLambdaDemoStack(app, "sqs-lambda-demo")

app.synth()
