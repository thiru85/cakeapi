import sys
import boto3
import os
import json
import warnings
import random
from flask import Flask
import socket
from boto3.dynamodb.conditions import Key, Attr

app = Flask(__name__)

@app.route("/")
def cake_api():

    query_list=[]
    for item in response['Items']:
        query_list.append(item)
    output=query_list[random.randint(0,len(response))]

    return {
        "id": output["cakeID"],
        "cakeName": output["cakeName"],
        "cakeSize": output["cakeSize"],
        "containerID": socket.gethostname()
    }


warnings.filterwarnings('ignore', category=FutureWarning, module='botocore.client')

dynamodbobj = boto3.resource("dynamodb", )
table = dynamodbobj.Table(os.environ.get('TABLENAME'))
response = table.scan()

app.run(host='0.0.0.0', port='80')

# this is a comment