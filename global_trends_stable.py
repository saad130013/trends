
from pytrends.request import TrendReq
import pandas as pd
import streamlit as st

# إعداد pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# كلمات نتابعها
keywords = ["AI", "Bitcoin", "Python"]

# تحميل البيانات
pytrends.build_payload(keywords, timeframe='now 1-d')
data = pytrends.interest_over_time()

# عرض في Streamlit
st.set_page_config(page_title="Google Trends", layout="wide")
st.title("📈 Google Trends Live Monitor")
st.write("Trending Data for the last 24 hours:")
st.line_chart(data[keywords])
