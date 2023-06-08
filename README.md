# Function

myGlobal_IP_check function for lambda<br />

## Overview

A Lambda function that displays the Global IP of the access source.<br />

## Archtecture

In order for the service to function and serve in the real world, it is necessary to properly configure the AWS provided WAF/API gateway (with Cognito authentication if necessary) and design the overall architecture with security in mind. If you need an https session, you need to additionally build an environment for SSL processing on AWS (using ACM and ALB, for example).<br />

ACM - AWS Certificate Manager<br />
ALB - Application Load Balancer<br />
WAF - Provides access security.<br />
API Gateway - Provides an internal interface to execute Lambda functions.<br />
Lambda-The core engine that executes this code.<br />
cloudwatch -The execution result is logged.<br />
  *Keep in mind that Cloudwatch does not store logs for long periods of time. <br />

<br />
<img src = './images/Architecture diagram-cw.png' align=left>
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />

## Usage (execution of function)

http(s)://api endpoint address/<br />

## Result json sample

When you access it with a web browser,<br />
the access source Global IPv4 Address and the access date and time are displayed in json format.<br />

{"statusCode":"200", "urGlobalIPv4": "xxx.xxx.xxx.xxx", "accessDate": "isoformat(UTC)"} <br />

Please understand that this is not a perfect method.
This is just one example.
