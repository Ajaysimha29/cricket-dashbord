import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.io as pio
from io import BytesIO
import random
import streamlit as st
from streamlit_option_menu import option_menu  # Import for better sideb



st.set_page_config(page_title="🏏 Cricket Analytics Dashboard", layout="wide")

# 📌 Set dataset directory
dataset_dir = "C:/Users/ajayj/Desktop/courses/data viz/data"

# 📌 Define dataset paths
dataset_paths = {
    "ipl": os.path.join(dataset_dir, "ipl.csv"),
    "bat": os.path.join(dataset_dir, "bat.csv"),
    "bow": os.path.join(dataset_dir, "bow.csv"),
    "matches": os.path.join(dataset_dir, "matches.csv"),
    "players": os.path.join(dataset_dir, "players.csv")
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

# Correct dataset reference
ipl = data["ipl"]

# Sidebar - Select analysis
with st.sidebar:
    st.markdown("## 🏏 Cricket Analytics Dashboard")
    selected = option_menu(
        menu_title=None,  # Remove default title
        options=[
            "Home",
            "IPL Analysis",
            "World Cup Batting",
            "World Cup Bowling",
            "Match Analysis",
            "Cricket Quiz",
            "Memes & GIFs",
            "Player Performance Correlation",
            "Visualized Story"
        ],
        icons=[
            "house",  # Home
            "graph-up",  # IPL Analysis
            "trophy",  # World Cup Batting
            "activity",  # World Cup Bowling
            "bar-chart",  # Match Analysis
            "controller",  # Cricket Quiz
            "image",  # Memes & GIFs
            "diagram-3",  # Player Performance Correlation (Added icon)
            "book"  # Visualized Story (Added icon)
        ],
        menu_icon="cast",  # Overall menu icon
        default_index=0,  # Default selected page
        orientation="vertical",  # Vertical menu
        styles={
            "container": {"padding": "5px", "background-color": "#f0f0f5"},  # Sidebar background
            "icon": {"font-size": "18px"},  # Icon size
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "padding": "8px",
                "color": "black",
                "hover-color": "#58a6ff"
            },  # Link styles
            "nav-link-selected": {"background-color": "#58a6ff"},  # Selected link style
        }
    )


# Function to save plotly figures as images
def save_fig_as_image(fig):
    img_bytes = BytesIO()
    pio.write_image(fig, img_bytes, format='png')
    img_bytes.seek(0)
    return img_bytes





if selected == "Home":
    # Page Title with Emoji
    st.markdown("<h1 style='text-align: center; color: #ff4b4b; font-size: 50px;'>🏏 Cricket Analytics Dashboard</h1>", unsafe_allow_html=True)
     # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.pinimg.com/originals/0c/e9/02/0ce90263bde405e21c544de46982006a.gif");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Banner Image (Full Width)
    st.image("https://wallpapercave.com/wp/wp6194569.jpg", use_container_width=True)

    # Welcome Message with Larger Font
    st.markdown("""
        <h2 style='text-align: center; color: #f39c12;'>Welcome to the Cricket Analytics Dashboard! 🎉</h2>
        <p style='text-align: center; font-size: 20px;'>Discover exciting cricket statistics, insights, and fun activities! 🚀</p>
    """, unsafe_allow_html=True)

    # Features Section with Icons and Bold Styling
    st.markdown("""
        <h2 style='color: #3498db;'>🔍 Explore Cricket Insights:</h2>
        <ul style="font-size: 18px; line-height: 1.8;">
            <li>🏆 <b>IPL Analysis:</b> Player prices, team spending & auction trends.</li>
            <li>🏅 <b>World Cup Batting:</b> Top scorers & batting performance insights.</li>
            <li>🎯 <b>World Cup Bowling:</b> Best bowlers, wickets & economy rates.</li>
            <li>🏏 <b>Match Analysis:</b> In-depth match statistics & trends.</li>
            <li>🎮 <b>Cricket Quiz:</b> Test your knowledge with interactive trivia! 🧠</li>
            <li>😂 <b>Memes & GIFs:</b> Enjoy cricket memes for a fun break! 🎉</li>
            <li>😂 <b>Visualized Story:</b> 🔍 Discovering Cricket 🏏, IPL 🥇, and World Cup 🌍🏆 Data Like Never Before!</li>
        </ul>
    """, unsafe_allow_html=True)

    # Data Sources Section
    st.markdown("""
        <h2 style='color: #e67e22;'>📊 Data Sources:</h2>
        <ul style="font-size: 18px; line-height: 1.8;">
            <li>IPL Player Data</li>
            <li>World Cup 2023 Statistics (Batting & Bowling)</li>
            <li>Player Performance Metrics</li>
            <li>Historical Match Records</li>
        </ul>
        <p style="font-size: 18px;"><b>Get ready to explore cricket data like never before! 🏏🚀</b></p>
    """, unsafe_allow_html=True)

    # Start Exploring Button
    if st.button("🔥 Start Exploring Now! 🚀"):
        st.write("Awesome! Let's dive into the IPL Analysis!")







