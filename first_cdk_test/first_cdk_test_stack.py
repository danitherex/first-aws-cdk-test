from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_lambda_event_sources as lambda_event_sources
)


class FirstCdkTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create Queue
        queue = sqs.Queue(
            self, "SqsLambdaQueue",
            visibility_timeout=Duration.seconds(300),
        )

        # Create lambda Function
        sqs_lambda = lambda_.Function(
            self, "SqsLambda",
            handler="lambda_handler.handler",
            runtime=lambda_.Runtime.PYTHON_3_12,
            code=lambda_.Code.from_asset("lambda")
            )
        
        # Create Event Source
        sqs_eventSource = lambda_event_sources.SqsEventSource(queue)

        # Add Sqs event source to lambda
        sqs_lambda.add_event_source(sqs_eventSource)
        


