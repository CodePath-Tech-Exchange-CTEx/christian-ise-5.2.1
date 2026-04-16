import streamlit as st


def init_session():
    if st.session_state.get("logged_in") is None:
        st.session_state["logged_in"] = False


def login():
    st.session_state.logged_in = True


def logout():
    st.session_state.logged_in = False


def render_sidebar():
    if st.session_state.logged_in:
        st.sidebar.success("Logged in")
        st.sidebar.button("Log out", on_click=logout)
    else:
        st.sidebar.warning("Not logged in")
        st.sidebar.button("Log in", on_click=login)

    st.sidebar.write("This site is copyright Fake Company LLC Inc., 2024")


def render_footer():
    with st.expander("Company Info"):
        st.write("Fake Company LLC Inc. is located at 1600 Amphitheatre Parkway Mountain View, CA 94043")

    with st.expander("Links"):
        st.markdown(
            """
            [Google](https://google.com)

            [Gemini](https://gemini.google.com)

            [Streamlit Docs](https://docs.streamlit.io/)
            """
        )