#st.markdown(page_element, unsafe_allow_html=True)
# IPL Analysis
if selected == "IPL Analysis":
    st.title("📊 IPL Analytics")
    
    
    # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHR3NmtndWpkcmhwaDF6MDQ4Nmg5cms1b2hzc2VnenZkMHI4emVqcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pUfqPRDs7K2IiN90yG/giphy.gif");
    .rotating-gif {
    display: block;
    margin: auto;
    width: 250px;  /* Adjust size */
    height: auto;
    animation: slow-rotate 10s linear infinite;
    }

    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
    
    # IPL Analysis: Player Sold Prices
    st.subheader("Player Sold Prices")
    fig1 = px.histogram(data["ipl"], x="SOLD_PRICE", nbins=20, title="Distribution of IPL Player Sold Prices")
    st.plotly_chart(fig1)

    # IPL Analysis: Total Spending by Teams
    st.subheader("Total Spending by Teams")
    team_spending = data["ipl"].groupby("TEAM")["SOLD_PRICE"].sum().reset_index()
    fig2 = px.bar(team_spending, x="TEAM", y="SOLD_PRICE", title="Total Spending by IPL Teams", color="TEAM")
    st.plotly_chart(fig2)
    
     
    #st.write(data["ipl"].head()) 
    #st.write(data["ipl"]["SOLD_PRICE"].head())  # Debugging step
    # Remove commas and convert to numeric
    #data["ipl"]["SOLD_PRICE"] = data["ipl"]["SOLD_PRICE"].astype(str).str.replace(",", "")
    #data["ipl"]["SOLD_PRICE"] = pd.to_numeric(data["ipl"]["SOLD_PRICE"], errors="coerce")

# Drop rows with NaN SOLD_PRICE values
    #data["ipl"].dropna(subset=["SOLD_PRICE"], inplace=True)

    #st.write(data["ipl"]["SOLD_PRICE"].head())  # Verify cleaned data

    #st.subheader("Total Spending by IPL Teams")
    #data["ipl"]["SOLD_PRICE"] = data["ipl"]["SOLD_PRICE"].astype(str).str.replace("cr", "", regex=False).astype(float)
    #team_spending = data["ipl"].groupby("TEAM")["SOLD_PRICE"].sum().reset_index()
    #fig3 = px.scatter(team_spending, 
                 #x="TEAM", 
                 #y="SOLD_PRICE", 
                 #size="SOLD_PRICE",  # Bubble size
                 #color="TEAM",  # Different colors for teams
                 #title="Total Spending by IPL Teams",
                 #hover_name="TEAM", 
                 #size_max=60)
    #st.plotly_chart(fig3)
    st.write(data["ipl"].head())
    st.write(data["ipl"]["SOLD_PRICE"].head())  # Debugging step

    def convert_price_to_float(price_str):
     price_str = str(price_str).lower()  # Convert to lowercase for easier handling

     if "cr" in price_str:
         price_str = price_str.replace("cr", "")
         return float(price_str) * 10000000  # Convert crores to float
     elif "l" in price_str:
         price_str = price_str.replace("l", "")
         return float(price_str) * 100000  # Convert lakhs to float
     else:
         try:
            return float(price_str)  # If no 'cr' or 'l', try direct conversion
         except ValueError:
            return None  # Return None for invalid values

