# AWS CloudWatch Agent Installation on Ubuntu

This guide provides step-by-step instructions to install and configure the AWS CloudWatch Agent on an Ubuntu EC2 instance. The CloudWatch Agent enables you to collect and monitor system metrics and logs, which can be sent to Amazon CloudWatch for analysis.

## Prerequisites

Before you begin, ensure the following:

- You have an Ubuntu EC2 instance running.
- AWS CLI is installed and configured on your instance.
- The instance has the necessary IAM role with permissions to write to CloudWatch Logs and Metrics.

## 1. Update System Packages

Update the package lists on your Ubuntu system to ensure you have the latest versions:

```bash
sudo apt-get update && sudo apt-get upgrade -y

## 2. Install the AWS CloudWatch Agent
