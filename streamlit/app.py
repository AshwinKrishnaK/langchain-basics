import streamlit as st
import numpy as np
import pandas as pd

#Display a simple text
st.write("Hellooo Ashwin")

#Create a Simple dataframe

df = pd.DataFrame({
    'a':[1,2,3,4,5],
    'b':[9,7,6,5,4]
})

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.write("DataFrame")
st.write(df)

st.write("Line Chart")
st.line_chart(chart_data)
