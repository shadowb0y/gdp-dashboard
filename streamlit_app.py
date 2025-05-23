import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.title("🌍 Test posizione utente")

st.markdown("""
<script>
navigator.geolocation.getCurrentPosition(
    function(position) {
        window.latitude = position.coords.latitude;
        window.longitude = position.coords.longitude;
    },
    function(error) {
        window.latitude = null;
        window.longitude = null;
    }
);
</script>
""", unsafe_allow_html=True)

coords = streamlit_js_eval(
    js_expressions="({lat: window.latitude, lon: window.longitude})",
    key="geo-test"
)

if coords and coords.get("lat") is not None:
    st.success(f"✅ Posizione: {coords['lat']}, {coords['lon']}")
    st.map([{"lat": coords["lat"], "lon": coords["lon"]}])
else:
    st.warning("🕒 Aspettando l'autorizzazione per la posizione...")
