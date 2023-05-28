from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_lambda_event_sources as _aws_lambda_event_sources,
    core
)

class SqsLambdaDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Making our SQS Queue
        queue = sqs.Queue(
            self, "SqsLambdaDemoQueue",
            visibility_timeout=core.Duration.seconds(300),
        )

        # Make our Lambda Function
        sqs_lambda = _lambda.Function(self, 'SQSLambdaTrigger',
            handler='lambda_handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.asset('lambda')
        )

        # Make our SQS + Lambda Event source
        sqs_event_source = _aws_lambda_event_sources.SqsEventSource(queue)

        # Add SQS event source to the lambda function
        sqs_lambda.add_event_source(sqs_event_source)