# Apply the conversion function to the 'SOLD_PRICE' column
    data["ipl"]["SOLD_PRICE"] = data["ipl"]["SOLD_PRICE"].apply(convert_price_to_float)

# Drop rows with NaN SOLD_PRICE values after conversion.
    data["ipl"].dropna(subset=["SOLD_PRICE"], inplace=True)

    st.write(data["ipl"]["SOLD_PRICE"].head())  # Verify cleaned data

    st.subheader("Total Spending by IPL Teams")
    team_spending = data["ipl"].groupby("TEAM")["SOLD_PRICE"].sum().reset_index()
    fig3 = px.scatter(team_spending,
                 x="TEAM",
                 y="SOLD_PRICE",
                 size="SOLD_PRICE",
                 color="TEAM",
                 title="Total Spending by IPL Teams",
                 hover_name="TEAM",
                 size_max=60)
    st.plotly_chart(fig3)


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
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://png.pngtree.com/thumb_back/fw800/background/20240324/pngtree-cricket-background-logo-image_15687146.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
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
     
    
    st.subheader("Four and Sixes")
    
# Creating a 3D scatter plot
    #fig = px.scatter_3d(data["bat"], x="RUNS", y="FOURS", z="SIXES", 
                     #color="BATTING_TEAM", hover_data=["BATTING"],
                     #title="Runs vs Fours vs Sixes by Players")
    
    # Create two subplots
    fig = sp.make_subplots(rows=1, cols=2, subplot_titles=("Runs vs Fours", "Runs vs Sixes"), 
                        horizontal_spacing=0.15)

# First plot: Runs vs Fours
    scatter1 = px.scatter(data["bat"], x="RUNS", y="FOURS", color="BATTING_TEAM", hover_data=["BATTING"])
    for trace in scatter1.data:
      fig.add_trace(trace, row=1, col=1)

# Second plot: Runs vs Sixes
    scatter2 = px.scatter(data["bat"], x="RUNS", y="SIXES", color="BATTING_TEAM", hover_data=["BATTING"])
    for trace in scatter2.data:
      fig.add_trace(trace, row=1, col=2)

# Update layout
    fig.update_layout(title_text="Runs vs Fours and Runs vs Sixes", showlegend=True)
    fig.show()
     
    


# Displaying the figure in Streamlit
    st.plotly_chart(fig)

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
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://png.pngtree.com/thumb_back/fw800/background/20240324/pngtree-cricket-background-logo-image_15687146.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
    st.subheader("Average Economy Rate by Team")
    economy = data["bow"].groupby("BOWLING_TEAM")["ECONOMY"].mean().reset_index()
    fig7 = px.bar(economy, x="BOWLING_TEAM", y="ECONOMY", title="Average Economy Rate by Team", color="BOWLING_TEAM")
    st.plotly_chart(fig7)
    
    st.subheader("Top 10 Wicket-Takers")
    top_wickets = data["bow"].groupby("BOWLING")["WICKETS"].sum().nlargest(10).reset_index()
    #fig8 = px.bar(top_wickets, x="BOWLING", y="WICKETS", title="Top 10 Wicket-Takers")
    #st.plotly_chart(fig8)
    fig8 = px.treemap(top_wickets, path=['BOWLING'], values='WICKETS',
                            title='Top 10 Wicket-Takers (Treemap)')
    st.plotly_chart(fig8)
 

    # Additional Bowling Insights
    st.subheader("Top 5 Best Economy Rate Bowlers")
    top_economy_bowlers = data["bow"].nsmallest(5, "ECONOMY")[["BOWLING", "ECONOMY"]]
    fig9_dot = px.strip(top_economy_bowlers, x="ECONOMY", y="BOWLING", 
                      title="Top 5 Best Economy Rate Bowlers (Dot Plot)",
                      orientation='h',  # Horizontal orientation for better readability
                      color="BOWLING")
    st.plotly_chart(fig9_dot)

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
        data=save_fig_as_image(fig9_dot),
        file_name="top_best_economy_bowlers.png",
        mime="image/png"
    )

