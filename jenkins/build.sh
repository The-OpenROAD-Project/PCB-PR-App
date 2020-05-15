git submodule update --init --recursive
docker build -t pcbprapp .
docker run -v $(pwd):/PCB-PR-App pcbprapp bash -c "./PCB-PR-App/jenkins/install.sh"
