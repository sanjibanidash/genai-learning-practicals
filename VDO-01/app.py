import streamlit as st
from ui_core import structured_model

st.title("🎬 Movie Information Extractor")

paragraph = st.text_area("Enter a movie paragraph:")

if st.button("Extract Data"):
    response = structured_model.invoke(paragraph)

    st.write("### 🎬 Extracted Information")

    st.write("**Title:**", response.title)

    st.write(
        "**Genre:**",
        ", ".join(response.genre)
    )

    st.write("**Director:**", response.director)

    st.write(
        "**Cast:**",
        ", ".join(response.cast)
    )

    st.write("**Rating:**", response.rating)

    st.write("**Release Year:**", response.release_year)