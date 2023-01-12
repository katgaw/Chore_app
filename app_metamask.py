################################################################################
#                                   Chore App
################################################################################

#Libraries
import streamlit as st
from web3 import Web3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
from PIL import Image
import tensorflow as tf
import numpy as np
import json

import utils as u


load_dotenv()

 #Upload your Infura api key
infura_api_key=os.getenv("INFURA_API_KEY")
# Upload accounts from your Metamask
parent=os.getenv('parent_account')
child=os.getenv('child_account')

# Connect to your MetaMask
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/'+infura_api_key))
accounts = w3.eth.accounts

# Define the value for the chore
chore_value=0.000001 #Value for 10 chores in ETH
amount = 1 #Value in your private currency KAT


#Load model
file_path=Path('image_model.h5')
model_load=tf.keras.models.load_model(file_path)

################################################################################
# Contract Helper function:
################################################################################

#Upload your contract from Remix
def load_contract(w3):

    # Load the contract ABI
    with open(Path('abi.json')) as f:
        abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=abi
    )

    return contract
contract = load_contract(w3)

balance_child=0
model_result=0

# Main page
################################################################################
# Upload local image as background for the streamlit app
u.add_bg_from_local('pexels-photo-5998025.jpeg')
st.title("Tidy Vision")
st.header("Clean your kitchen and earn $$$")

################################################################################
# Sidebar
################################################################################
# Streamlit Sidebar Code - Start
st.sidebar.markdown("## Settings")
    
# Upload button for the image
image_file = st.sidebar.file_uploader("So you cleaned up the kitchen huh? Prove it!", type=['png', 'jpeg','jpg'])

# Transfer money in your currency KAT
kitchen_button = st.sidebar.button('Clean Kitchen')

# Save the amount in your private currency
if 'amount' not in st.session_state:
    st.session_state.amount = 0

# if you click the Kitchen button - evaluate if kitchen is clean
if kitchen_button:
    if image_file:
        image = Image.open(image_file) #Open the image file

        #Convert the image size
        img = tf.keras.utils.load_img(
            image_file, target_size=(180, 180)
        )
        # Vectorize the image for the image-recognition model
        img_array = tf.keras.utils.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)

        # Predict if the kitchen is clean
        prediction=model_load.predict(img_array)
        score = tf.nn.softmax(prediction[0])
        model_result=np.argmax(score)
        if model_result==0:
            st.sidebar.write("Congrats, you cleaned the kitchen!")

            # Create a button which will increment the balance in KAT
            st.session_state.amount += 1
            balance_child+=st.session_state.amount
            st.sidebar.write("Your balance is now "+ str(balance_child) +"KAT")
            
            
        else:
            st.sidebar.write("The kitchen is still dirty. Get back to work!")
    else:
        st.sidebar.write("Please upload an image")

st.markdown("---")
st.markdown("---")

# If the child collected 10 units of KAT transfer him ETH
if balance_child > 1 and balance_child % 10 ==0:
    private_key=os.getenv("ACCOUNT_KEY")
    nonce=w3.eth.getTransactionCount(parent)
    tokens=chore_value
    tx={
        'nonce': nonce,
        'to': child,
        'value': w3.toWei(tokens, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei(40, 'gwei')
    }

    signed_tx=w3.eth.account.signTransaction(tx, private_key)

    tx_transaction=w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    st.sidebar.write(f"Allowance of {amount} is transferred.")


# See the child balance in ETH
balance=w3.eth.get_balance(child)
tokens=w3.fromWei(balance,'ether')
st.sidebar.write(f"This address owns {tokens}ETH.")

#Sources:
##https://www.youtube.com/watch?v=cFB1BGeCpn0

