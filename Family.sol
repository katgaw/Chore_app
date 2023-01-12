// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Family {
    address public parent;
    address public child;

    constructor() public {
        parent = msg.sender;
        child;
    }

    modifier onlyOwner {
        require(
            msg.sender == parent,
            "Only the owner can call this function"
        );
        _;
    }

    modifier onlyFamily {
        require(msg.sender == child || msg.sender == parent, "You're not my child!");
        _;
    }
}