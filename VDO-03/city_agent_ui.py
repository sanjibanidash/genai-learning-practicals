import streamlit as st

from city_agent import agent


st.set_page_config(
    page_title="City Intelligence Agent",
    page_icon="🌍"
)

st.title("🌍 City Intelligence Agent")
st.write("Ask about weather and the latest news for any city.")


query = st.text_input(
    "Enter your question:",
    placeholder="What is the weather in Delhi and the latest news about Delhi?"
)


if st.button("Ask Agent"):

    if query:

        with st.spinner("Agent is working..."):

            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": query
                        }
                    ]
                }
            )

        final_message = result["messages"][-1]

        st.subheader("Answer")

        if isinstance(final_message.content, list):
            st.write(final_message.content[0]["text"])
        else:
            st.write(final_message.content)

    else:
        st.warning("Please enter a question.")