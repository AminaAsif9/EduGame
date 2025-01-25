import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="EduGame", page_icon=":books:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_bot = load_lottieurl("https://lottie.host/668636f4-92fc-4f23-bc3b-4cc4a00e3604/fNTNcqHty9.json")
lottie_main = load_lottieurl("https://lottie.host/accf15ff-6219-42b5-af4b-51d5adf09168/dUSw7cGNNG.json")

# ---- HEADER SECTION ----
with st.container():
    st_lottie(lottie_main, height=350, key="main")
    st.title("🤖 EduGame")    
    # st.write("##")
    st.subheader("Hi, I am EduBot :wave:")
    st.write(
        " An adaptive learning tool, here to personalize the learning experience for you."
    )

# ---- SECTION ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Try Edu!")
        st.write("##")


        # File Upload
        uploaded_file = st.file_uploader("Upload your file", type=["txt", "pdf", "docx"])

        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # React to user input
        if prompt := st.chat_input("Ask your question?"):
            # Display user message in chat message container
            st.chat_message("user").markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            response = f"{prompt}"
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})



    with right_column:
        st_lottie(lottie_bot, height=300, key="bot")

# ---- MAIN ----
with st.container():
    st.write("##")
    st.write("---")
    st.header("What I do?")
    st.write(
            """
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Facilis, ducimus nesciunt nam vero nulla esse: 
            - (add details, if needed)
            - are looking for a way to .............
            - are struggling with tasks ...........
            - want to learn ...................
            - Iure facere unde explicabo, cumque animi doloribus commodi voluptatibus deleniti? Iste ullam voluptatibus maiores accusamus.

            Sounds interesting?
            """
    )
   