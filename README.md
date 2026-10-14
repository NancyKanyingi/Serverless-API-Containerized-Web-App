# AWS Cloud-Native Capstone Project

A containerized web application deployed on Amazon ECS with AWS Fargate, supported by a serverless API built with AWS Lambda and API Gateway.

## Project Overview

This project demonstrates how to deploy and monitor a web application using AWS cloud-native services.

## AWS Services

- **Amazon ECS:** Orchestrates the website container.
- **AWS Fargate:** Runs containers without managing servers.
- **Amazon ECR:** Stores the Docker image.
- **AWS Lambda:** Processes JSON submissions and generates reference IDs.
- **Amazon API Gateway:** Provides the HTTP API endpoint when configured.
- **Amazon CloudWatch:** Collects container logs for monitoring.
- **AWS CloudFormation:** Defines the website infrastructure.
- **Amazon VPC:** Provides the network for the ECS service.

## Project Structure

```text
aws-cloud-native-capstone/
├── lambda-api/
│   └── app.py
├── webapp/
│   ├── Dockerfile
│   ├── app.js
│   └── index.html
├── Screenshots/
├── infrastructure.yml
├── AWS-Capstone-Report.docx
├── AWS-Capstone-Report.md
├── .gitignore
└── README.md
Application Behavior
The Lambda handler accepts JSON submissions, handles CORS preflight requests, and returns a generated reference ID when a submission is accepted.
Invalid JSON returns an HTTP 400 response.
Deployment
1. Build the website Docker image using the Dockerfile in webapp/.
2. Push the image to an Amazon ECR repository.
3. Deploy infrastructure.yml through AWS CloudFormation.
4. Provide the container image URI, VPC ID, and two public subnet IDs as stack parameters.
5. Configure API Gateway to invoke the Lambda function if it has not already been configured.
6. Test the website and API, then review logs in CloudWatch.
Ensure that your AWS account, region, networking, IAM permissions, and image URI are configured correctly before deployment.
Screenshots
The Screenshots/ folder contains evidence of the application, API tests, ECS website, and CloudWatch monitoring.
Security Notes
- Never commit AWS access keys, passwords, private keys, or other secrets.
- Review source code and configuration files before publishing.
- Use HTTPS and appropriate access controls for production deployments.
Author
Moringa School Capstone Project