# Match Analysis
elif selected == "Match Analysis":
    st.title("🏆 World Cup Match Analysis")
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://png.pngtree.com/thumb_back/fw800/background/20240324/pngtree-cricket-background-logo-image_15687146.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
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
def cricket_quiz():
    st.title("🎮 Cricket Quiz Game")
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://media1.giphy.com/media/9m4yAf60N6uRcLiWFU/giphy.gif");
        background-position: right center;  /* Align the image to the right */
        background-repeat: no-repeat;  /* Prevent the GIF from repeating */
        background-size: ;  /* Scale the GIF to fit within the container */
        height: 100vh;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    
    
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
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://media1.tenor.com/m/YgBHa5IgmhwAAAAC/aggressive-trending.gif");
        background-position: right center; /* Aligns the image to the right */
        background-size: auto; /* Ensures the background image covers the entire height */
        height: 100vh; /* Makes the container take the full height of the screen */
        background-repeat: no-repeat; /* Prevents the background from repeating */
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
    meme_urls = [
        #"https://media1.tenor.com/m/dq4CBxSKxawAAAAd/striker-saini.gif"  # Cricket batsman hit
        "https://media1.tenor.com/m/DEiXgXvrHzgAAAAC/dhoni-gif.gif",  # Umpire gesture
        "https://media.tenor.com/w8mhB_o1iAUAAAAC/out-gif.gif",  # Players hugging
        #"https://media1.tenor.com/m/l1iKhSUAdRoAAAAC/cheating-at-cricket-do-not-scratch-your-balls.gif",  # Cricket catch
    ]

    # Display memes/GIFs in a grid layout for better presentation
    cols = st.columns(3)  # Create 3 columns
    for i, url in enumerate(meme_urls):
        with cols[i % 3]:  # Place each item in a column
            st.image(url, use_container_width=True)




 #Player Performance Correlation
elif selected == "Player Performance Correlation":

    st.title("📊 Player Performance Correlation")
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpaperaccess.com/full/3076836.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
    # Create Age vs Runs Scored plot using Plotly
    st.subheader('Age vs Runs Scored')
    fig1 = px.scatter(ipl, x='AGE', y='Runs', color='TEAM', title='Age vs Runs Scored', 
                      labels={'AGE': 'Age', 'Runs': 'Runs Scored'}, 
                      color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig1)

    # Create Paying Role vs Sold Price box plot using Plotly
    st.subheader('Paying Role vs Sold Price')
    fig2 = px.box(ipl, x='Paying_Role', y='SOLD_PRICE', title='Paying Role vs Sold Price', 
                  labels={'Paying_Role': 'Paying Role', 'SOLD_PRICE': 'Sold Price'}, 
                  color='Paying_Role', color_discrete_sequence=px.colors.qualitative.Set2)
    fig2.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels for better readability
    st.plotly_chart(fig2)

    # Download button for Player Correlation Data
    st.sidebar.download_button(
        label="Download Player Correlation Data",
        data=ipl.to_csv(index=False),
        file_name="player_correlation_data.csv",
        mime="text/csv"
    )

    # Function to save Plotly figures as images
    def save_fig_as_image(fig):
        img_bytes = BytesIO()
        pio.write_image(fig, img_bytes, format='png')
        img_bytes.seek(0)
        return img_bytes

    # Download Figures as images
    st.sidebar.download_button(
        label="Download Age vs Runs Chart",
        data=save_fig_as_image(fig1),
        file_name="age_vs_runs.png",
        mime="image/png"
    )

    st.sidebar.download_button(
        label="Download Paying Role vs Sold Price Chart",
        data=save_fig_as_image(fig2),
        file_name="paying_role_vs_sold_price.png",
        mime="image/png"
    )




