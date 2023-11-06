import streamlit as st
import pickle as pkl
import numpy as np



class MultiPage:

    def __init__(self):
        self.pages = []


    def add_page(self, title, func):
        self.pages.append({
            "title":title,
            "function":func
        })

    def run(self):
        page = st.sidebar.selectbox(
            'Pages',
            self.pages,
            format_func=lambda page: page['title']
        )

        page['function']()


multi_page = MultiPage()

def page_one():
    st.title('Home')


def page_two():
    st.title('Dashboard')
    html_code = """
    <style>
    .responsive-iframe {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 56.25%; /* 16:9 aspect ratio (h/w) */
    }
    .responsive-iframe iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
    </style>
    <div class="responsive-iframe">
        <iframe width="100%" height="100%" src="https://lookerstudio.google.com/embed/reporting/e250424c-d5da-4da0-bfb5-fb7607becac0/page/p_383q79vcbd" frameborder="0" style="border:0" allowfullscreen></iframe>
    </div>
    """

    st.markdown(html_code, unsafe_allow_html=True)


def page_three():
    st.title('Churn Prediction :writing_hand:')

    with st.form('Feature Audio Analysis'):
        st.write('Input Features')
        tenure_month = st.number_input('Tenure Month: ', value=0, step=1)
        location = st.radio(
            "Lokasi User", ("Jakarta", "Bandung")
        )
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


multi_page.add_page('Home', page_one)
multi_page.add_page('Dashboard', page_two)
multi_page.add_page('Churn Prediction', page_three)

multi_page.run()
