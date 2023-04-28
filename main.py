import streamlit as st
import os
from random import randrange
import plotly.graph_objects as go

#page config
st.set_page_config(layout="wide")


st.title("Friday tutorial")

st.subheader("How to deploy a streamlit app using Azure services")

st.caption("A button")
if st.button("Generate a random integer!"):
    st.write(randrange(10))


st.caption("A cool graph")
fig = go.Figure(go.Surface(
    contours = {
        "x": {"show": True, "start": 1.5, "end": 2, "size": 0.04, "color":"white"},
        "z": {"show": True, "start": 0.5, "end": 0.8, "size": 0.05}
    },
    x = [1,2,3,4,5],
    y = [1,2,3,4,5],
    z = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]))
fig.update_layout(
        scene = {
            "xaxis": {"nticks": 20},
            "zaxis": {"nticks": 4},
            'camera_eye': {"x": 0, "y": -1, "z": 0.5},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2}
        })

st.plotly_chart(fig)