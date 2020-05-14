docker run -v $(pwd):/PCB-PR-App ubuntu:18.04 bash -c "cd PCB-PR-App;./ubuntu_install.sh; ./tests/regression-py.sh"
