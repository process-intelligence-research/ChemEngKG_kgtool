## Quick Start


1. Installation
2. First Steps
3. Functions
4. Custom Queries

### 1. Installation

`pip3 install git+https://github.com/process-intelligence-research/ChemEngKG_kgtool.git`

in your python file:

```from kgtool.interface import *```

### 2. First Steps

- Init the interface with the default graph

```python
chemKG = ChemKG()
```

- Specify your own Graph by naming it on init


```python
chemKG = ChemKG(graph="GraphDracula")
```


### 3. Functions 

- Upload your RDF Files via:

```python
chemKG.uploadTurtle("/teenage/mutant/ninja.ttl")
```


- Upload your Files via:

```python
chemKG.uploadFile("/path/to/file.ext", "someURI")
```

After upload the generated hash-download-url will be inserted as a Triple in the current Graph.

- get the Triples from the default or specified graph:
  
```python
chemKG.getGraph()
```

- get all graphs

```python
chemKG.getGraphs()
```

- delete your graph with all its triples 

```python
chemKG.deleteGraph()
```


### 4. Custom Queries

- Virtuoso

```python
chemkg.runSparql("SELECT * WHERE { ?s ?p ?o } LIMIT 10")
```
