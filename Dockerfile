# docker pull zceq-solver-buildenv

FROM debian:sid

MAINTAINER Ondrej Sika <ondrej@ondrejsika.com>

RUN apt-get update \
    #&& apt-get install -y gcc-6 g++-6 make cmake \
    && apt-get install -y gcc-8 g++-8 make cmake \
    #&& apt-get install -y llvm-3.9 clang-3.9 \
    && apt-get install -y llvm-6.0 clang-6.0 \
    && apt-get install -y mingw-w64 scons virtualenv \
    && apt-get install -y build-essential libssl-dev libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    #&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 999 \h
    #&& update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 999 \
    #&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.9 999 \
    #&& update-alternatives --install /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-3.9 999
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 999 \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 999 \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-6.0 999 \
    && update-alternatives --install /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-6.0 999
