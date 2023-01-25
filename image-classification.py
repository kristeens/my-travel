# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:18:14 2023

@author: Koky
"""

import boto3
import json
import base64

ENDPOINT = 'image-classification-2023-01-23-14-01-28-082'
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event["image_data"])
    
    # Instantiate a Predictor
    predictor = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                       ContentType='image/png',
                                       Body=image)

    # Make a prediction:
    inferences = json.loads(predictor['Body'].read().decode())

    # We return the data back to the Step Function    
    event["inferences"] = inferences
    #print(inferences)
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }