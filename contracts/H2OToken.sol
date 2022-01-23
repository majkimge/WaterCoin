// contracts/H2OToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract H2OToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("WaterCoin", "H2O") {
        _mint(msg.sender, initialSupply);
    }
}
