import json
import pytest

from aws_cdk import core
from datalake_access_management.datalake_access_management_stack import DatalakeAccessManagementStack


def get_template():
    app = core.App()
    DatalakeAccessManagementStack(app, "datalake-access-management")
    return json.dumps(app.synth().get_stack("datalake-access-management").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
