## Run tests

* setup virtualenv

```bash
python3 -m venv .venv
source./.venv/bin/activate
```

* install requirements
```bash
pip install -r requirements.txt
```
* run tests
```bash
tox # run test matrix
tox -e ansible29-centos7 # Specify test
# Or via molecule
MOLECULE_DISTRO=centos7 molecule test
```

## Run tests with pyenv with specific python and pypy

```shell
pyenv install 3.10.2
pyenv local 3.10.2
pip install -r requirements-dev.txt
tox -e py310-centos7
```
