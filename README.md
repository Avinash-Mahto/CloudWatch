# AWS CloudWatch Agent Installation on Ubuntu

This guide provides step-by-step instructions to install and configure the AWS CloudWatch Agent on an Ubuntu EC2 instance. The CloudWatch Agent enables you to collect and monitor system metrics and logs, which can be sent to Amazon CloudWatch for analysis.

## Prerequisites

Before you begin, ensure the following:

- You have an Ubuntu EC2 instance running.
- AWS CLI is installed and configured on your instance.
- The instance has the necessary IAM role with permissions to write to CloudWatch Logs and Metrics.

## 1. Update System Packages
   ```bashsudo apt-get update
```

Update the package lists on your Ubuntu system to ensure you have the latest versions:

## 2. Download the CloudWatch Agent Package
   ```bashwget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb```

## 3. Install the CloudWatch Agent
```bash sudo dpkg -i amazon-cloudwatch-agent.deb
```

## 4. Configure the CloudWatch Agent
```bash vi /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json
```

## Start the CloudWatch Agent
```bash sudo systemctl start amazon-cloudwatch-agent
```

## 5. Enable the CloudWatch Agent to Start on Boot
```bash sudo systemctl enable amazon-cloudwatch-agent
```

## 6. Verify the CloudWatch Agent is Running
```bash sudo systemctl status amazon-cloudwatch-agent
```

## 7. Validate the Configuration File
```bash sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json -s
```

