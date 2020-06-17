docker run -u $(id -u ${USER}):$(id -g ${USER}) -v $(pwd):/PCB-PR-App pcbprapp bash -c "cd PCB-PR-App;./ubuntu_install.sh; ./tests/regression-py.sh"
