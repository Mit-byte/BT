pragma solidity >=0.7.4;
// SPDX-License-Identifier: UNLICENSED
 
contract Bank {
    uint balance;
 
    // event Deposit(uint val);
 
    function deposit(uint amt) public returns(uint) {
        balance += amt;
        return 1;
    }

    // event Withdraw(uint val);

    function withdraw   (uint amt) public returns(uint) {
        if(amt > balance) {
            return 0;
        }
        balance -= amt;
        return 1;
    }
    function showBalance() view public returns(uint) {
        return balance;
    } 
}
