FROM ubuntu:16.04

LABEL version="1.0"
LABEL maintainer="shindu666@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install --yes software-properties-common
RUN add-apt-repository ppa:ethereum/ethereum
RUN apt-get update && apt-get install --yes geth

RUN adduser --disabled-login --gecos "" eth_user

USER eth_user
WORKDIR /home/eth_user


#--testnet
CMD ["geth", "--rpc", "-rpcport","8545", "--rpcaddr","0.0.0.0","--rpccorsdomain","*","--fast","--cache","512"]
