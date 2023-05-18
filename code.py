import streamlit as st
import numpy as np 
import pandas as pd
import base64
import statsmodels.formula.api as smf
import statsmodels.api as sm
from PIL import Image
import matplotlib.pyplot as plt
import japanize_matplotlib

st.title("ジャシネーター")
st.write("あなたが考えている邪神ちゃんのキャラを当てるんですの。")
st.write("※マイナー過ぎるキャラクターは出てこない可能性があるんですの")

data=pd.read_csv("Jashin-Chan")
