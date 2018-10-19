#!/bin/bash

apt-get update -q

apt-get install -qy \
    sudo \
    software-properties-common \
    bzip2 \
    gnupg2 \
    apt-utils \
    apt-transport-https \
    lsb-release \
    ca-certificates \
    make \
    gcc \
    wget \
    curl \
    vim \
    git \
    tar \
    unzip \
    nginx \
    tzdata \
    supervisor \
    libcurl4-openssl-dev \
    pkg-config \
    libsasl2-dev \
    libglib2.0-dev
