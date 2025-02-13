import streamlit as st
from PIL import Image
import utils

def initialize_session_state():
    st.session_state.setdefault('history', [])
    st.session_state.setdefault('generated', ["Hello! Feel free to ask anything from Database!"])
    st.session_state.setdefault('past', ["Hi Man! How you Doin'!"])

def display_chat(conversation_chain, chain):
    st.markdown("<h2 style='text-align: center; color: white;'>💬 AI Chat Bot</h2>", unsafe_allow_html=True)

    reply_container = st.container()
    container = st.container()

    with container:
        user_input = st.chat_input("Come on.. Ask me!")
        if user_input:
            generate_response(user_input, conversation_chain, chain)

    display_generated_responses(reply_container)


def generate_response(user_input, conversation_chain, chain):
    with st.spinner('Wait.. Let me think...'):
        output = conversation_chat(user_input, conversation_chain, chain, st.session_state['history'])

    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

def conversation_chat(user_input, conversation_chain, chain, history):
    response = conversation_chain.invoke(user_input)
    final_response = chain.invoke(f"Based on the information, generate a human-readable answer: {response['query']}, {response['result']}")

    history.append((user_input, final_response))
    return final_response

def display_generated_responses(reply_container):
    if st.session_state['generated']:
        with reply_container:
            for i in range(len(st.session_state['generated'])):
                with st.chat_message("user"):
                    st.markdown(f"👤 **You:** {st.session_state['past'][i]}")
                with st.chat_message("assistant"):
                    st.markdown(f"🤖 **Bot:** {st.session_state['generated'][i]}")

def main():
    initialize_session_state()

    st.markdown("""
        <style>
        body {
            background-color: #1E1E1E;
            color: white;
        }
        .stChatMessage {
            padding: 10px;
            border-radius: 10px;
        }
        .stChatMessage.user {
            background-color: #0084ff;
            color: white;
            text-align: right;
        }
        .stChatMessage.assistant {
            background-color: #282c34;
            color: white;
            text-align: left;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        image = Image.open('chatbot.png')
        st.image(image, width=150)

    conversation_chain, chain = utils.create_conversational_chain()
    display_chat(conversation_chain, chain)

if __name__ == "__main__":
    main()