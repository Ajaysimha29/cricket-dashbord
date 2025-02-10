import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.io as pio
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="🏏 Cricket Analytics Dashboard", layout="wide")

# 📌 Set dataset directory
dataset_dir = "C:/Users/ajayj/Desktop/courses/data viz/archive"

# 📌 Define dataset paths
dataset_paths = {
    "ipl": os.path.join(dataset_dir, "IPL dataset final.csv"),
    "bat": os.path.join(dataset_dir, "BATTING.csv"),
    "bow": os.path.join(dataset_dir, "BOWLING.csv"),
    "matches": os.path.join(dataset_dir, "Cricket_WC23.csv"),
    "players": os.path.join(dataset_dir, "PLAYERS_INFO.csv")
}

# Load datasets
@st.cache_data
def load_data():
    return {
        "ipl": pd.read_csv(dataset_paths["ipl"]),
        "bat": pd.read_csv(dataset_paths["bat"], encoding='latin-1'),
        "bow": pd.read_csv(dataset_paths["bow"]),
        "matches": pd.read_csv(dataset_paths["matches"]),
        "players": pd.read_csv(dataset_paths["players"])
    }

data = load_data()

# Sidebar - Select analysis
tab = st.sidebar.radio("Select Analysis", ["IPL Analysis", "World Cup Batting", "World Cup Bowling", "Match Analysis"])

# Sidebar - Color theme selection
color_theme = st.sidebar.selectbox("Select Color Theme", ["light", "dark"])

if color_theme == "dark":
    st.markdown('<style>body{background-color: #1e1e1e; color: white;}</style>', unsafe_allow_html=True)
else:
    st.markdown('<style>body{background-color: white; color: black;}</style>', unsafe_allow_html=True)

# Function to save plotly figures as images
def save_fig_as_image(fig):
    img_bytes = BytesIO()
    pio.write_image(fig, img_bytes, format='png')
    img_bytes.seek(0)
    return img_bytes

# IPL Analysis
if tab == "IPL Analysis":
    st.title("📊 IPL Analytics")
    st.subheader("Player Sold Prices")
    fig1 = px.histogram(data["ipl"], x="SOLD_PRICE", nbins=20, title="Distribution of IPL Player Sold Prices")
    st.plotly_chart(fig1)
    
    st.subheader("Total Spending by Teams")
    team_spending = data["ipl"].groupby("TEAM")["SOLD_PRICE"].sum().reset_index()
    fig2 = px.bar(team_spending, x="TEAM", y="SOLD_PRICE", title="Total Spending by IPL Teams", color="TEAM")
    st.plotly_chart(fig2)

    # Download button for IPL dataset
    st.sidebar.download_button(
        label="Download IPL Price Data",
        data=data["ipl"].to_csv(index=False),
        file_name="ipl_prices.csv",
        mime="text/csv"
    )

    # Download figures as images
    st.sidebar.download_button(
        label="Download IPL Sold Prices Chart",
        data=save_fig_as_image(fig1),
        file_name="ipl_sold_prices.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download IPL Team Spending Chart",
        data=save_fig_as_image(fig2),
        file_name="ipl_team_spending.png",
        mime="image/png"
    )

# World Cup Batting Analysis
elif tab == "World Cup Batting":
    st.title("🏏 World Cup Batting Analysis")
    st.subheader("Runs vs Strike Rate")
    fig3 = px.scatter(data["bat"], x="RUNS", y="STRICK RATE", color="BATTING_TEAM", hover_data=["BATTING"], title="Runs vs Strike Rate")
    st.plotly_chart(fig3)
    
    st.subheader("Runs Distribution by Team")
    fig4 = px.box(data["bat"], x="BATTING_TEAM", y="RUNS", title="Runs Distribution by Team")
    st.plotly_chart(fig4)

    # Download button for Batting dataset
    st.sidebar.download_button(
        label="Download Batting Data",
        data=data["bat"].to_csv(index=False),
        file_name="batting_data.csv",
        mime="text/csv"
    )

    # Download figures as images
    st.sidebar.download_button(
        label="Download Runs vs Strike Rate Chart",
        data=save_fig_as_image(fig3),
        file_name="runs_vs_strike_rate.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Runs Distribution Chart",
        data=save_fig_as_image(fig4),
        file_name="runs_distribution_by_team.png",
        mime="image/png"
    )

# World Cup Bowling Analysis
elif tab == "World Cup Bowling":
    st.title("🎯 World Cup Bowling Analysis")
    st.subheader("Average Economy Rate by Team")
    economy = data["bow"].groupby("BOWLING_TEAM")["ECONOMY"].mean().reset_index()
    fig5 = px.bar(economy, x="BOWLING_TEAM", y="ECONOMY", title="Average Economy Rate by Team", color="BOWLING_TEAM")
    st.plotly_chart(fig5)
    
    st.subheader("Top 10 Wicket-Takers")
    top_wickets = data["bow"].groupby("BOWLING")["WICKETS"].sum().nlargest(10).reset_index()
    fig6 = px.bar(top_wickets, x="BOWLING", y="WICKETS", title="Top 10 Wicket-Takers")
    st.plotly_chart(fig6)

    # Download button for Bowling dataset
    st.sidebar.download_button(
        label="Download Bowling Data",
        data=data["bow"].to_csv(index=False),
        file_name="bowling_data.csv",
        mime="text/csv"
    )

    # Download figures as images
    st.sidebar.download_button(
        label="Download Economy Rate Chart",
        data=save_fig_as_image(fig5),
        file_name="economy_rate_by_team.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Wicket-Takers Chart",
        data=save_fig_as_image(fig6),
        file_name="top_wicket_takers.png",
        mime="image/png"
    )

# Match Analysis
elif tab == "Match Analysis":
    st.title("🏆 World Cup Match Analysis")
    st.subheader("World Cup Wins by Team")
    team_wins = data["matches"]["Winner"].value_counts()
    fig7 = px.pie(names=team_wins.index, values=team_wins.values, title="World Cup Wins by Teams")
    st.plotly_chart(fig7)
    
    st.subheader("Team Wins Over Time")
    wins_over_time = data["matches"].groupby(["Match Date", "Winner"]).size().reset_index(name="Win Count")
    fig8 = px.line(wins_over_time, x="Match Date", y="Win Count", color="Winner", title="Team Wins Over Time")
    st.plotly_chart(fig8)

    # Download button for Match dataset
    st.sidebar.download_button(
        label="Download Match Data",
        data=data["matches"].to_csv(index=False),
        file_name="match_data.csv",
        mime="text/csv"
    )

    # Additional Figure: Total Matches Played Over Time
    st.subheader("Total Matches Played Over Time")
    total_matches_over_time = data["matches"].groupby("Match Date").size().reset_index(name="Total Matches")
    fig9 = px.line(total_matches_over_time, x="Match Date", y="Total Matches", title="Total Matches Played Over Time")
    st.plotly_chart(fig9)

    # Download figure as an image
    st.sidebar.download_button(
        label="Download Total Matches Played Over Time Chart",
        data=save_fig_as_image(fig9),
        file_name="total_matches_played.png",
        mime="image/png"
    )
