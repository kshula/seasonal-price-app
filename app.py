# import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
import datetime

# Load the data
data = pd.read_csv('data.csv')
data['Month'] = pd.to_datetime(data['Month'], format='%d/%m/%Y')
data.set_index('Month', inplace=True)

# Function to calculate Mean Absolute Percentage Error (MAPE)
def calculate_mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Home Page
if st.sidebar.button('Home'):
    st.title('Welcome to the Seasonal Analysis App - Ubunga AI')
    st.write("""
    This interactive app is designed to provide valuable insights into seasonal trends for various products over time. Whether you're a business owner, analyst, or enthusiast, the Seasonal Analysis App empowers you to:

    - **Visualize Trends:** Explore and visualize the historical trends of different products over months or years using interactive line charts.

    - **Forecast Future Trends:** Leverage advanced time series forecasting techniques, such as SARIMA modeling, to predict the future values of your selected product.

    - **Evaluate Model Accuracy:** Assess the performance of the forecasting model with metrics like Mean Squared Error (MSE) and Mean Absolute Percentage Error (MAPE).

    - **Monthly Metrics Overview:** Gain a quick overview of each product's monthly performance, including average monthly percentage increase and delta, providing actionable insights.

    - **User-Friendly Interface:** Easily navigate through the app with a user-friendly interface and interactive components.

    - **Customization:** Select specific products for analysis, tailor visualizations to your needs, and view detailed metrics for informed decision-making.

    Whether you're interested in understanding market trends, optimizing inventory, or making data-driven decisions, the Seasonal Analysis App is here to support your analytical needs.

    Explore the features, analyze trends, and uncover valuable insights with this powerful and intuitive tool.

    Start by selecting products on the sidebar to explore the visualizations and analysis pages. Have a great analytical journey!
    
    ---

    **About the Creator:**
    
    Hi, I'm Kampamba Shula, the creator of this app. I am passionate about data analysis and helping businesses make informed decisions through data-driven insights.

    **Contact Information:**
    
    Feel free to reach out if you have any questions, feedback, or suggestions:
    
    - Email: kampambashula@gmail.com
    - LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/kampamba-shula-03946633/)
    - GitHub: [GitHub Profile](https://github.com/kshula)
    
    """)
# Sidebar for product selection
selected_products = st.sidebar.multiselect('Select Products', data.columns)

# Visualisation Page
if st.sidebar.checkbox('Show Visualisation'):
    st.subheader('Visualisation Page')

    # Plotting selected products over time
    if selected_products:
        fig = px.line(data, x=data.index, y=selected_products, title='Product Trends Over Time')
        st.plotly_chart(fig)
    else:
        st.warning('Please select at least one product.')

# Analysis Page
if st.sidebar.checkbox('Show Analysis'):
    st.subheader('Analysis Page')

    # Select a product for analysis
    selected_product = st.selectbox('Select a Product for Analysis', selected_products)

    if selected_product:
        st.write(f"### Analysis for {selected_product}")

        # SARIMA Model
        st.write("#### SARIMA Model")

        # Train SARIMA model on the entire dataset
        model_sarima = SARIMAX(data[selected_product], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        fit_sarima = model_sarima.fit()

        # Predict next three months
        forecast_start_date = data.index[-1] + pd.DateOffset(months=1)
        forecast_end_date = forecast_start_date + pd.DateOffset(months=2)
        forecast_dates = pd.date_range(forecast_start_date, forecast_end_date, freq='MS')
        predictions_sarima = fit_sarima.get_forecast(steps=3)
        forecast_values = predictions_sarima.predicted_mean

        # Display predicted values in a line chart
        st.line_chart(pd.concat([data[selected_product], forecast_values], axis=1))

        # Evaluate SARIMA model
        mse_sarima = mean_squared_error(data[selected_product], fit_sarima.fittedvalues)
        mape_sarima = calculate_mape(data[selected_product], fit_sarima.fittedvalues)

        st.write(f"##### Model Evaluation Metrics:")
        st.write(f"- **SARIMA Model:** Mean Squared Error: {mse_sarima:.2f}, MAPE: {mape_sarima:.2f}%")

        # Calculate month-on-month percentage increase and delta
        monthly_percentage_increase = data[selected_product].pct_change() * 100
        delta = data[selected_product].diff()

        # Display metrics for each product
        st.write("#### Monthly Metrics:")

        # Define colors based on the sign of the delta
        delta_color_increase = "red"
        delta_color_decrease = "green"

        # Set delta_color based on the sign of the delta
        delta_color_percentage_increase = delta_color_increase if monthly_percentage_increase.mean() >= 0 else delta_color_decrease
        delta_color_delta = delta_color_increase if delta.mean() >= 0 else delta_color_decrease

        # Define the HTML code for displaying metrics with custom colors
        html_code_percentage_increase = f'<p style="color:{delta_color_percentage_increase};">Average Monthly Percentage Increase: {monthly_percentage_increase.mean():.2f}%</p>'
        html_code_delta = f'<p style="color:{delta_color_delta};">Delta: {delta.mean():.2f}</p>'

        # Display HTML code
        st.markdown(html_code_percentage_increase, unsafe_allow_html=True)
        st.markdown(html_code_delta, unsafe_allow_html=True)



