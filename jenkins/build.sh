#git submodule update --init --recursive # This is now done with a Jenkins config setting
docker build -t pcbprapp .
docker run -v $(pwd):/PCB-PR-App pcbprapp bash -c "./PCB-PR-App/jenkins/install.sh"
