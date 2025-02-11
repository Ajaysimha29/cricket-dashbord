import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.io as pio
from io import BytesIO
import random
import streamlit as st
from streamlit_option_menu import option_menu  # Import for better sideb



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

# Sidebar - Select analysis
with st.sidebar:
    st.markdown("## Cricket Analytics Dashboard")
    selected = option_menu(
        menu_title=None,  # Remove default title
        options=["IPL Analysis", "World Cup Batting", "World Cup Bowling", "Match Analysis", "Cricket Quiz", "Memes & GIFs"],
        icons=["graph-up", "trophy", "baseball", "bar-chart", "gamepad", "image"],  # Add corresponding icons
        menu_icon="cast",  # Overall menu icon
        default_index=0,  # Default selected page
        orientation="vertical",  # Vertical menu
        styles={
            "container": {"padding": "5px", "background-color": "#f0f0f5"},  # Style container
            "icon": {"font-size": "18px"},  # Icon size
            "nav-link": {"font-size": "16px", "text-align": "left", "padding": "8px", "color": "black", "hover-color": "#58a6ff"},  # Link styles
            "nav-link-selected": {"background-color": "#58a6ff"},  # Selected link style
        }
    )



# Function to save plotly figures as images
def save_fig_as_image(fig):
    img_bytes = BytesIO()
    pio.write_image(fig, img_bytes, format='png')
    img_bytes.seek(0)
    return img_bytes

# IPL Analysis
if selected == "IPL Analysis":
    st.title("📊 IPL Analytics")
    st.subheader("Player Sold Prices")
    fig1 = px.histogram(data["ipl"], x="SOLD_PRICE", nbins=20, title="Distribution of IPL Player Sold Prices")
    st.plotly_chart(fig1)
    
    st.subheader("Total Spending by Teams")
    team_spending = data["ipl"].groupby("TEAM")["SOLD_PRICE"].sum().reset_index()
    fig2 = px.bar(team_spending, x="TEAM", y="SOLD_PRICE", title="Total Spending by IPL Teams", color="TEAM")
    st.plotly_chart(fig2)

    # Additional IPL Insights
    #st.subheader("Top 5 Expensive Players")
    #top_expensive_players = data["ipl"].nlargest(5, "SOLD_PRICE")[["PLAYER", "SOLD_PRICE"]]
    #fig3 = px.bar(top_expensive_players, x="PLAYER", y="SOLD_PRICE", title="Top 5 Expensive IPL Players", color="PLAYER")
    #st.plotly_chart(fig3)

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
elif selected == "World Cup Batting":
    st.title("🏏 World Cup Batting Analysis")
    st.subheader("Runs vs Strike Rate")
    fig4 = px.scatter(data["bat"], x="RUNS", y="STRICK RATE", color="BATTING_TEAM", hover_data=["BATTING"], title="Runs vs Strike Rate")
    st.plotly_chart(fig4)
    
    st.subheader("Runs Distribution by Team")
    fig5 = px.box(data["bat"], x="BATTING_TEAM", y="RUNS", title="Runs Distribution by Team")
    st.plotly_chart(fig5)

    # Additional Batting Insights
    #st.subheader("Top 5 Run Scorers")
    #top_run_scorers = data["bat"].nlargest(5, "RUNS")[["BATTING", "RUNS"]]
    #fig6 = px.bar(top_run_scorers, x="BATTING", y="RUNS", title="Top 5 Run Scorers in WC", color="BATTING")
    #st.plotly_chart(fig6)

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
        data=save_fig_as_image(fig4),
        file_name="runs_vs_strike_rate.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Runs Distribution Chart",
        data=save_fig_as_image(fig5),
        file_name="runs_distribution_by_team.png",
        mime="image/png"
    )

# World Cup Bowling Analysis
elif selected == "World Cup Bowling":
    st.title("🎯 World Cup Bowling Analysis")
    st.subheader("Average Economy Rate by Team")
    economy = data["bow"].groupby("BOWLING_TEAM")["ECONOMY"].mean().reset_index()
    fig7 = px.bar(economy, x="BOWLING_TEAM", y="ECONOMY", title="Average Economy Rate by Team", color="BOWLING_TEAM")
    st.plotly_chart(fig7)
    
    st.subheader("Top 10 Wicket-Takers")
    top_wickets = data["bow"].groupby("BOWLING")["WICKETS"].sum().nlargest(10).reset_index()
    fig8 = px.bar(top_wickets, x="BOWLING", y="WICKETS", title="Top 10 Wicket-Takers")
    st.plotly_chart(fig8)

    # Additional Bowling Insights
    st.subheader("Top 5 Best Economy Rate Bowlers")
    top_economy_bowlers = data["bow"].nsmallest(5, "ECONOMY")[["BOWLING", "ECONOMY"]]
    fig9 = px.bar(top_economy_bowlers, x="BOWLING", y="ECONOMY", title="Top 5 Best Economy Rate Bowlers", color="BOWLING")
    st.plotly_chart(fig9)

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
        data=save_fig_as_image(fig7),
        file_name="economy_rate_by_team.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Wicket-Takers Chart",
        data=save_fig_as_image(fig8),
        file_name="top_wicket_takers.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Best Economy Bowlers Chart",
        data=save_fig_as_image(fig9),
        file_name="top_best_economy_bowlers.png",
        mime="image/png"
    )

