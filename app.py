import streamlit as st
import pickle as pkl
import numpy as np
from PIL import Image



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


def layout_streamlit():
    st.set_page_config(layout='wide')

    light = '''
        <style>
            .stApp {
            background-color: white;
            }
        </style>
        '''
    st.markdown(light, unsafe_allow_html=True)


layout = layout_streamlit()

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

def page_three():
    about_us = 'About Us'
    st.markdown(
    f"<h1 style='text-align: center; color: black;'>{about_us}</h1>",
    unsafe_allow_html=True
    )
    profile_team = Image.open('profile.png')
    st.image(profile_team)

    # Informasi Kontak
    kontak_orang_1 = {
        'Nama': 'Nine Alvariqati',
        'Email': 'ninealvariqati.v.a@gmail.com',
        'LinkedIn': 'https://www.linkedin.com/in/nine-alvariqati-a138a5298/'
    }

    kontak_orang_2 = {
        'Nama': 'Joni Bastian',
        'Email': 'jonibastian01@gmail.com',
        'LinkedIn': 'https://www.linkedin.com/in/jonibastian/'
    }

    kontak_orang_3 = {
        'Nama': 'Ibnu Zahy Atha Illah',
        'Email': 'ibnuzahyy22@gmail.com',
        'LinkedIn': 'https://www.linkedin.com/in/ibnuzahy/'
    }

    # Tampilan
    kontak = "Informasi Kontak"
    st.markdown(
    f"<h3 style='text-align: center; color: black;'>{kontak}</h3>",
    unsafe_allow_html=True
    )

    # Membuat kolom secara horizontal
    kolom1, kolom2, kolom3 = st.columns(3)

    # Informasi Orang 1
    with kolom1:
        st.write(
            f"<p style='color: black; font-weight: bold;'>Nama: {kontak_orang_1['Nama']}</p>"
            f"<p style='color: black; font-weight: bold;'>Email: <a href='mailto:{kontak_orang_1['Email']}'>{kontak_orang_1['Email']}</a><br>"
            f"<p style='color: black; font-weight: bold;'>LinkedIn: <a href='{kontak_orang_1['LinkedIn']}' target='_blank'>{kontak_orang_1['LinkedIn']}</a></p>",
            unsafe_allow_html=True
        )

    # Informasi Orang 2
    with kolom2:
        st.write(
            f"<p style='color: black; font-weight: bold;'>Nama: {kontak_orang_2['Nama']}</p>"
            f"<p style='color: black; font-weight: bold;'>Email: <a href='mailto:{kontak_orang_2['Email']}'>{kontak_orang_2['Email']}</a><br>"
            f"<p style='color: black; font-weight: bold;'>LinkedIn: <a href='{kontak_orang_2['LinkedIn']}' target='_blank'>{kontak_orang_2['LinkedIn']}</a></p>",
            unsafe_allow_html=True
        )

    # Informasi Orang 3
    with kolom3:
        st.write(
            f"<p style='color: black; font-weight: bold;'>Nama: {kontak_orang_3['Nama']}</p>"
            f"<p style='color: black; font-weight: bold;'>Email: <a href='mailto:{kontak_orang_3['Email']}'>{kontak_orang_3['Email']}</a><br>"
            f"<p style='color: black; font-weight: bold;'>LinkedIn: <a href='{kontak_orang_3['LinkedIn']}' target='_blank'>{kontak_orang_3['LinkedIn']}</a></p>",
            unsafe_allow_html=True
        )

def page_one():
    dashboard = 'Dashboard'
    st.markdown(
    f"<h1 style='text-align: center; color: black;'>{dashboard}</h1>",
    unsafe_allow_html=True
    )
    responsive_iframe("https://lookerstudio.google.com/embed/reporting/e250424c-d5da-4da0-bfb5-fb7607becac0/page/p_383q79vcbd&embed=0")


def render_churn_prediction():
    churn_app = 'Churn Prediction 📉'
    st.markdown(
        f"<h1 style='text-align: center; color: black;'>{churn_app}</h1>"
        f"<style>body {{"  # CSS untuk mengubah warna tulisan
            "color: black !important;"
        "}}</style>",  # Penutup tag style
        unsafe_allow_html=True
    )

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

    st.write('Input Features')

    # Tambahkan properti key untuk menyesuaikan gaya elemen
    tenure_month = st.number_input('Tenure Month: ', value=0, step=1, key='tenure_month')
    location = st.radio("Lokasi User", ("Jakarta", "Bandung"), key='location')
    device_class = st.selectbox('Jenis Device: ', ("Low End", "Mid End", "High End"), key='device_class')

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

    game = st.radio('Use Games Product: ', game_options, key='game')
    music = st.radio('Use Music Product: ', music_options, key='music')
    video = st.radio("Use Video Product: ", video_options, key='video')
    education = st.radio('Use Education Product: ', education_options, key='education')
    use_my_app = st.radio("Use MyApp Application", use_my_app_options, key='use_my_app')
    call_center = st.radio('Call Center: ', ("No", "Yes"), key='call_center')
    payment_method = st.radio('Metode Pembayaran: ', ("Debit", "Pulsa", "Digital Wallet", "Credit"), key='payment_method')
    monthly_purchase = st.number_input('Monthly Purchase of Thousand IDR: ', value=0.0, format="%.3f", key='monthly_purchase')
    cltv = st.number_input('CLTV: ', value=0.0, format="%.3f", key='cltv')

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

    loaded_model = load_model()
    prediction = loaded_model.predict(data)

    if st.button('Predict'):
        prediction_result = prediction_mapping[prediction[0]]
        st.write(f"Prediction: {prediction_result}")
       

def page_two():
    render_churn_prediction()


multi_page.add_page('Dashboard', page_one)
multi_page.add_page('Churn Prediction', page_two)
multi_page.add_page('About Us', page_three)

multi_page.run()
