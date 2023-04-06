"""
    Public Interface to be used by the ppl who want to use the Databases
"""

import base64
import json
import os

import requests

dev_url = "http://localhost:4001/graphql"
prod_url = "http://api.chemkg.cloud:4001/graphql"
headers = {"Content-Type": "application/json"}
default_graph = "chemkg"


class ChemKG:
    @classmethod
    def dev(cls):
        return cls(dev_url, default_graph)

    def __init__(self, url=prod_url, graph=default_graph):
        self._url = url
        self.graph = graph

    def __str__(self):
        return f"ChemKG({self._url}, {self.graph})"

    def _run(self, payload):
        request = requests.post(self._url, json=payload, headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception(
                f"Query failed to run by returning code of {request.status_code}. {payload} ::{request.text}"
            )

    def _run_query(self, query):
        return self._run({"query": query})

    def _prepareFile(self, path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read())

    #
    def uploadFile(self, filePath, URI):
        """
        Upload a file to the file storage and add basic triples to the knowledge graph.
        Atributes
        ---------
        filePath : str
            The path to the file to be uploaded.
        URI : str
            The URI of the object the file is associated with.
        Returns
        -------
        dict
            The response from the graphql API. If the upload was successful, the response will contain the URI of the file, the download URL, and information on the created hash object (uri,value,algorithm).
        """
        with open(filePath, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode("utf-8")
            root, ext = os.path.splitext(filePath)
            fn = f'uploadFile(file:"{encoded_string}", ext: "{ext}", uri: "{URI}", graph: "{self.graph}")'
            res = "{ uri downloadURL hash { uri value algorithm } }"
            return self._run_query("mutation {" + fn + res + "}")

    #
    def deleteFile(self, fileURI):
        """
        Delete a file from the file storage and remove the associated triples from the knowledge graph.
        Atributes
        ---------
        fileURI : str
            The URI of the file to be deleted.
        """
        fn = f'deleteFile(fileURI: "{fileURI}", graph: "{self.graph}")'
        return self._run_query("mutation {" + fn + "}")

    #
    def uploadTurtle(self, filePath):
        with open(filePath, encoding="utf-8") as f:
            encoded_string = base64.b64encode(f.read().encode("utf-8")).decode("utf-8")
            fn = f'uploadTurtle(file:"{encoded_string}", graph: "{self.graph}")'
            self._run_query("mutation {" + fn + "}")

    #
    def getGraphs(self):
        return self._run_query("mutation { getGraphs }")

    def getGraph(self):
        return self._run_query('mutation { getGraph(urn: "' + self.graph + '") }')

    def deleteGraph(self):
        return self._run_query('mutation { deleteGraph(urn: "' + self.graph + '") }')

    def runSparql(self, query):
        no_new_line = query.replace("\n", " ")
        encodedQuery = base64.b64encode(no_new_line.encode("utf-8")).decode("utf-8")
        return self._run_query('mutation { runSparql(query: "' + encodedQuery + '") }')


def connect(options):

    return 0
