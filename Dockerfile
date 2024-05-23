FROM ubuntu:24.04

LABEL maintainer="ozan.tokatli@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

# Change shell to bash
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y \
    python3-pip xvfb && \
    rm -rf /var/lib/apt/lists/*

RUN rm -rf /usr/lib/python3.12/EXTERNALLY-MANAGED && \
    python3 -m pip install numpy scipy matplotlib jupyterlab scikit-learn pandas mujoco pyKinovaGen3