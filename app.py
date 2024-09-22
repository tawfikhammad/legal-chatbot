import streamlit as st
import requests

st.write("مرحبا! أنا هنا للإجابة على أسئلتك المتعلقة بالقضاء والقانون المصريه. كيف يمكنني أن اخدمك؟")

question = st.text_input('أدخل سؤالك هنا:')

if st.button('إرسال'):
    if question:
        # Make a POST request to the Flask API
        response = requests.post('https://127.0.0.1:5000/get_response', json={'question': question})

        if response.ok:
            try:
                response_data = response.json()
                st.write(response_data.get('response'))
            except ValueError:
                st.write("Response is not valid JSON:", response.text)
        else:
            st.write("حدث خطأ في الاتصال بالخادم.")
    else:
        st.write("يرجى إدخال سؤال.")

