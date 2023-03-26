
import streamlit as st

import psycopg2

def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn=init_connection()



st.title("Teeny Tiny Bee")

menu = ['Home', 'Products', 'Product Category', 'Product Subcategory', 'Shopping cart', 'Checkout', 'Payment']
choice = st.sidebar.selectbox("Select a Page", menu)

if choice == 'Home':
    st.write("Welcome to the Teeny Tiny Bee!! :bee:")
    st.write("Here you can find a variety of hand made cold-process soaps and tools to get started making your own.")

