# Setup docker to debug Bob packages

```base
docker run -it docker.idiap.ch/bob/docker-images/c3i-linux-64 /bin/bash
curl --silent https://gitlab.idiap.ch/tiago.pereira/cheat-sheet/-/raw/master/bootstrap.py --output "bootstrap.py"
python3 bootstrap.py -vv channel base