# Match Analysis
elif selected == "Match Analysis":
    st.title("🏆 World Cup Match Analysis")
    st.subheader("World Cup Wins by Team")
    team_wins = data["matches"]["Winner"].value_counts()
    fig10 = px.pie(names=team_wins.index, values=team_wins.values, title="World Cup Wins by Teams")
    st.plotly_chart(fig10)
    
    st.subheader("Team Wins Over Time")
    wins_over_time = data["matches"].groupby(["Match Date", "Winner"]).size().reset_index(name="Win Count")
    fig11 = px.line(wins_over_time, x="Match Date", y="Win Count", color="Winner", title="Team Wins Over Time")
    st.plotly_chart(fig11)

    # Additional Match Insights
    st.subheader("Match Result by Date")
    result_by_date = data["matches"].groupby("Match Date")["Winner"].value_counts().unstack().fillna(0)
    fig12 = px.line(result_by_date, x=result_by_date.index, title="Match Result by Date")
    st.plotly_chart(fig12)

    # Download button for Match dataset
    st.sidebar.download_button(
        label="Download Match Data",
        data=data["matches"].to_csv(index=False),
        file_name="match_data.csv",
        mime="text/csv"
    )

    # Additional Figure: Total Matches Played Over Time
    st.subheader("Total Matches Played Over Time")
    total_matches_over_time = data["matches"].groupby("Match Date").size().reset_index(name="Matches Played")
    fig13 = px.line(total_matches_over_time, x="Match Date", y="Matches Played", title="Total Matches Played Over Time")
    st.plotly_chart(fig13)

    # Download figures as images
    st.sidebar.download_button(
        label="Download Match Win Distribution Chart",
        data=save_fig_as_image(fig10),
        file_name="world_cup_wins_by_team.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Team Wins Over Time Chart",
        data=save_fig_as_image(fig11),
        file_name="team_wins_over_time.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Match Result by Date Chart",
        data=save_fig_as_image(fig12),
        file_name="match_result_by_date.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Matches Played Over Time Chart",
        data=save_fig_as_image(fig13),
        file_name="matches_played_over_time.png",
        mime="image/png"
    )
# Cricket Quiz Game
# Cricket Quiz Game
def cricket_quiz():
    st.title("🎮 Cricket Quiz Game")
    st.subheader("Test Your Knowledge")

    # Initialize session state for tracking answers, score, and question index
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0

    # List of Questions and Answers
    quiz_questions = [
        {"question": "Who won the first Cricket World Cup?", "options": ["Australia", "West Indies", "India", "England"], "answer": "West Indies"},
        {"question": "Which country hosted the 2011 World Cup?", "options": ["India", "Sri Lanka", "Bangladesh", "Pakistan"], "answer": "India"},
        {"question": "Who is the highest run-scorer in World Cup history?", "options": ["Sachin Tendulkar", "Ricky Ponting", "Kumar Sangakkara", "Brian Lara"], "answer": "Sachin Tendulkar"},
        {"question": "How many overs are there in a standard ODI match?", "options": ["20", "40", "50", "60"], "answer": "50"},
        {"question": "Which player has scored the most runs in Test cricket?", "options": ["Sachin Tendulkar", "Ricky Ponting", "Brian Lara", "Virat Kohli"], "answer": "Sachin Tendulkar"}
    ]

    # Display the current question
    if st.session_state.question_index < len(quiz_questions):
        question = quiz_questions[st.session_state.question_index]
        st.write(f"Question {st.session_state.question_index + 1}: {question['question']}")

        # Let the user select an answer
        answer = st.radio("Choose the correct answer", question["options"], key=f"quiz_{st.session_state.question_index}")

        # Add a button to submit the answer and check the result
        submit = st.button("Submit Answer")

        if submit:
            if answer:
                # Check if the answer is correct
                if answer == question["answer"]:
                    st.success("Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorrect. The correct answer is: {question['answer']}")

                # Move to the next question
                st.session_state.question_index += 1
            else:
                st.warning("Please select an answer before submitting.")

    # Show score at the end
    else:
        st.subheader("Quiz Finished!")
        st.write(f"Your final score is: {st.session_state.score} out of {len(quiz_questions)}")

        # Option to restart the quiz
        if st.button("Play Again"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.experimental_rerun()  # Re-run to reset the quiz state

# Use the function to handle the "Cricket Quiz" section
if selected == "Cricket Quiz":
    cricket_quiz()
# Fun Cricket Memes and GIFs
elif selected == "Memes & GIFs":
    st.title("😂 Fun Cricket Memes and GIFs")
    meme_urls = [
        #"https://media1.tenor.com/m/dq4CBxSKxawAAAAd/striker-saini.gif"  # Cricket batsman hit
        "https://media1.tenor.com/m/DEiXgXvrHzgAAAAC/dhoni-gif.gif",  # Umpire gesture
        #"https://media1.tenor.com/m/uhmCKHPRp_oAAAAC/risers-with-buland-soch-cricket.gif",  # Players hugging
        "https://media1.tenor.com/m/l1iKhSUAdRoAAAAC/cheating-at-cricket-do-not-scratch-your-balls.gif",  # Cricket catch
    ]

    # Display memes/GIFs in a grid layout for better presentation
    cols = st.columns(3)  # Create 3 columns
    for i, url in enumerate(meme_urls):
        with cols[i % 3]:  # Place each item in a column
            st.image(url, use_container_width=True)

