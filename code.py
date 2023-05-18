import streamlit as st
st.title("ジャシネーター")
st.header("あなたが考えている邪神ちゃんのキャラを当てるんですの。")
st.header("思いついたら次へを押すんですの！")
st.write("※マイナー過ぎるキャラクターは出てこない可能性があります。")
K=0
while K<1:
  if st.button("次へ"):
    K+=1
