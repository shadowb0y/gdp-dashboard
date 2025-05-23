import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.title("📍 Geolocalizzazione sicura (con postMessage)")

st.markdown("""
<script>
navigator.geolocation.getCurrentPosition(
    function(position) {
        const data = {
            type: 'coords',
            lat: position.coords.latitude,
            lon: position.coords.longitude
        };
        window.parent.postMessage(data, "*");
    },
    function(error) {
        const data = {
            type: 'coords',
            lat: null,
            lon: null
        };
        window.parent.postMessage(data, "*");
    }
);
</script>
""", unsafe_allow_html=True)

# Ricevi il messaggio JS
coords = streamlit_js_eval(message=True, key="geolocation")

if coords and coords.get("type") == "coords" and coords.get("lat") is not None:
    st.success(f"✅ Posizione rilevata: {coords['lat']}, {coords['lon']}")
    st.map([{"lat": coords["lat"], "lon": coords["lon"]}])
else:
    st.warning("🕒 In attesa dell'autorizzazione o dei dati...")
