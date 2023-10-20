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
            input = (
                'ext: "'
                + ext
                + '", file: "'
                + encoded_string
                + '", graph: "'
                + self.graph
                + '" , uri: "'
                + URI
                + '"'
            )
            mutation = (
                "mutation { uploadFile(input: {"
                + input
                + "} ) { fileName, subjectURI, predicate, fileURI, hashURI  } }"
            )
            return self._run_query(mutation)

    #
    def deleteFile(self, fileURI):
        """
        Delete a file from the file storage and remove the associated triples from the knowledge graph.
        Atributes
        ---------
        fileURI : str
            The URI of the file to be deleted.
        """
        input = 'fileURI: "' + fileURI + '", graph: "' + self.graph + '"'
        mutation = "mutation { deleteFile(input: {" + input + "} ) { response } }"
        return self._run_query(mutation)

    #
    def uploadTurtle(self, turtle: str):
        """
        Upload a turtle file to the knowledge graph.
        Atributes
        ---------
        turtle : str
            The turtle file to be uploaded. Either a file path or a turtle string.
        """
        if os.path.isfile(turtle):
            # given turtle is a file path -> read file and upload content
            with open(turtle, encoding="utf-8") as f:
                encoded_string = base64.b64encode(f.read().encode("utf-8")).decode(
                    "utf-8"
                )
        else:
            # given turtle is a string -> encode string and upload content
            encoded_string = base64.b64encode(turtle.encode("utf-8")).decode("utf-8")
        input = 'file: "' + encoded_string + '", graph: "' + self.graph + '"'
        mutation = "mutation { uploadTurtle(input: {" + input + "} ) { response } }"
        return self._run_query(mutation)

    #
    def getGraphs(self):
        """
        Retrieve a list of all available graphs.
        """
        return self._run_query("query { getGraphs { graphs }}")

    def getGraph(self):
        input = 'graph: "' + self.graph + '"'
        query = "query { getGraph(input: {" + input + "} ) { contents } }"
        return self._run_query(query)

    def deleteGraph(self):
        """
        Retrieve the contents of self.graph.
        """
        input = f'urn: "urn:graph:{self.graph}"'
        mutation = "mutation { dropGraph(input: {" + input + "} ) { response } }"
        return self._run_query(mutation)

    def runSparql(self, query):
        """
        Run a SPARQL query on the knowledge graph.
        Atributes
        ---------
        query : str
            The SPARQL query to be executed.
        """
        no_new_line = query.replace("\n", " ")
        encodedQuery = base64.b64encode(no_new_line.encode("utf-8")).decode("utf-8")
        input = 'query: "' + encodedQuery + '"'
        mutation = "mutation { runSparql(input: {" + input + "} ) { response } }"
        return self._run_query(mutation)


def connect(options):

    return 0
