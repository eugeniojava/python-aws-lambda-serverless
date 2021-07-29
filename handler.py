import json


def hello(event, context):
    try:
        return dict(
            statusCode=200,
            body=json.dumps(event)
        )
    except Exception as exception:
        return dict(
            statusCode=500,
            body=str(exception)
        )
