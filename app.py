import streamlit as st

st.set_page_config(page_title="Country Language Finder")

st.title("🌍 Country Language Finder")
st.write("Select a country to see its widely spoken language(s).")

country_languages = {
    "India": ["Hindi", "English"],
    "United States": ["English"],
    "United Kingdom": ["English"],
    "France": ["French"],
    "Germany": ["German"],
    "Spain": ["Spanish"],
    "China": ["Mandarin Chinese"],
    "Japan": ["Japanese"],
    "Russia": ["Russian"],
    "Brazil": ["Portuguese"],
    "Italy": ["Italian"],
    "Canada": ["English", "French"],
    "Australia": ["English"],
    "Mexico": ["Spanish"],
    "South Korea": ["Korean"],
    "Saudi Arabia": ["Arabic"],
    "Pakistan": ["Urdu", "English"],
    "Bangladesh": ["Bengali"],
    "Nepal": ["Nepali"],
    "Sri Lanka": ["Sinhala", "Tamil"]
}

country = st.selectbox(
    "Choose a country:",
    sorted(country_languages.keys())
)

if country:
    st.success(
        f"Widely spoken language(s) in {country}: "
        f"{', '.join(country_languages[country])}"
    )