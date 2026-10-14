AWS CLOUD-NATIVE CAPSTONE PROJECT
CLOUD SUBMISSION PORTAL
Project Documentation Report
Student Name: Nancy Wangui Kanyingi
Course Name: AWS DEVOPS
Institution: Moringa School
Submission Date: 12/10/2026

1.	Project Overview
The Cloud Submission Portal is a cloud-native web application hosted on Amazon Web Services (AWS). It allows users to submit a name and message through a web interface. Amazon API Gateway receives the request and invokes an AWS Lambda function to proces16
2.	Project Objectives
•  Host a static website using Amazon S3.
•  Receive user submissions through Amazon API Gateway.
•  Process submitted data using AWS Lambda.
•  Monitor application activity using Amazon CloudWatch.
•  Test and document the complete application workflow.
3.	System Architecture
Architecture of the AWS Cloud Submission Portal.
                    User's Web Browser
                                                     |
    Amazon S3
                 |
    Static website files
                 |
    Amazon API Gateway
                 |
    POST /submit
                 |
     AWS Lambda
                 |
    Processes the request and returns a reference ID
              |
    Amazon CloudWatch
              |
    Logs and monitoring metrics

4.	AWS Services Used

                
Amazon S3	Hosts the website files.

Amazon API Gateway	Receives HTTP POST requests.
AWS Lambda	Processes requests and generates a reference ID.
Amazon CloudWatch Logs	Stores execution log entries.
Amazon CloudWatch Dashboard	Displays invocation, duration, and error metrics.





