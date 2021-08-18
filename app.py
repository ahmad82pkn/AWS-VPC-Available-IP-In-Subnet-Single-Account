import json
import boto3



def lambda_handler(event, context):
        regionlist=['ap-southeast-2','us-east-1']  # --> Change Number 1
        notification = ""
        for region in regionlist:
            ec2 = boto3.client('ec2',region_name=region)
            output_describe_subnets = ec2.describe_subnets( Filters=[{'Name': 'state', 'Values': ['available']}])
            print(output_describe_subnets)

            for eachsubnet in output_describe_subnets['Subnets']:
                message = "Available IP's in Account Number: %s , Region: %s, VPC ID: %s , Subnet: %s is approaching ciritcal limit of %d" % (eachsubnet['OwnerId'],region,eachsubnet['VpcId'],eachsubnet['SubnetId'], eachsubnet['AvailableIpAddressCount'])
                if eachsubnet['AvailableIpAddressCount']<10: # Feel free to change this number from 10 to any number on which you want to be alerted
                    print(message)
                    notification = notification+"\n"+message

        if notification:
            sns = boto3.client('sns')
            topicArn = 'arn:aws:sns:REGION:ACCOUNT NUMBER:NotifyMe'  # --> Change Number 2
            sns.publish(
                TopicArn = topicArn,
                Message = notification
            )
