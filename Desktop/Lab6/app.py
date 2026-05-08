import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


st.title("Streamlit Data Visualization Dashboard")

# CACHE DATA

@st.cache_data
def load_train_data():
    return pd.read_csv("train.csv", nrows=1000)

@st.cache_data
def load_center_data():
    return pd.read_csv("fulfilment_center_info.csv")

@st.cache_data
def load_meal_data():
    return pd.read_csv("meal_info.csv")

# Load datasets
train_data = load_train_data()
center_data = load_center_data()
meal_data = load_meal_data()


# WEEKLY DEMAND DATA

st.header("Weekly Demand Data")

st.subheader("Number of Orders Bar Chart")
st.bar_chart(train_data['num_orders'])

st.subheader("Line Chart")
st.line_chart(train_data['num_orders'])

# Histogram
st.subheader("Histogram of Number of Orders")

fig, ax = plt.subplots()
train_data['num_orders'].hist(ax=ax, bins=30)

st.pyplot(fig)

# Area chart
st.subheader("Area Chart")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.area_chart(chart_data)


# FULFILLMENT CENTER DATA

st.header("Fulfillment Center Data")

if st.checkbox("Show Center Information data"):
    st.write(center_data)

# Region code chart
st.subheader("Region Code Distribution")

region_counts = center_data['region_code'].value_counts()

st.bar_chart(region_counts)

# Center type chart
st.subheader("Center Type Distribution")

center_type_counts = center_data['center_type'].value_counts()

st.bar_chart(center_type_counts)

# Plotly Distribution Plot
st.subheader("Distribution Plot")

hist_data = [train_data['num_orders']]
group_labels = ['num_orders']

fig2 = ff.create_distplot(hist_data, group_labels)

st.plotly_chart(fig2)


# MEAL DATA

st.header("Meal Data")

st.subheader("Cuisine Distribution")

cuisine_counts = meal_data['cuisine'].value_counts()

st.bar_chart(cuisine_counts)


if st.button("Click to see Categories of Meal"):
    
    st.subheader("Meal Categories")
    
    category_counts = meal_data['category'].value_counts()
    
    st.bar_chart(category_counts)



st.success("Dashboard Loaded Successfully!")