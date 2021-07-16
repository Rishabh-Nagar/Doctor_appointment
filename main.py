# core packages
import streamlit as st

import hashlib

# DB
from manage_db_doctor import *
from manage_db_patient import *
from current_doctor import *


def generate_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def verify_hashes(password, hashed_text):
    if generate_hashes(password) == hashed_text:
        return hashed_text
    return False


def main():
    """Instant Chat Application"""
    st.title("Doctor Appointment Application")

    menu = ["Home", "Login", "SignUp", "Contact Us", "About Us"]
    type = ["Login As Patient", "Login As Doctor"]
    type1 = ["Sign Up As Patient", "Sign Up As Doctor"]
    act_doc = ["Profile", "Appointment Status"]
    act_pat = ["Book Appointment", "Appointment Status", "Available Doctor"]
    sex = ["Male", "Female"]
    doctor_type = ["Cardiologist", "Audiologist", "Dentist", "ENT specialist"]

    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        st.subheader("Home")
        st.text("Book an Appointment")

    elif choice == "Login":
        choice1 = st.sidebar.selectbox("Login Type", type)
        if choice1 == "Login As Patient":
            patient_username = st.sidebar.text_input("Username")
            patient_password = st.sidebar.text_input("Password", type='password')
            if st.sidebar.checkbox("Login As Patient"):
                create_patient_table()
                hashed_patient_password = generate_hashes(patient_password)
                result_patient = login_patient(patient_username, verify_hashes(patient_password, hashed_patient_password))
                if result_patient:
                    # if patient_password == "12345":
                    st.success("Welcome {}".format(patient_username))

                    activity_patient = st.selectbox("Activities", act_pat)
                    if activity_patient == "Book Appointment":
                        st.subheader("Book Appointment")
                    elif activity_patient == "Appointment Status":
                        st.subheader("Appointment Status")
                    else:
                        st.subheader("Available Doctor")
                else:
                    st.warning("Incorrect Username/Password")

        else:
            doctor_username = st.sidebar.text_input("Username")
            doctor_password = st.sidebar.text_input("Password", type='password')
            if st.sidebar.checkbox("Login As Doctor"):
                create_doctor_table()
                hashed_doctor_password = generate_hashes(doctor_password)
                result_doctor = login_doctor(doctor_username, verify_hashes(doctor_password, hashed_doctor_password))
                # if doctor_password == "12345":
                if result_doctor:
                    st.success("Welcome {}".format(doctor_username))

                    activity_doctor = st.selectbox("Activites", act_doc)
                    if activity_doctor == "Profile":
                        st.subheader("Profile")
                        name = st.text_input("Name")
                        age = st.number_input("Age")
                        sex = st.selectbox("Sex", sex)
                        degree = st.text_input("Degree Name")
                        cur_hosp = st.text_input("Current Hospital(in which you are working)")
                        if st.button("Save"):
                            create_current_doctor_table()
                            add_current_doctor_data(name, age, sex, degree, cur_hosp)
                            st.success("Your Profile is Successfully saved")


                    else:
                        st.subheader("Appointment Status")

                else:
                    st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        choice2 = st.sidebar.selectbox("Login Type", type1)
        if choice2 == "Sign Up As Patient":
            new_patient_username = st.text_input("User name")
            new_patient_password = st.text_input("Password", type='password')

            confirm_patient_password = st.text_input("Confirm Patient Password", type='password')
            if new_patient_password == confirm_patient_password:
                st.success("Password Confirmed")
            else:
                st.warning("Password does not match")

            if st.button("Submit"):
                create_patient_table()
                hashed_new_patient_password = generate_hashes(new_patient_password)
                add_patient_data(new_patient_username, hashed_new_patient_password)
                st.success("You Have Successfully created an account")
                st.info("Login to get Started")

        else:
            new_doctor_username = st.text_input("Username")
            new_doctor_password = st.text_input("Password", type='password')

            confirm_doctor_password = st.text_input("Confirm Doctor Password", type='password')
            if new_doctor_password == confirm_doctor_password:
                st.success("Password Confirmed")
            else:
                st.warning("Password does not match")

            if st.button("Submit"):
                create_doctor_table()
                hashed_new_doctor_password = generate_hashes(new_doctor_password)
                add_doctor_data(new_doctor_username, hashed_new_doctor_password)
                st.success("You Have Successfully created an account")
                st.info("Login to get Started")

    elif choice == "About Us":
        st.subheader("Our Vision")
        st.write("Enable healthcare businesses to provide superior healthcare delivery and patient care with technology – globally")
        st.subheader("Our Mission")
        st.write("Provide a scalable, secure platform to clinics and hospitals that provide great value at reasonable cost")

    elif choice == "Contact Us":
        st.subheader("Contact Details")





if __name__ == "__main__":
    main()
