import json

def lambda_handler(event, context):
    name = event.get('name', 'World')
    message = f'Hello, {name}!'
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        })
    }
