FROM ubuntu:18.04

ARG USER_ID
ARG GROUP_ID
COPY ./basic_dependencies.sh /
RUN ./basic_dependencies.sh
RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user



