"""
    Public Interface to be used by the ppl who want to use the Databases
"""

import base64
import json
import os

import requests

url = "http://localhost:4001/graphql"
headers = {"Content-Type": "application/json"}


def run_query(query):
    return run({"query": query})


def run(payload):
    request = requests.post(url, json=payload, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            f"Query failed to run by returning code of {request.status_code}. {payload}"
        )


def prepareFile(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read())


#
def uploadFile(filePath, DOI):
    encoded_string = prepareFile(filePath).decode("utf-8")
    root, ext = os.path.splitext(filePath)
    fn = f'uploadFile(file:"{encoded_string}",ext: "{ext}", doi: "{DOI}")'
    run_query("mutation {" + fn + "}")


#
def uploadTurtle(filePath):
    with open(filePath) as f:
        encoded_string = base64.b64encode(f.read().encode("utf-8")).decode("utf-8")
        fn = f'uploadTurtle(file:"{encoded_string}")'
        run_query("mutation {" + fn + "}")


# only supported by Neo4j atm
def fullGraph():
    return run_query("{ fullGraph }")


def connect(options):

    return 0
