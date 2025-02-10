Here's a basic README for your Streamlit project that incorporates the custom theme setup:

---

# Streamlit Cricket Analytics Dashboard

This is an interactive Streamlit app that provides various cricket analytics, including IPL player data, World Cup batting and bowling stats, and match analysis. The app allows you to explore datasets related to cricket in an engaging and visually appealing way.

## Features

- **IPL Analysis**: Visualize player sold prices and total spending by IPL teams.
- **World Cup Batting Analysis**: Explore the relationship between runs and strike rate for batting teams.
- **World Cup Bowling Analysis**: Analyze economy rates and wicket statistics.
- **Match Analysis**: View World Cup wins by team and team performance over time.

## Getting Started

### Prerequisites

To run the Streamlit app, ensure you have the following installed:

- Python 3.7 or later
- Streamlit
- Pandas
- Plotly

You can install the necessary dependencies by running:

```bash
pip install streamlit pandas plotly
```

### Installation

1. Clone or download this repository to your local machine.
   
2. Install the required dependencies (if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

3. Download the datasets from the provided sources and place them in the `data/` folder in your project directory.

4. Configure the theme by creating a `.streamlit` folder in the same directory as the `streamlit_app.py` file and add the `config.toml` file with the following content:

   ```toml
   [theme]
   # Primary accent color for interactive elements.
   primaryColor = "#E694FF"

   # Background color for the main content area.
   backgroundColor = "#00172B"

   # Background color used for the sidebar and most interactive widgets.
   secondaryBackgroundColor = "#0083B8"

   # Color used for almost all text.
   textColor = "#FFF"

   # Font family for all text in the app, except code blocks. One of "sans serif", "serif", or "monospace".
   font = "sans serif"
   ```

   Your directory structure should look like this:

   ```
   your_project_directory/
   ├── .streamlit/
   │   └── config.toml
   ├── streamlit_app.py
   └── data/
       ├── IPL dataset final.csv
       ├── BATTING.csv
       ├── BOWLING.csv
       ├── Cricket_WC23.csv
       └── PLAYERS_INFO.csv
   ```

### Running the App

After setting up the dependencies and datasets:

1. Navigate to the project directory in your command line or terminal.

2. Run the Streamlit app:

   ```bash
   streamlit run streamlit_app.py
   ```

3. The app should open in your default web browser.

## App Interface

- **Sidebar**: Choose the analysis tab and select your preferred color theme (Light, Dark, or Kickass).
- **Charts**: Interactive visualizations for various cricket metrics like runs, wickets, player performance, and match outcomes.
- **Download Data**: Download raw dataset CSV files directly from the sidebar for further exploration.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
