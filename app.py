import streamlit as st
import py_simple as ps
import requests


ENDPOINT = "https://openlibrary.org/search.json"


st.title("~ Books by Vibe ~")
vibe = st.text_input("What's your vibe?")
st.session_state["vibe"] = vibe

if st.session_state["vibe"] != "":
    st.write("Searching for books...")
    st.write(f"Match vibe: {vibe}")
    try:
        result = requests.get(ENDPOINT + f"?q={vibe}")
        authors = []
        titles = []
        for i in range(3):
            authors.append(result.json()['docs'][i]['author_name'])
            titles.append(result.json()['docs'][i]['title'])

        st.write(f"authors: {authors}")
        st.write(f"titles: {titles}")
    except Exception as e:
        st.write("Sorry couldn't get a match...")

    # Try, try again and don't give up on this one!