import re
import streamlit as st

st.title("AI assistant")
st.text("Hello form bot!")

def main():
  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

  name = st.text_input("Your Name :", "")
  if name:
    st.text(f"Hello, {name.title()}")
    email = st.text_input("Your Email :", "")
    if re.fullmatch(regex, email):
      company = st.text_input("You comapny :", "")

      if st.button("Send"):
        st.text_area("Chatbot :", {"name": name, "email": email, "company": company}, height=100)

    elif email:
      st.write("Email is not valid")


if __name__ == "__main__":
  main()

