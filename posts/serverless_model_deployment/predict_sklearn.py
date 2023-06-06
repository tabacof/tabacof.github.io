import json
import cloudpickle

# By loading the pickle outside `predict`,
# we re-use it across different Lambda calls for the same execution instance
with open('model.pickle', 'rb') as f:
    model = cloudpickle.load(f)

def api_return(body, status):
    return {
        'isBase64Encoded': False,
        'statusCode': status,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body, default=str)
    }

def predict(event, context):
    if isinstance(event['body'], str):
        try:
            payload = json.loads(event['body'])
        except json.JSONDecodeError:
            return api_return({'error': 'JSON decode error when decoding payload'}, 400)
    elif isinstance(event['body'], list):
        payload = event['body']
    else:
        return api_return({'error': 'Unknown input format'}, 400)

    # Scikit-learn needs a list or array as input
    if not isinstance(payload, list):
        payload = [payload]

    try:
        output = model.predict(payload).tolist()
    except Exception as e:
        return api_return({'error': str(e)}, 500)

    return api_return(output, 200)
