import streamlit as st
import pandas as pd
from helpers import read_file
from settings import bucket_name

score_df = read_file(bucket_name, "Outputs/score_df.csv").set_index("Owner")
st.header("Match wise player points for our draft")
st.subheader("Points for players in our draft including captaincy mutlipliers")
st.dataframe(score_df)

sum_df = read_file(bucket_name, "Outputs/sum_df.csv").set_index("Owner")
st.header("Match aggregate points")
st.dataframe(sum_df)

cumsum_df = read_file(bucket_name, "Outputs/cumsum_df.csv").set_index("Owner")
st.header("Cumulative points")
st.dataframe(cumsum_df)

points_df = read_file(bucket_name, "Outputs/season_points_df.csv").set_index("Player")
st.header("Match wise player points for all players")
st.subheader("Points for all players without captaincy multipliers or bench exclusions")
st.dataframe(points_df)
