
import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Google Trends Live Monitor", layout="wide")

# إدخال الكلمات من المستخدم
custom_words = st.text_input("📝 أدخل كلمات ترند (مفصولة بفاصلة):", value="AI,Python,Bitcoin")
keywords = [word.strip() for word in custom_words.split(",")]

# عرض الكلمات في الشريط الجانبي
with st.sidebar:
    st.markdown("### الكلمات المرصودة:")
    for word in keywords:
        st.write(f"🔹 {word}")

# تحميل البيانات من Google Trends
pytrends = TrendReq()
pytrends.build_payload(keywords, cat=0, timeframe='now 1-d', geo='', gprop='')
df = pytrends.interest_over_time()

# عرض العنوان
st.markdown("# 📈 Google Trends Live Monitor")
st.markdown("### Trending Data for the last 24 hours:")

# عرض البيانات البيانية
fig, ax = plt.subplots()
df[keywords].plot(ax=ax, figsize=(14, 6))
plt.legend(loc='upper left')
plt.tight_layout()
st.pyplot(fig)
