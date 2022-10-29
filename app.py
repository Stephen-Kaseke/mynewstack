#!/usr/bin/env python3

import aws_cdk as cdk

from mynewstack.mynewstack_stack import MynewstackStack


app = cdk.App()
MynewstackStack(app, "mynewstack")

app.synth()
