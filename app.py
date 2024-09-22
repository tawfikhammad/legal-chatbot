import streamlit as st
from chatbot import chatbot_response

st.write("مرحبا! أنا هنا للإجابة على أسئلتك المتعلقة بالقضاء والقانون المصريه. كيف يمكنني أن اخدمك؟")

question = st.text_input('أدخل سؤالك هنا:')

if st.button('إرسال'):
    if question:
        response = chatbot_response(question)
        st.write(response)
    else:
        st.write("يرجى إدخال سؤال.")

