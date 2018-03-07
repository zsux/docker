var Web3 = require('web3');
var BigNumber = require('bignumber.js');
var coder = require('web3/lib/solidity/coder');
const abiDecoder = require('abi-decoder'); // NodeJS

const web3 = new Web3(new Web3.providers.HttpProvider("https://ropsten.infura.io/TOKEN"));
//var web3 = new Web3(new Web3.providers.HttpProvider('https://api.myetherapi.com/eth'));

web3.setProvider(new web3.providers.HttpProvider('http://127.0.0.1:8545'));
web3.setProvider(new web3.providers.HttpProvider('https://ropsten.infura.io/TOKEN'));
web3.eth.getBlock(1)


var filter = web3.eth.filter('pending');

var account = '0xE767aEB31dAAF66366999F72FB5De2CEEA76c277'.toLowerCase()
var filter = web3.eth.filter('latest')


filter.watch(function(error, result) {
    if (!error) {
         console.log(result)
    }
})




var balance = new BigNumber('131242344353464564564574574567456');

console.log(balance.plus(21).toString(10))
web3.eth.getTransaction("0x0870b9316a9d9a353a7b453ab994c8cf31ed936d6df46c772404c6171851a326")

var str = web3.toHex({test: 'test'});
console.log(str); // '0x7b2274657374223a2274657374227d'

var str = web3.toAscii("0x0000000000000000000000000000000220000000000000000000000000000000");
console.log(str); // "ethereum"


console.log(web3.toAscii("0x3100000000000000000000000000000000000000000000000000000000000000"))

web3.eth.defaultAccount = '0x0c73af7f4b5341fbc63f5b5d4902a7f25805ebb9';

var number = web3.eth.getBlockTransactionCount("0x0870b9316a9d9a353a7b453ab994c8cf31ed936d6df46c772404c6171851a326");


var str = web3.toAscii("0x27dc297eab9620b7d3242e85e6fe908cddeeae8681358452442eac3d7fc54636526f521d000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000013100000000000000000000000000000000000000000000000000000000000000");
console.log(str)


web3.eth.abi.decodeParameters(['bytes32', 'string','bytes'], '0x27dc297eab9620b7d3242e85e6fe908cddeeae8681358452442eac3d7fc54636526f521d000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000013100000000000000000000000000000000000000000000000000000000000000');

coder.decodeParam("string",'000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000013100000000000000000000000000000000000000000000000000000000000000');

coder.encodeParam("string","welcome to ethereum. welcome to ethereum. welcome to ethereum.");
var abi = require('./api.json');
abiDecoder.addABI(abi);
const decodedData = abiDecoder.decodeMethod("0x27dc297eab9620b7d3242e85e6fe908cddeeae8681358452442eac3d7fc54636526f521d000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000013100000000000000000000000000000000000000000000000000000000000000");
web3.eth.getTransactionReceipt("0x0870b9316a9d9a353a7b453ab994c8cf31ed936d6df46c772404c6171851a326", function(e, receipt) {
    const decodedLogs = abiDecoder.decodeLogs(receipt.logs);
    console.log(decodedLogs)
});

