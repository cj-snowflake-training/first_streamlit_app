import streamlit, pandas

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# fruit list from S3 bucket
fruits_selected = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
fruits_to_show = my_fruit_list.loc[fruits_selected]

# allow the user to pick some fruits from the list
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Banana', 'Strawberries'])

# display the table on the page
streamlit.dataframe(my_fruit_list)