# Visualized Story
elif selected == "Visualized Story":
    st.title("📖 Cricket Data Story: The Boy Who Discovered the Magic of Cricket 🏏")
        # Define page background image with CSS
    page_element = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://wallpaperaccess.com/full/1878537.jpg");
        background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)
    # Add Manga-Style Image of Rohan's Journey
    st.image(r"C:\Users\ajayj\Desktop\courses\data viz\cccc.png",caption="Rohan's Journey into Cricket",use_container_width =True)
    st.image(r"C:\Users\ajayj\Desktop\courses\data viz\ChatGPT Image Mar 31, 2025, 11_38_28 PM.png", 
         caption="Rohan's Journey into IPL Data", 
         use_container_width =True)
    st.image(r"C:\Users\ajayj\Desktop\courses\data viz\0.png", 
         caption="Rohan's Journey into Wining Games ", 
         use_container_width =True)
    st.image(r"C:\Users\ajayj\Desktop\courses\data viz\bb.PNG",caption="Rohan Learning about World Cup Bowlers",use_container_width=True)

    # Introduction
    st.markdown("""
        ## The Curious Journey of a Young Cricket Enthusiast 🌱
        Once upon a time, there was a boy named Rohan. He had heard about cricket but never understood the magic behind it. One day, he stumbled upon some cricket data, and his journey of discovery began. Let's dive into his adventure!
    """)

    # 1. Rohan Discovers IPL Auctions 💰
    st.header("💰 IPL Auctions: Rohan's First Glimpse into the Strategy of Teams")
    st.markdown("""
        Rohon’s IPL Discovery Journey

       Rohon was never much into cricket, but one day, he overheard his friends passionately debating IPL team strategies. Curious, he decided to explore what made IPL so exciting. He started with the basics—learning about the teams, their star players, and, most importantly, how team owners spend big money on players during auctions.

One evening, he came across a chart that showed how much each IPL team spent on players. At first glance, it looked like a colorful bar graph, but as he dived deeper, he noticed some interesting patterns.

Some teams, like Sunrisers Hyderabad (SRH) and Rajasthan Royals (RR), spent the most, stacking their squads with expensive players.

Others, like Chennai Super Kings (CSK) and Delhi Capitals (DC), had more conservative spending, possibly relying on experienced players rather than buying new ones.

Teams like Mumbai Indians (MI) and Royal Challengers Bangalore (RCB) had a balanced approach—spending well but not going overboard.

Rohon realized that IPL auctions are like a high-stakes strategy game, where teams invest smartly to build their dream squads. With this newfound knowledge, he could finally join his friends' cricket debates, impressing them with insights into how money shapes the IPL teams!

And just like that, Rohon wasn’t just a casual viewer anymore—he was hooked on the IPL!🤔
    """)
    
    st.subheader('Paying Role vs Sold Price')
    fig2 = px.box(ipl, x='Paying_Role', y='SOLD_PRICE', title='Paying Role vs Sold Price', 
                  labels={'Paying_Role': 'Paying Role', 'SOLD_PRICE': 'Sold Price'}, 
                  color='Paying_Role', color_discrete_sequence=px.colors.qualitative.Set2)
    fig2.update_layout(xaxis_tickangle=-45)  # Rotate x-axis labels for better readability
    st.plotly_chart(fig2)

    st.markdown("""
        **Key Takeaway:** Rohan noticed that teams like Mumbai Indians and Chennai Super Kings spent a lot, while others took a more balanced approach. It was clear that team strategies and budget management played a big role in IPL success. 💡

        **Interactive Insight:** Hover over the bars to see the exact spending for each team. What do you think? Which teams do you believe have the best spending strategies?
    """)

    # 2. Batting Brilliance: Rohan Becomes a Fan of the Power Hitters 🏏
    st.header("🏏 Batting Brilliance: Rohan's Deep Dive into Runs and Strike Rates")
    st.markdown("""
        As Rohan explored more cricket data, he got curious about the batsmen's performance. He wanted to understand how runs and strike rates correlated. Was a higher strike rate always a good sign? Let's see what he found out!
    """)
    
    fig_batting_runs_strike = px.scatter(data["bat"], x="RUNS", y="STRICK RATE", color="BATTING_TEAM", hover_data=["BATTING"], title="Runs vs Strike Rate")
    st.plotly_chart(fig_batting_runs_strike)

    st.markdown("""
        **Rohan's Discovery:** He learned that high runs and strike rates made some players stand out as game-changers. But not all the time – some players played steadily, focusing on partnerships and innings stability. **Which player do you think is the most efficient?**
    """)

    # 3. Bowling: Rohan Decodes Team Strategies 🎯
    st.header("🎯 Bowling Mastery: How Teams Control the Game")
    st.markdown("""
        Rohan's next discovery was about bowling. He wanted to figure out how bowling economy rates could influence a team's success. Were the most successful teams the ones with the best bowlers? Let's find out!
    """)
    
    economy = data["bow"].groupby("BOWLING_TEAM")["ECONOMY"].mean().reset_index()
    fig_bowling_economy = px.bar(economy, x="BOWLING_TEAM", y="ECONOMY", title="Average Economy Rate by Team", color="BOWLING_TEAM")
    st.plotly_chart(fig_bowling_economy)

    st.markdown("""
        **Rohan's Insight:** A lower economy rate indicated that teams were controlling the game, keeping the opposition's runs in check. Teams with the best bowlers often had the most success! 🏆

        **Quiz Time:** Which team do you think has the best bowling attack based on the economy rate? Drop your guesses below!
    """)

    

    # The Future of Cricket Analytics: What Will Rohan Discover Next? 🌟
    st.header("🌟 The Future of Cricket Analytics: Rohan's Ongoing Adventure")
    st.markdown("""
        As Rohan's journey continues, he’s excited about the future of cricket analytics. With more data and better tools like Power BI and Tableau, the insights into cricket will only get deeper and more detailed. Who knows? Maybe he will discover new trends that will change the way we view the game forever! 🚀
    """)

    # 5. Integrating Power BI & Tableau Dashboards 📊
    st.header("📊 Power BI Dashboard: A More Detailed Adventure")
    st.markdown("""
        Want to explore even more data? Rohan invites you to explore his Power BI dashboard for a deeper dive into cricket stats. Click below to see what’s in store!
    """)
    power_bi_link = "https://app.powerbi.com/view?r=eyJrIjoiYjk2ZmI3NjYtMTI3OC00MmYxLWE0MGEtYjllZjQ3NTE0MTUzIiwidCI6IjcwZGUxOTkyLTA3YzYtNDgwZi1hMzE4LWExYWZjYmEwMzk4MyIsImMiOjN9"  # Replace with your Power BI embed link
    st.components.v1.iframe(power_bi_link, height=600, scrolling=True)

    

    # Download all figures for users
    st.sidebar.download_button(
        label="Download paying Spending Chart",
        data=save_fig_as_image(fig2),
        file_name="ipl_team_spending.png",
        mime="image/png"
    )
    st.sidebar.download_button(
        label="Download Runs vs Strike Rate Chart",
        data=save_fig_as_image(fig_batting_runs_strike),
        file_name="runs_vs_strike_rate.png",
        mime="image/png"
    )
    st.sidebar.download_button(
        label="Download Economy Rate Chart",
        data=save_fig_as_image(fig_bowling_economy),
        file_name="economy_rate_by_team.png",
        mime="image/png"
    )
 
    