This Code will help monitor number of free ip in each subnet across single account/multiple region/vpc and alert if they decrease below specified threshold.

####INSTRUCTIONS#####

Please follow steps to update the code as per your account numbers/arn info at specified locations.


1- In regionlist add all regions where you want this scan to happen

2- Replace SNS Topic ARN  topicArn = 'arn:aws:sns:REGION:ACCOUNT NUMBER:NotifyMe'

3- Go to your Lambda Function Config in AWS console and change execution rolename to "basic-lambda-execution-role"

4- Add cloudwatch Event Cronjob to schedule lambda execution as per your required frequency Per hour/Per day etc

