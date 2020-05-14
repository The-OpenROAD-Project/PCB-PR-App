docker build -t pcb-pr-app .
docker run -v $(pwd):/PCB-PR-App pcb-pr-app bash -c "./PCB-PR-App/jenkins/install.sh"
