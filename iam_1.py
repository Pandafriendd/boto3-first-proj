import boto3

client = boto3.client('iam')

def list_p(): 
    response = client.list_policies()
    print(response) 

list_p() 