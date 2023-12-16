# Seasonal Analysis App Documentation

## Overview

The Seasonal Analysis App is an interactive tool designed to provide valuable insights into seasonal trends for various products over time. Whether you're a business owner, analyst, or enthusiast, this app empowers you to explore, visualize, and analyze historical trends, forecast future trends, and evaluate model accuracy. The data is based on Zambian data from the central statistics office monthly bulletins.

## Features

- **Visualize Trends:** Explore and visualize the historical trends of different products over months or years using interactive line charts.

- **Forecast Future Trends:** Leverage advanced time series forecasting techniques, such as SARIMA modeling, to predict the future values of your selected product.

- **Evaluate Model Accuracy:** Assess the performance of the forecasting model with metrics like Mean Squared Error (MSE) and Mean Absolute Percentage Error (MAPE).

- **Monthly Metrics Overview:** Gain a quick overview of each product's monthly performance, including average monthly percentage increase and delta, providing actionable insights.

- **User-Friendly Interface:** Easily navigate through the app with a user-friendly interface and interactive components.

- **Customization:** Select specific products for analysis, tailor visualizations to your needs, and view detailed metrics for informed decision-making.

## Usage

1. **Home Page:**
    - Overview of the app's features and benefits.
    - Information about the creator and contact details.

2. **Visualisation Page:**
    - Explore and visualize historical trends of selected products using interactive line charts.
    - Use the sidebar to select products for visualization.

3. **Analysis Page:**
    - Analyze trends, forecast future values, and evaluate model accuracy.
    - Use the sidebar to select a product for detailed analysis.

## Creator and Contact Information

- **Creator:** Kampamba Shula
- **Email:** kampambashula@gmail.com
- **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/kampamba-shula-03946633/)
- **GitHub:** [GitHub Profile](https://github.com/kshula)

## Getting Started

To run the app locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/kshula/seasonal-analysis-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd seasonal-analysis-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    streamlit run app.py
    ```

## Dependencies

- Streamlit
- Pandas
- NumPy
- Plotly
- Statsmodels
- Scikit-learn

## Acknowledgments

- Special thanks to the [Streamlit](https://streamlit.io/) team for providing an excellent platform for creating data apps.

Feel free to explore, analyze, and discover insights with the Seasonal Analysis App!
