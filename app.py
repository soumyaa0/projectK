import boto3
client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-0dee22c13ea7a9a67',
    InstanceType='t2.micro',
    KeyName = 'projectK',
    MaxCount = 1,
    MinCount = 1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Boto3-py'  # Replace with your desired instance name..!!
                }
            ]
        }
    ]
)

