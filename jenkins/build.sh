git submodule update --init --recursive
docker run -v $(pwd):/PCB-PR-App ubuntu:18.04 bash -c "./PCB-PR-App/jenkins/install.sh"
