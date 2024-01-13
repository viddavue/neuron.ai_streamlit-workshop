import pandas as pd
import numpy as np
import random
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from utils import crocodile_facts, alligator_facts






if __name__ == '__main__':
    st.session_state[''], total_runs = 0, 0

    # set title
    st.title('Train your personal neural image classifier')
    next_button = st.button("Guess again")
    # set sidebar
    st.sidebar.title('About')
    st.sidebar.info(
        'This is a Streamlit app written by crocodile hunters to showcase a random image and lets the user guess if it is a crocodile or an alligator.')