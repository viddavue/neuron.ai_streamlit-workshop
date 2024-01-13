# streamlit app that showcases a random image and lets the user guess if it is a crocodile or an alligator

import streamlit as st
import time
import pandas as pd
import numpy as np
import random
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from utils import crocodile_facts, alligator_facts

if 'score' not in st.session_state:
    st.session_state['score'], st.session_state['total_runs'] = 0, 1
st.session_state['guessed'] = False
# set title
st.title('Train your personal neural image classifier')

# set sidebar
st.sidebar.title('About')
st.sidebar.info(
    'This is a Streamlit app written by crocodile hunters to showcase a random image and lets the user guess if it is '
    'a crocodile or an alligator.\n Disclaimer: We do not guarantee for the correctness of the displayed facts.')

# set random image by searching the subfolders

if 'random_image' not in st.session_state:
    st.session_state['random_image'] = random.choice(
        os.listdir('alligator vs crocodile/alligator/') + os.listdir('alligator vs crocodile/crocodile/'))
# set image path
image_path = 'alligator vs crocodile/' + st.session_state['random_image'][:9] + '/' + st.session_state['random_image']
# set image
image = Image.open(image_path)

# show image
image1 = st.image(image, caption='Is it a crocodile or an alligator?', use_column_width=True)

st.subheader("Make your guess!")
# set buttons
# set button text
col1, col2 = st.columns(2)
croc_button = col1.button('Crocodile')
all_button = col2.button('Alligator')

# Create a plot in the sidebar to display the guessing accuracy over time

st.sidebar.subheader("Your guessing accuracy over time")
if "accuracies" in st.session_state:
    st.sidebar.line_chart(pd.DataFrame({'Accuracy': st.session_state['accuracies']},
                                       columns=['Accuracy']))

# set button function
if croc_button and not st.session_state["guessed"]:

    # set button function
    if 'crocodile' in image_path[-20:]:
        st.session_state['score'] += 1
        st.write(f'You guessed right! It is a crocodile. Your reward is a fun fact about crocodiles:')
        st.write(random.choice(crocodile_facts))
    else:
        st.write(f'You guessed wrong! It is actually an alligator :(')
        st.session_state['score'] = max(st.session_state['score'] - 1, 0)
    st.session_state['guessed'] = True

if all_button and not st.session_state["guessed"]:
    # set button function
    if 'alligator' in image_path.split('/')[-1]:
        st.session_state['score'] += 1
        st.write(f'You guessed right! It is an alligator. Your reward is a fun fact about alligators:')
        st.write(random.choice(alligator_facts))
    else:
        st.session_state['score'] = max(st.session_state['score'] - 1, 0)
        st.write(f'You guessed wrong! It is actually a crocodile :(')
    st.session_state['guessed'] = True

next_button = st.button("Guess again")
if next_button:
    st.session_state['total_runs'] += 1
    st.session_state['random_image'] = random.choice(os.listdir('alligator vs crocodile/alligator/') +
                                                     os.listdir('alligator vs crocodile/crocodile/'))
    if st.session_state['total_runs'] % 10 == 0:
        if "accuracies" not in st.session_state:
            st.session_state['accuracies'] = [
                st.session_state['score'] / st.session_state['total_runs']
            ]
        else:
            st.session_state['accuracies'].append(
                st.session_state['score'] / st.session_state['total_runs']
            )

    st.rerun()
