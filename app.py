import streamlit as st
import pandas as pd
from global_trends_stable import fetch_trends  # تأكد من وجود الدالة في ملفك

st.set_page_config(page_title="🌍 الترندات العالمية", layout="wide")

st.title("🌍 أبرز الترندات العالمية اليوم")

try:
    df = fetch_trends()  # الدالة لازم ترجع DataFrame

    if not df.empty:
        st.success("تم جلب البيانات بنجاح ✅")
        st.dataframe(df)
    else:
        st.warning("⚠️ لم يتم العثور على بيانات الترندات حالياً.")
except Exception as e:
    st.error(f"❌ حدث خطأ أثناء جلب البيانات:

{e}")