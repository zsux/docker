#!/usr/bin/env node


const Web3 = require('web3')
//const web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/TOKEN"));
const web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:8545"));
const web3_1 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:9545"));

//console.log(web3.eth.getBlock(1));
// can be 'latest' or 'pending'

var options = {
    fromBlock: "0"
}

var cb = function(dd){
    console.log('callback 1',dd)
}

var cb2 = function(dd){
    console.log('callback 2',dd)
}

console.log(web3_1.eth.syncing)
console.log(web3.eth.syncing)

// var filter = web3.eth.filter();
var filter = web3.eth.filter('latest', cb, cb2);

// console.log(JSON.stringify(filter))
// OR object are log filter options
//var filter = web3.eth.filter(options);

// watch for changes
filter.watch(function (error, result) {
    if (error){
        console.error("Error: %s", error.message)
        // console.error("Stack: %s", error.stack)
    }
    if (!error)
        console.log(result);
});

// // Additionally you can start watching right away, by passing a callback:
// web3.eth.filter(options, function(error, result){
//   if (!error)
//     console.log(result);
// });