import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.ensemble import RandomForestRegressor

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Public Transport Crowd Predictor",
    page_icon="🚌",
    layout="wide"
)

# ============================================================
# API CONFIGURATION
# ============================================================

# DO NOT put your real API key directly in this file.
# Add it in Streamlit Secrets.

# .streamlit/secrets.toml
# BUS_API_KEY = "YOUR_API_KEY"

BUS_API_KEY = st.secrets.get("BUS_API_KEY", "")

# Replace this with the actual live-bus API endpoint
API_URL = "YOUR_LIVE_BUS_API_URL"

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef5ff, #f8fbff);
}

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: #12355b;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.prediction-card {
    background: linear-gradient(135deg, #12355b, #1d70a2);
    color: white;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}

.prediction-number {
    font-size: 42px;
    font-weight: 800;
}

.prediction-label {
    font-size: 17px;
}

.recommendation {
    background-color: #fff7e6;
    border-left: 6px solid #ff9800;
    padding: 18px;
    border-radius: 10px;
    color: #5c4000;
    font-size: 17px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🚌 AI Public Transport Crowd Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Real-Time Bus Tracking + AI Crowd Prediction</div>',
    unsafe_allow_html=True
)

# ============================================================
# SAMPLE ML DATA
# ============================================================

np.random.seed(42)

data = []

for i in range(1000):

    hour = np.random.randint(5, 23)
    day = np.random.randint(0, 7)
    route = np.random.randint(1, 6)
    weather = np.random.randint(0, 3)

    passengers = 40

    if 7 <= hour <= 10:
        passengers += 60

    if 17 <= hour <= 20:
        passengers += 80

    if day >= 5:
        passengers -= 20

    if weather == 1:
        passengers += 10

    if weather == 2:
        passengers += 20

    passengers += route * 8

    passengers += np.random.randint(-15, 16)

    passengers = max(10, passengers)

    data.append([
        hour,
        day,
        route,
        weather,
        passengers
    ])

df = pd.DataFrame(
    data,
    columns=[
        "hour",
        "day",
        "route",
        "weather",
        "passengers"
    ]
)

# ============================================================
# ML MODEL
# ============================================================

X = df[[
    "hour",
    "day",
    "route",
    "weather"
]]

y = df["passengers"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# ============================================================
# ROUTE INPUT
# ============================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader("🔍 Enter Travel Details")

col1, col2 = st.columns(2)

with col1:

    from_place = st.selectbox(
        "📍 From",
        [
            "Kompally",
            "Suchitra",
            "Jeedimetla",
            "Gandimaisamma"
        ]
    )

    to_place = st.selectbox(
        "📍 To",
        [
            "Maisammaguda",
            "Bachupally",
            "JNTU",
            "Miyapur"
        ]
    )

    day_name = st.selectbox(
        "📅 Day",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

with col2:

    travel_time = st.slider(
        "⏰ Travel Hour",
        5,
        22,
        8
    )

    weather_name = st.selectbox(
        "🌦️ Weather",
        [
            "Normal",
            "Rainy",
            "Heavy Rain"
        ]
    )

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# CONVERT INPUTS
# ============================================================

day_number = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
].index(day_name)

weather_number = [
    "Normal",
    "Rainy",
    "Heavy Rain"
].index(weather_name)

route_number = 1

# ============================================================
# LIVE BUS API FUNCTION
# ============================================================

def get_live_buses(source, destination):

    if not BUS_API_KEY:
        return None, "API key not configured."

    if API_URL == "YOUR_LIVE_BUS_API_URL":
        return None, "Live API URL not configured."

    try:

        headers = {
            "Authorization": f"Bearer {BUS_API_KEY}",
            "Accept": "application/json"
        }

        params = {
            "from": source,
            "to": destination
        }

        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            return None, f"API Error: {response.status_code}"

        return response.json(), None

    except Exception as e:

        return None, str(e)

# ============================================================
# PREDICT BUTTON
# ============================================================

if st.button("🚀 Find Live Buses & Predict Crowd"):

    st.markdown("---")

    # ========================================================
    # LIVE BUS SECTION
    # ========================================================

    st.subheader(
        f"🚌 Live Buses: {from_place} → {to_place}"
    )

    live_data, error = get_live_buses(
        from_place,
        to_place
    )

    if live_data:

        st.success("🟢 Live bus data received")

        # ----------------------------------------------------
        # IMPORTANT
        # Adjust these field names according to your API.
        # ----------------------------------------------------

        buses = live_data.get("buses", [])

        if buses:

            for bus in buses:

                bus_name = bus.get(
                    "bus_number",
                    "Unknown Bus"
                )

                location = bus.get(
                    "location",
                    "Unknown"
                )

                eta = bus.get(
                    "eta",
                    "N/A"
                )

                st.markdown(
                    f"""
                    <div class="card">

                    <h3>🚌 {bus_name}</h3>

                    <b>📍 Current Location:</b>
                    {location}

                    <br><br>

                    <b>⏱ ETA:</b>
                    {eta}

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info(
                "No live buses found for this route."
            )

    else:

        st.warning(
            f"""
            ⚠️ Live bus data unavailable.

            {error}

            AI crowd prediction can still be calculated.
            """
        )

    # ========================================================
    # AI CROWD PREDICTION
    # ========================================================

    input_data = pd.DataFrame(
        [[
            travel_time,
            day_number,