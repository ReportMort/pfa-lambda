from __future__ import print_function

import json
from titus.genpy import PFAEngine

print('Loading function')

engine, = PFAEngine.fromJson('''
{"input": "double",
"output": "double",
"action": {"+": ["input", 100]}}
''')

def lambda_handler(event, context):

    return engine.action(3.14)
