# *Chore App*
---

**Welcome to my and Maxwell Marovich repository for the App for Children to earn money after cleaning their chores. Please explore the codebase!** <br />

---
## Analytical Summary

This app allows a money transfer from your account to your child's account in Metamask after your child cleans a kitchen. The child uploads an image with a clean kitchen and the image-classification model in the app decides if the kitchen is truly clean, only then it increases your child's balance for a private currency KAT (not linked to your currency). After the child cleans the kitchen number of times (default is 10 times) money will be transferred from your account to the child's account in your Metamask wallet.

This project allows you to use an app to objectively determine wheter your child cleaned the kitchen sufficiently and also to provide rewards to your child even when you are not home. 

Writing contracts with Solidity

* For minting a currency
* Allowing transfer to a child
* Allowing transfer of ownership to new child/parent pair
* Providing information about their balance

Family.sol
* Make sure only the parent and child can use the contract

Tidy_contract.sol
* transferOwnership to new parent-child pair
* Mint currency for the parent
* Transfer money from parent to child
* Get balances for both
* SafeMath with OpenZeppelin

Front-end with Streamlit
* Upload image button
* Message if the kitchen is clean
* Information about the allowance

Image-recognition model
* Uploading/scraping data
* Conversion to jpeg format
* Encoding dataset
* Splitting to train/test
* Neural network model
* Saving model as .h5

---

## Usage

To use this project simply clone the repository and run the code **streamlit run app_metamask.py** in your terminal.

## Methodology
!Before running the code:
1. Run the solidity contracts in Remix: Family.sol .
2. Save the abi.json (button in the bottom after compiling the contract in Remix).
3. Create a new project on the Infura website.
4. Make sure you have enough ETH on your Goerli testnet in Metamask wallet (at least 0.03 ETH).
5. Populate your .env file with:
API_KEY to your Pexels account (if you want to use the pexel website for the image recognition model, otherwise you can just upload your pics of clean and dirty kitchen, I recommend at least 400 images in total).
SMART_CONTRACT_ADDRESS = if you want to use the solidity contracts (not necessary for the app to function).
INFURA_API_KEY = your endpoint to the project you need to create for this app in Infura.
ACCOUNT_KEY = private key to your Metamask wallet (you will find it in the three dots in your Metamask Wallet)
parent_account = the number for your 'parent' account in Metamask
child_account = the number for your child's account in Metamask

---


The streamlit web app looks as follows:

![snippet of our code](Images/Image1.png)

![snippet of our code](Images/Image2.png)


![snippet of our code](Images/Image3.png)


---

## License

MIT

---


 
