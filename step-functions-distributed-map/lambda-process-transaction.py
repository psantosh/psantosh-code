import json

print('Loading function')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    output = "transactionId = " + event['transactionId'] + " type = " + event['type'] + " amount = " + event['amount']
    print(output)
    return output
