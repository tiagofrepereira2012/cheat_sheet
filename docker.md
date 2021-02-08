# Setup docker to debug Bob packages

```base
docker run -it docker.idiap.ch/bob/docker-images/c3i-linux-64 /bin/bash
TARGET=bob.buildout
TARGET_REPO=http://gitlab.idiap.ch/bob/$TARGET
curl --silent https://raw.githubusercontent.com/tiagofrepereira2012/cheat_sheet/main/bootstrap.py --output "bootstrap.py"
python3 bootstrap.py -vv channel base
source ./miniconda/etc/profile.d/conda.sh
conda activate base
git clone $TARGET_REPO
cd $TARGET
bdt build -vv .

```

Variables

```base
export CI_JOB_TOKEN=
export CI_PROJECT_DIR=bob
export PYTHON_VERSION=3.8
export CI_COMMIT_REF_NAME=master
export DOCUSER=
export DOCPASS=
export PYPIUSER=
export PYPIPASS=
```
