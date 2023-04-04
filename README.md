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

## Installation (for Users)

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
