import streamlit, pandas, requests, snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# fruit list from S3 bucket
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

# allow the user to pick some fruits from the list
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Banana', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display the table on the page
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit to get information.')
  else:
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

# adding a stop so that we can troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets['snowflake'])
my_cur = my_cnx.cursor()
my_cur.execute('SELECT * FROM fruit_load_list')
my_data_rows = my_cur.fetchall()
streamlit.header('The fruit load list contains:')
streamlit.dataframe(my_data_rows)

# allow a user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?', 'jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)
# insert the fruit into the fruit load list
# THIS WON'T WORK BUT GO WITH IT FOR THE DEMO AND LEARNING
my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlit')")
