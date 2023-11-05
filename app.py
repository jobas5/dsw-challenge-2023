import numpy as np
import streamlit as st
import pickle as pkl


if __name__ == '__main__':
    st.title('Aplikasi Churn Analysis :writing_hand:')

    with st.form('Feature Audio Analysis'):
        st.write('Input Features')
        tenure_month = st.number_input('Tenure Month: ', value=0, step=1)
        location = st.number_input('Location: ', value=0, step=1)
        device_class = st.number_input('Device Class: ', value=0, step=1)
        game = st.number_input('Game Product: ', value=0, step=1)
        music = st.number_input('Music Product: ', value=0, step=1)
        education = st.number_input('Education: ', value=0, step=1)
        call_center = st.number_input('Call Center: ', value=0, step=1)
        payment_method = st.number_input('Payment Method: ', value=0, step=1)
        monthly_purchase = st.number_input('Monthly Purchase: ', value=0, step=1)
        cltv = st.number_input('CLTV: ', value=0, step=1)

        data = np.array([tenure_month, location, device_class, game, music, education, call_center, payment_method, monthly_purchase, cltv]).reshape(1, -1)

        if st.form_submit_button('Generate'):
            file_name = 'xgboost_model.pkl'

            with open(file_name, 'rb') as file:
                loaded_model = pkl.load(file)

            prediction = loaded_model.predict(data)
            st.write(f"Prediction: {prediction[0]}")