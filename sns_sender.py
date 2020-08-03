#!/usr/local/bin/python3

import sys
import re
import boto3

def sns_away(number,msg):
    ''' Sends a SMS msg to the (US based) number via AWS SNS '''
    sns = boto3.client('sns')
    # Input validation check
    num = re.search(r'\+1(\d){10}', number)
    if type(msg) is str and len(msg) < 401:
        sns.publish(PhoneNumber = num[0], Message=msg)
    else:
        print('Error: String too long or wrong type')
        sys.exit(1)

if __name__ == '__main__':
    pass
