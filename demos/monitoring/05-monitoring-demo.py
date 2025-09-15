# Demonstrates creating a custom metric and alarm in CloudWatch

import boto3

cloudwatch = boto3.client('cloudwatch')

def put_metric():
    # Put a custom metric data point into CloudWatch
    cloudwatch.put_metric_data(
        Namespace='DemoNamespace',
        MetricData=[
            {
                'MetricName': 'DemoMetric',
                'Value': 1,
                'Unit': 'Count'
            }
        ]
    )

def create_alarm():
    # Create a CloudWatch alarm based on the custom metric
    cloudwatch.put_metric_alarm(
        AlarmName='DemoAlarm',
        MetricName='DemoMetric',
        Namespace='DemoNamespace',
        Statistic='Sum',
        Period=60,
        EvaluationPeriods=1,
        Threshold=1,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        ActionsEnabled=False
    )

if __name__ == '__main__':
    put_metric()
    create_alarm()