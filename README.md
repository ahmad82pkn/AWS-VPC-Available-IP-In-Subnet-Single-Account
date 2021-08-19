This Code will help monitor number of free ip in each subnet across single account/multiple region/vpc and alert if they decrease below specified threshold.

####INSTRUCTIONS#####

Please follow steps to update the code as per your account numbers/arn info at specified locations.

1- In Lambda python code regionlist add all regions where you want this scan to happen

2- Create or use existing SNS topic that can send you emails. And In Lambda python code replace SNS Topic ARN topicArn = 'arn:aws:sns:REGION:ACCOUNT NUMBER:NotifyMe'

3- Create a Lambda Role with following permission and name it something like available-ip-single-account

	{ 
	"Version": "2012-10-17",

	"Statement": 
	[

	{
		"Effect": "Allow",
		"Action": ["ec2:DescribeSubnets"],
		"Resource": "*"
	},

	{
		"Effect": "Allow",
		"Sid": "LambdaBasicExecution",
		"Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
		"Resource": "*"
	},
	{
		"Sid": "AllowPublishToMyTopic",
		"Effect": "Allow",
		"Action": "sns:Publish",
		"Resource": "arn:aws:sns:REGION:ACCOUNT NUMBER:NotifyMe" ---> Refer to correct SNS topic ARN
	}
	]
	}

4- Go to your Lambda Function Config in AWS console and change execution role name to the role name created at step 3 and test.

5- Add cloudwatch Event Cronjob to schedule lambda execution as per your required frequency Per hour/Per day etc
