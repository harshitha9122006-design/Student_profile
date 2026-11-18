import streamlit as st
from groq import Groq
st.set_page_config(page_title="Student Profile Application",page_icon="🎓",layout="centered")
st.title("Student Profile Application")
st.caption("Developed by Student Name")
st.caption("Launched by Harshitha K T")
st.info("Fill in your details and click View My Profile.")
name=st.text_input("Student Name",placeholder="Enter your name")
roll=st.text_input("USN/Roll Number",placeholder="Enter roll number")
dept=st.selectbox('Department',['CSE','ISE','ECE','EEE','ME','CE','AIDS','AIML'])
year=st.radio('Year',['1st Year','2nd Year','3rd Year','4th Year'])
if st.button('View My Profile'):
   if name=="" or roll=="":
     st.warning("Please enter your name and roll number")
else:
  st.success("Profile Submitted Successfully")
