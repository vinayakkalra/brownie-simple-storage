# Simple storage contract using brownie

A Simple Storage Contract that uses brownie and python. 

1. You can find the SimpleStorage.sol in the contracts folder. This the contract that we are using to demonstrate a simple storage based on brownie. It has methods store (To store the number), retrieve (to retrieve the number) and addPeople (to add the values in People struct). You can find the deploy script in the scripts folder

2. This project also has two basic tests in the test folder. To run the tests, execute the below script in the terminal:

```
brownie test
```

3. To deploy the contract on rinkeby use the below script :

```
brownie run scripts/deploy.py --network rinkeby
```

Note: Make sure you have some testnet rinkeby ether with you before deployment

