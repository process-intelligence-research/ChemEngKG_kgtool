# KG-tool: Python package for accessing the Chemical Engineering Knowledge Graph (ChemEngKG)

<div align="center">

[![Build status](https://github.com/process-intelligence-research/ChemEngKG_kgtool/workflows/build/badge.svg?branch=master&event=push)](https://github.com/process-intelligence-research/ChemEngKG_kgtool/actions?query=workflow%3Abuild)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/process-intelligence-research/ChemEngKG_kgtool/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/process-intelligence-research/ChemEngKG_kgtool/releases)
[![License](https://img.shields.io/github/license/process-intelligence-research/ChemEngKG_kgtool)](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

</div>

## Quick Start

[Here! ](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/quick-start.md)


## 🚀 Features

### Development features

- Supports for `Python 3.9` and higher.
- [`Poetry`](https://python-poetry.org/) as the dependencies manager. See configuration in [`pyproject.toml`](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/pyproject.toml) and [`setup.cfg`](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/setup.cfg).
- Automatic codestyle with [`black`](https://github.com/psf/black), [`isort`](https://github.com/timothycrosley/isort) and [`pyupgrade`](https://github.com/asottile/pyupgrade).
- Ready-to-use [`pre-commit`](https://pre-commit.com/) hooks with code-formatting.
- Type checks with [`mypy`](https://mypy.readthedocs.io); docstring checks with [`darglint`](https://github.com/terrencepreilly/darglint); security checks with [`safety`](https://github.com/pyupio/safety) and [`bandit`](https://github.com/PyCQA/bandit)
- Testing with [`pytest`](https://docs.pytest.org/en/latest/).


### Deployment features

- `GitHub` integration: issue and pr templates.
- `Github Actions` with predefined [build workflow](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/.github/workflows/build.yml) as the default CI/CD.
- Everything is already set up for security checks, codestyle checks, code formatting, testing, linting, docker builds, etc with [`Makefile`](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/Makefile#L89). More details in [makefile-usage](#makefile-usage).
- [Dockerfile](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/docker/Dockerfile) for your package.
- Always up-to-date dependencies with [`@dependabot`](https://dependabot.com/). You will only [enable it](https://docs.github.com/en/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates).
- Automatic drafts of new releases with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). You may see the list of labels in [`release-drafter.yml`](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/.github/release-drafter.yml). Works perfectly with [Semantic Versions](https://semver.org/) specification.

### Open source community features

- Ready-to-use [Pull Requests templates](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/.github/PULL_REQUEST_TEMPLATE.md) and several [Issue templates](https://github.com/process-intelligence-research/ChemEngKG_kgtool/tree/main/.github/ISSUE_TEMPLATE).
- Files such as: `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md` are generated automatically.
- [`Stale bot`](https://github.com/apps/stale) that closes abandoned issues after a period of inactivity. (You will only [need to setup free plan](https://github.com/marketplace/stale)). Configuration is [here](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/.github/.stale.yml).
- [Semantic Versions](https://semver.org/) specification with [`Release Drafter`](https://github.com/marketplace/actions/release-drafter).

## Installation and Documentation
### 1. Install package

```bash
pip install git+https://github.com/process-intelligence-research/ChemEngKG_kgtool
```

Then you can run

```bash
kgtool --help
```

or with `Poetry`:

```bash
poetry run kgtool --help
```

### 2. Import package and setup interface

Import the package to your python project with

```python
from kgtool.interface import *
```

and setup a connection to the ChemEngKG with

```python
chemkg = ChemKG(url="api_url", graph="graph_name")
```

where `api_url` is the url of the ChemEngKG GraphQL-API and `graph_name` is the name of the default graph you want to access.
You can also use 

```python
chemkg_dev = ChemKG.dev()
```

for development purposes. This will connect to a local instance of the ChemEngKG, thus make sure to have the ChemEngKG running locally (see [ChemEngKG_backend repository](https://github.com/process-intelligence-research/ChemEngKG_backend) for further guidance).

### 3. Documentation

#### Return format

The interface provides a set of funcitonalities which can be accessed via the `ChemKG` class. 
Since the interface always interacts with the ChemEngKG via GraphQL the resonse is always a dictionary of the following form:

```json
{
  "data": {
    "function_name": {
      ...
    }
  }
}
```

or 

```json
{
  "errors": [
    ...
  ]
}
```

if an error occured in the backend.


<details>
<summary>FILL IN EXAMPLE</summary>
<p>
</p>
</details>

#### Functionalities
The following list gives an overview of the available functionalities:

<details>
<summary>getGraphs</summary>
<p>

  ```python
  chemkg.getGraphs()
  ```

  Retrieve the URI of all available graphs in the ChemEngKG.

  **Returns:**
  ```json
  {"data": {
    "getGraphs": {
      "graphs":[...]
      }
    }
  }
  ```
  The `graphs` field contains a list of strings which are the URIs of the available graphs.

  **Note:**
  URI is the unique resource identifier of a graph. It is not the same as the graph name which is used to define the interfaces graph (`chemkg.graph`).
</p>
</details>

<details>
<summary>getGraph</summary>
<p>

  ```python
  chemkg.getGraph()
  ```

  Retrieve the contents of a the graph defined in `chemkg.graph` as turtle string.

  **Returns:**
  ```json
  {"data": {
    "getGraph": {
      "contents": ...
      }
    }
  }
  ```
  The `contents` field contains a string which is the turtle representation of the graph in `chemkg.graph`.
</p>
</details>

<details>
<summary>runSparql</summary>
<p>

  ```python
  chemkg.runSparql(query)
  ```
  Runs a SPARQL query on the graph defined in `chemkg.graph` and returns the response.
  
  **Inputs:**
  - `query`: SPARQL query string

  **Returns:**
  ```json
  {"data": {
    "runSparql": {
      "response":
      }
    }
  }
  ```
  The response field contains the response of the SPARQL query. Since it can look very different depending on the query here is a small example:
  <details>
  <summary>runSparql Example</summary>
  <p>
    For a query like 

    ```sparql
    SELECT ?s ?p ?o
    WHERE {
      ?s ?p ?o
    }
    ```
    
    the respnse would look like this:
    ```json
    {"data": {
      "runSparql": {
        "response": {
          "head": {
            "link": [],
            "vars": ["s", "p", "o"]
          },
          "results": {
            "distinct": False,
            "ordered": True,
            "bindings": [{
              "s": {
                "type": "uri",
                "value": "http://www.openlinksw.com/virtrdf-data-formats#default-iid"
              },
              "p": {
                "type": "uri", 
                "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
              },
              "o": {
                "type": "uri",
                "value": "http://www.openlinksw.com/schemas/virtrdf#QuadMapFormat"
              }
            }]
          }
        }
      }
    }}
    ```
  </p>
  </details>
</p>
</details>

<details>
<summary>uploadFile</summary>
<p>
  
  ```python
  chemkg.uploadFile(file_path, URI)
  ```
  Uploads a file to the ChemEngKG. The file is attached to the object defined by `URI`.
  
  **Inputs**:
  - `file_path`: path to the file to be uploaded
  - `URI`: URI of the object in the graph to which the file should be attached.

  **Returns**:

  ```json
  {"data": {
    "uploadFile": {
      "fileName": ...,
      "subjectURI": ...,
      "predicate": ...,
      "fileURI": ...,
      "hashURI": ...
    }
  }}
  ```
 - `fileName`: name the uploaded file is stored under in the ChemEngKG filestorage. You can use this name to download the file sending a request to `<filestorageURL>/uploads/<fileName>`.
  - `subjectURI`: URI of the object in the graph to which the file is attached.
  - `predicate`: predicate of the triple which connects the object to the file. This should either be `frbr:exemplar` or `frbr:part`.
  - `fileURI`: URI of the file node in the graph.
  - `hashURI`: URI of the hash node in the graph.

</p>
</details>

<details>
<summary>deleteFile</summary>
<p>
  
  ```python
  chemkg.deleteFile(fileURI)
  ```
  Deletes a file from the ChemEngKG filestorage and removes all afiliated triples in the graph. The file is identified by its URI.
  
  **Inputs**:
  - `fileURI`: URI of the file to be deleted

  **Returns**:
  ```json
  {"data": {
    "deleteFile": {
      ... FILL IN
      }
    }
  }
  ```

### Makefile usage (for Maintainer)

[`Makefile`](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/process-intelligence-research/kgtool/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/process-intelligence-research/ChemEngKG_kgtool/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![LICENSE](https://img.shields.io/github/license/process-intelligence-research/ChemEngKG_kgtool)](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/process-intelligence-research/ChemEngKG_kgtool/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{kgtool,
  author = {Kleinpaß, Marvin and Kondakov, Valentin and Gao, Qinghe and Schulze Balhorn, Lukas and Schweidtmann, Artur M.},
  title = {KG-tool: Python package for accessing the Chemical Engineering Knowledge Graph (ChemEngKG)},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/process-intelligence-research/ChemEngKG_kgtool}}
}
```
