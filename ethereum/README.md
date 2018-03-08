# docker

- https://gist.github.com/fishbullet/4c36ecd6d6932adae24c68c8750894e6
- https://github.com/ethereum/wiki/wiki/JavaScript-API
- http://web3js.readthedocs.io/en/1.0/index.html





    docker build -t ether_node .
    docker run --rm -it -p 8545:8545 -v /data/ethereum/test:/home/eth_user/.ethereum ether_node

    docker run -d -p 8545:8545 -v /data/ethereum/test:/eth_user/.ethereum ether_node
    geth --rpc --rpcport 8545 --rpcaddr 0.0.0.0 --rpccorsdomain "*" --rpcapi db,eth,net,web3,personal --testnet --fast --cache=512 --verbosity=2 console
    
   
    docker build -t ether_prod .
    docker run --rm -it -p 9545:8545 -v /data/ethereum/prod:/eth_user/.ethereum ether_prod
    docker run -d -p 9545:8545 -v /data/ethereum/prod:/eth_user/.ethereum ether_prod
    geth --rpc --rpcport 8545 --rpcaddr 0.0.0.0 --rpccorsdomain "*" --rpcapi db,eth,net,web3,personal --testnet --fast --cache=512 --verbosity=2 console
   
  
    eth.syncing 
    web3.net.peerCount
    
    {
      currentBlock: 424937,
      highestBlock: 2788064,
      knownStates: 945142,
      pulledStates: 944401,
      startingBlock: 423808
    }
    
    npm install web3 bignumber.js abi-decoder

