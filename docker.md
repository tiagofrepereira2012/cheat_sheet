# Setup docker to debug Bob packages

```base
docker run -it docker.idiap.ch/bob/docker-images/c3i-linux-64 /bin/bash
curl --silent https://raw.githubusercontent.com/tiagofrepereira2012/cheat_sheet/main/bootstrap.py --output "bootstrap.py"
python3 bootstrap.py -vv channel base
