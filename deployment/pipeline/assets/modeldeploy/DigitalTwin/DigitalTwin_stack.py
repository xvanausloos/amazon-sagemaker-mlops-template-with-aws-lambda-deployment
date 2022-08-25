from aws_cdk import Duration, Stack
from aws_cdk import aws_iam as _iam
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_event_sources as _event_sources
from aws_cdk import aws_s3 as _s3
from constructs import Construct

policy = [
    _iam.PolicyStatement(
        actions=[
            "s3:GetObject*",
            "s3:GetBucket*",
            "s3:List*",
            "s3:DeleteObject*",
            "s3:PutObject",
            "s3:Abort*",
        ],
        resources=[
            "arn:aws:s3:::sagemaker-*",
        ],
    ),
]

class DigitalTwinStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Defines an AWS Lambda resource
        _lambda.DockerImageFunction(
            self, 'DigitalTwin',
            code=_lambda.DockerImageCode.from_image_asset("lambda/digital_twin"),
            memory_size=512,
            timeout=Duration.seconds(60),
        )
