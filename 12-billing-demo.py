# Uses AWS Cost Explorer to query cost and usage

import boto3

ce = boto3.client('ce')

response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2025-08-01',
        'End': '2025-08-21'
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost']
)

# Print the cost and usage results for the selected period
print(response['ResultsByTime'])