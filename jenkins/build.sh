git submodule update --init --recursive
docker build -t pcbprapp \
  --no-cache \
  --build-arg USER_ID=$(id -u) \
  --build-arg GROUP_ID=$(id -g) .
docker run -u $(id -u ${USER}):$(id -g ${USER}) -v $(pwd):/PCB-PR-App pcbprapp bash -c "./PCB-PR-App/jenkins/install.sh"
