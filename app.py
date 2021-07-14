#!/usr/bin/env python3

from aws_cdk import core

from datalake_access_management.datalake_access_management_stack import DatalakeAccessManagementStack


app = core.App()
DatalakeAccessManagementStack(app, "datalake-access-management")

app.synth()
