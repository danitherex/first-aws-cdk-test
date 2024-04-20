#!/usr/bin/env python3

import aws_cdk as cdk

from first_cdk_test.first_cdk_test_stack import FirstCdkTestStack


app = cdk.App()
FirstCdkTestStack(app, "FirstCdkTestStack")

app.synth()
