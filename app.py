import streamlit as st


st.title("~ Books by Vibe ~")
vibe = st.text_input("What's your vibe?")
st.session_state["vibe"] = vibe

if st.session_state["vibe"] != "":
    st.write("Searching for books...")
    st.write(f"Match vibe: {vibe}")
    # Use Google Books API to search for books
    # Try using the vibe as the search query and see what happens
    # If that fails (high chance), search for a better way
    # Try, try again and don't give up on this one!