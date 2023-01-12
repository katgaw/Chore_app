// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "./Family.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/math/SafeMath.sol";

contract TidyVision is Family {
    using SafeMath for uint256;
    mapping(address => uint) balances;

    
    function transferOwnership(address newParent, address newChild) external onlyOwner {
        parent = newParent;
        child = newChild;
    }

    function balanceOf(address addressOf) public view returns(uint) {
        return balances[addressOf];
    }

    //function addFunds(address payable _child) external payable onlyOwner {
    //    child = _child;
    //}


    function transfer(address payable recipient, uint value) public {
        require(msg.sender==parent && recipient==child, "You are not the parties in the contract, you cannot do the transfer!");
        // @TODO: replace the following with the .sub function
        balances[msg.sender] = balances[msg.sender].sub(value);
        // @TODO: replace the following with the .add function
        balances[recipient] = balances[recipient].add(value);
    }

    function mint(address recipient, uint value) public {
        require(msg.sender == parent, "You do not have permission to mint tokens!");
        // @TODO: replace the following with the .add function
        balances[recipient] = balances[recipient] + value;
    }

    //function withdraw() external onlyFamily {
    //    payable(msg.sender).transfer(1000000000000000); // set to .001 ETH
        
    //}
}
