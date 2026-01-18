import pandas as pd
import streamlit as st


df = pd.read_csv("datasets/1642645053.csv", encoding="tis-620")

st.write(df)



animal_count_per_area = df.groupby("สถานที่เลี้ยงสัตว์ เขตปศุสัตว์").size().reset_index(name="จำนวนสัตว์")

# แสดงผลรวมจำนวนสัตว์ต่อเขต
st.write("จำนวนสัตว์ต่อเขต", animal_count_per_area)
