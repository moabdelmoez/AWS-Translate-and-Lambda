import json
import logging
import boto3
import os

def lambda_handler(event, context):
    translate = boto3.client(service_name='translate', region_name='eu-west-1', use_ssl=True)
    
    try:
        review_id = event["queryStringParameters"]['review_id']
    except:
        review_id = "1"
    
    try:
        source_language = event["queryStringParameters"]['source_language']
    except:
        source_language = 'auto'
        
    try:
        target_language = event["queryStringParameters"]['target_language']
    except:
        target_language = 'it'
    
    try:
        review = event["queryStringParameters"]['review']
    except:
        review = "My name is Mostafa"
    
    result = translate.translate_text(
        Text=review, 
        SourceLanguageCode=source_language, 
        TargetLanguageCode=target_language
        )
    
    return{
        'statusCode': 200,
        'body': json.dumps(result.get('TranslatedText'))
    }
    
        
