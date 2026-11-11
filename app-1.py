import streamlit as st

st.title("WASHROOM FACILITIES MANAGEMENT PROGRAM")
st.write("--------------------------------------")

facilities = st.selectbox(
    "Are the washroom facilities adequate?",
    ["Yes", "No"]
)

if facilities == "No":
    st.warning("Construct additional washroom facilities.")
else:
    st.success("Continue regular maintenance.")

water = st.selectbox(
    "Is the water supply reliable?",
    ["Yes", "No"]
)

if water == "No":
    st.warning("Provide a reliable water supply.")
else:
    st.success("Continue monitoring the water supply.")

cleanliness = st.selectbox(
    "Are the washrooms clean and well maintained?",
    ["Yes", "No"]
)

if cleanliness == "No":
    st.warning("Improve cleaning and repair damaged facilities.")
else:
    st.success("Continue regular cleaning and maintenance.")

hygiene = st.selectbox(
    "Are soap, tissue and enough waste bins available?",
    ["Yes", "No"]
)

if hygiene == "No":
    st.warning("Provide soap, tissue and enough waste bins.")
else:
    st.success("Continue supplying hygiene materials.")

st.write("--------------------------------------")
st.info("Inspect the washrooms regularly.")
st.write("PROGRAM ENDED")
