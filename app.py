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

        st.markdown(
            """
            <style>
            .stApp {
                max-width: 100%;
                margin: 0 auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        page['function']()


multi_page = MultiPage()

def responsive_iframe(url):
    code = f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{url}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
    </div>
    """
    st.markdown(code, unsafe_allow_html=True)

def load_model():
    file_name = 'xgboost_model_11.pkl'

    with open(file_name, 'rb') as file:
        return pkl.load(file)

def page_one():
    st.title('Home')


def page_two():
    st.title('Dashboard')
    responsive_iframe("https://lookerstudio.google.com/embed/reporting/e250424c-d5da-4da0-bfb5-fb7607becac0/page/p_383q79vcbd&embed=0")

def render_churn_prediction():
    st.title('Churn Prediction :writing_hand:')

    mapping = {
        "Jakarta": 0,
        "Bandung": 1,
        "Low End": 0,
        "Mid End": 1,
        "High End": 2,
        "No": 0,
        "Yes": 1,
        "No Internet Service": 2,
        "Debit": 0,
        "Pulsa": 1,
        "Digital Wallet": 2,
        "Credit": 3
    }

    prediction_mapping = {
        0: "Non Churn",
        1: "Churn"
    }

    with st.form('Feature Audio Analysis'):
        st.write('Input Features')
        tenure_month = st.number_input('Tenure Month: ', value=0, step=1)
        location = st.radio("Lokasi User", ("Jakarta", "Bandung"))
        device_class = st.selectbox('Jenis Device: ', ("Low End", "Mid End", "High End"))

        def get_radio_options(device_class):
            if device_class == "Low End":
                return ["No Internet Service"]
            else:
                return ["No", "Yes", "No Internet Service"]

        game_options = get_radio_options(device_class)
        music_options = get_radio_options(device_class)
        video_options = get_radio_options(device_class)
        education_options = get_radio_options(device_class)
        use_my_app_options = get_radio_options(device_class)

        game = st.radio('Use Games Product: ', game_options)
        music = st.radio('Use Music Product: ', music_options)
        video = st.radio("Use Video Product: ", video_options)
        education = st.radio('Use Education Product: ', education_options)
        use_my_app = st.radio("Use MyApp Application", use_my_app_options)

        call_center = st.radio('Call Center: ', ("No", "Yes"))
        payment_method = st.radio('Metode Pembayaran: ', ("Debit", "Pulsa", "Digital Wallet", "Credit"))
        monthly_purchase = st.number_input('Monthly Purchase of Thousand IDR: ', value=0.0, format="%.3f")
        cltv = st.number_input('CLTV: ', value=0.0, format="%.3f")

        location = mapping[location]
        device_class = mapping[device_class]
        game = mapping[game]
        music = mapping[music]
        video = mapping[video]
        education = mapping[education]
        use_my_app = mapping[use_my_app]
        call_center = mapping[call_center]
        payment_method = mapping[payment_method]

        data = np.array(
            [tenure_month, location, device_class, game, music, education, call_center, video, use_my_app,
             payment_method, monthly_purchase, cltv]).reshape(1, -1)

        if st.form_submit_button('Generate'):
            loaded_model = load_model()
            prediction = loaded_model.predict(data)
            prediction_result = prediction_mapping[prediction[0]]
            st.write(f"Prediction: {prediction_result}")

def page_three():
    render_churn_prediction()


multi_page.add_page('Home', page_one)
multi_page.add_page('Dashboard', page_two)
multi_page.add_page('Churn Prediction', page_three)

multi_page.run()
