
"""
    Public Interface to be used by the ppl who want to use the Databases
"""

import requests
import json
import base64
import os


url = "http://localhost:4001/graphql"
headers = { 'Content-Type': 'application/json' }

def run_query(query): 
    return run({'query': query})    
    
def run(payload):
    request = requests.post(url, json=payload, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))        


def prepareFile(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read())
    
#
def uploadFile(filePath, DOI):
    encoded_string = prepareFile(filePath)
    root, ext = os.path.splitext(filePath)
    mimeType = ext 
    fn = f'uploadFile(file:"{encoded_string}",mimetype: "{mimeType}", doi: "{DOI}")'
    run_query("mutation {" + fn + "}" )
 
#        
def uploadTurtle(filePath):
    encoded_string = prepareFile(filePath)
    
# only supported by Neo4j atm
def fullGraph():
    return run_query("{ fullGraph }")

def connect(options):
    
    return 0

