import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="منتجات الأكثر مبيعًا", layout="wide")
st.title("📦 المنتجات الأكثر مبيعًا")
st.markdown("### عرض مباشر للمنتجات الأكثر مبيعًا على Amazon")

# اختيار الدولة
country = st.selectbox("اختر الدولة:", ["السعودية", "أمريكا"])

# روابط Amazon
amazon_urls = {
    "السعودية": "https://www.amazon.sa/gp/bestsellers",
    "أمريكا": "https://www.amazon.com/Best-Sellers/zgbs"
}

url = amazon_urls[country]

@st.cache_data(show_spinner=False)
def fetch_best_sellers(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    items = soup.select(".zg-grid-general-faceout")
    data = []
    for item in items[:10]:
        title = item.select_one(".p13n-sc-truncate, ._cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
        title_text = title.text.strip() if title else ""
        img = item.select_one("img")
        img_url = img["src"] if img else ""
        data.append({"المنتج": title_text, "الصورة": img_url})
    return pd.DataFrame(data)

# تحميل البيانات
with st.spinner("جاري تحميل الترندات..."):
    df = fetch_best_sellers(url)

# عرض البيانات
if not df.empty:
    for i, row in df.iterrows():
        st.image(row["الصورة"], width=120)
        st.markdown(f"**{i+1}. {row['المنتج']}**")
        st.markdown("---")
else:
    st.error("لم يتم العثور على بيانات")
