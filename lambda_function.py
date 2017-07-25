from __future__ import print_function

import json
from titus.genpy import PFAEngine

print('Loading function')

def lambda_handler(event, context):

    engine, = PFAEngine.fromJson('''
    {"input": "double",
    "output": "double",
    "action": {"+": ["input", 100]}}
    ''')
    
    return engine.action(3.14)
