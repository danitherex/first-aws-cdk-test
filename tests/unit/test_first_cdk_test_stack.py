import aws_cdk as core
import aws_cdk.assertions as assertions
from first_cdk_test.first_cdk_test_stack import FirstCdkTestStack


def test_sqs_queue_created():
    app = core.App()
    stack = FirstCdkTestStack(app, "first-cdk-test")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })
