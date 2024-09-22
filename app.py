import streamlit as st
import requests

st.write("مرحبا! أنا هنا للإجابة على أسئلتك المتعلقة بالقضاء والقانون المصريه. كيف يمكنني أن اخدمك؟")

question = st.text_input('أدخل سؤالك هنا:')

if st.button('إرسال'):
    if question:
        # Make a POST request to the Flask API
        response = requests.post('https://legal-chatbot-egy.streamlit.app/get_response', json={'question': question})
        if response.ok:
            st.write(response.json().get('response'))
        else:
            st.write("حدث خطأ في الاتصال بالخادم.")
    else:
        st.write("يرجى إدخال سؤال.")

