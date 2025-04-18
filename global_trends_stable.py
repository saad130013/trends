
import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

st.set_page_config(page_title="Google Trends Explorer", layout="wide")

st.title("🌍 ترندات Google حسب الدولة")

# قائمة بالدول المدعومة من pytrends
countries = {
    "السعودية 🇸🇦": "saudi_arabia",
    "الولايات المتحدة 🇺🇸": "united_states",
    "اليابان 🇯🇵": "japan",
    "ألمانيا 🇩🇪": "germany",
    "كوريا الجنوبية 🇰🇷": "south_korea",
    "مصر 🇪🇬": "egypt",
    "المملكة المتحدة 🇬🇧": "united_kingdom",
    "فرنسا 🇫🇷": "france",
    "تركيا 🇹🇷": "turkey"
}

selected_country = st.selectbox("اختر الدولة", list(countries.keys()))
country_code = countries[selected_country]

try:
    pytrends = TrendReq()
    trending_df = pytrends.trending_searches(pn=country_code)

    st.success(f"عرض الترندات في {selected_country}")
    st.dataframe(trending_df.head(10))

except Exception as e:
    st.error("حدث خطأ أثناء جلب البيانات. حاول لاحقًا.")
    st.exception(e)
