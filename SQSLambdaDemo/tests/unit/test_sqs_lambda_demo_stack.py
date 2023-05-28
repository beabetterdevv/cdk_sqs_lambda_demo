import json
import pytest

from aws_cdk import core
from sqs_lambda_demo.sqs_lambda_demo_stack import SqsLambdaDemoStack


def get_template():
    app = core.App()
    SqsLambdaDemoStack(app, "sqs-lambda-demo")
    return json.dumps(app.synth().get_stack("sqs-lambda-demo").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
