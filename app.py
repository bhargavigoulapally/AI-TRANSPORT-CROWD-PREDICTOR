import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Transport Crowd Predictor",
    page_icon="🚌",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
}

.card {
    padding: 22px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.result {
    padding: 25px;
    border-radius: 15px;
    background-color: #eef4ff;
    text-align: center;
    margin-top: 20px;
}

.result h2 {
    color: #333333;
}

.footer {
    text-align: center;
    padding: 20px;
    color: #777777;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="hero">

<h1>🚌 AI Transport Crowd Predictor</h1>

<p>
Predict transport crowd levels using Artificial Intelligence
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# INTRODUCTION
# =========================================================

st.markdown("""
<div class="card">

<h3>🤖 About the Project</h3>

<p>
This AI-based application predicts the expected crowd level
in public transportation based on route, day, weather,
travel time and route type.
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# GENERATE TRAINING DATA
# =========================================================

np.random.seed(42)

data_size = 1000

travel_time_data = np.random.randint(5, 24, data_size)

day_data = np.random.randint(1, 8, data_size)

weather_data = np.random.randint(1, 5, data_size)

route_type_data = np.random.randint(1, 6, data_size)

crowd_data = (
    20
    + travel_time_data * 5
    + day_data * 3
    + weather_data * 8
    + route_type_data * 7
    + np.random.normal(0, 10, data_size)
)

crowd_data = np.maximum(crowd_data, 5)

training_data = pd.DataFrame({
    "Travel_Time": travel_time_data,
    "Day": day_data,
    "Weather": weather_data,
    "Route_Type": route_type_data,
    "Crowd": crowd_data
})

# =========================================================
# TRAIN AI MODEL
# =========================================================

X = training_data[
    [
        "Travel_Time",
        "Day",
        "Weather",
        "Route_Type"
    ]
]

y = training_data["Crowd"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# =========================================================
# USER INPUT
# =========================================================

st.markdown("""
<div class="card">

<h3>📍 Enter Travel Details</h3>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    route = st.text_input(
        "🛣️ Enter Route",
        placeholder="Example: Hyderabad to Secunderabad"
    )

    day = st.selectbox(
        "📅 Select Day",
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

    weather = st.selectbox(
        "🌤️ Select Weather",
        [
            "Sunny",
            "Cloudy",
            "Rainy",
            "Stormy"
        ]
    )

with col2:

    travel_time = st.slider(
        "⏰ Travel Time",
        min_value=5,
        max_value=23,
        value=9
    )

    route_type = st.selectbox(
        "🚌 Route Type",
        [
            "Local",
            "City",
            "Intercity",
            "High Traffic",
            "Express"
        ]
    )

# =========================================================
# CONVERT INPUTS TO NUMBERS
# =========================================================

day_mapping = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

weather_mapping = {
    "Sunny": 1,
    "Cloudy": 2,
    "Rainy": 3,
    "Stormy": 4
}

route_mapping = {
    "Local": 1,
    "City": 2,
    "Intercity": 3,
    "High Traffic": 4,
    "Express": 5
}

day_number = day_mapping[day]

weather_number = weather_mapping[weather]

route_number = route_mapping[route_type]

# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("###")

if st.button(
    "🔮 Predict Crowd",
    use_container_width=True
):

    if route.strip() == "":
        st.warning("⚠️ Please enter a route.")

    else:

        # Create input DataFrame

        input_data = pd.DataFrame(
            [[
                travel_time,
                day_number,
                weather_number,
                route_number
            ]],
            columns=[
                "Travel_Time",
                "Day",
                "Weather",
                "Route_Type"
            ]
        )

        # AI prediction

        predicted_crowd = model.predict(input_data)[0]

        predicted_crowd = int(max(0, round(predicted_crowd)))

        # =================================================
        # CROWD LEVEL
        # =================================================

        if predicted_crowd < 70:

            crowd_level = "LOW 🟢"

        elif predicted_crowd < 120:

            crowd_level = "MEDIUM 🟡"

        else:

            crowd_level = "HIGH 🔴"

        # =================================================
        # RESULT
        # =================================================

        st.markdown(f"""
        <div class="result">

        <h2>🚌 Crowd Prediction</h2>

        <h1>{predicted_crowd} Passengers</h1>

        <h2>{crowd_level}</h2>

        <p><b>Route:</b> {route}</p>

        </div>
        """, unsafe_allow_html=True)

        # =================================================
        # SUMMARY
        # =================================================

        st.markdown("### 📊 Travel Summary")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Route",
                route
            )

        with col2:
            st.metric(
                "Day",
                day
            )

        with col3:
            st.metric(
                "Weather",
                weather
            )

        with col4:
            st.metric(
                "Passengers",
                predicted_crowd
            )

        # =================================================
        # CROWD BAR GRAPH
        # =================================================

        st.markdown("### 📈 Crowd Comparison")

        graph_data = pd.DataFrame({
            "Category": [
                "Predicted Crowd",
                "Low Limit",
                "Medium Limit"
            ],

            "Passengers": [
                predicted_crowd,
                70,
                120
            ]
        })

        st.bar_chart(
            graph_data.set_index("Category")
        )

        # =================================================
        # HOURLY CROWD GRAPH
        # =================================================

        st.markdown("### ⏰ Estimated Hourly Crowd")

        hours = list(range(6, 23))

        hourly_crowd = []

        for hour in hours:

            hour_input = pd.DataFrame(
                [[
                    hour,
                    day_number,
                    weather_number,
                    route_number
                ]],
                columns=[
                    "Travel_Time",
                    "Day",
                    "Weather",
                    "Route_Type"
                ]
            )

            prediction = model.predict(hour_input)[0]

            hourly_crowd.append(
                int(max(0, round(prediction)))
            )

        hourly_data = pd.DataFrame({
            "Hour": [
                f"{hour}:00"
                for hour in hours
            ],

            "Passengers": hourly_crowd
        })

        st.line_chart(
            hourly_data.set_index("Hour")
        )

        # =================================================
        # PEAK TIME
        # =================================================

        peak_index = int(
            np.argmax(hourly_crowd)
        )

        peak_hour = hours[peak_index]

        peak_crowd = hourly_crowd[peak_index]

        st.success(
            f"🔥 Estimated peak time: "
            f"{peak_hour}:00 with approximately "
            f"{peak_crowd} passengers."
        )

        # =================================================
        # AI EXPLANATION
        # =================================================

        st.markdown("### 🤖 AI Analysis")

        if predicted_crowd < 70:

            explanation = (
                "The predicted crowd is relatively low. "
                "This may be a comfortable travel period."
            )

        elif predicted_crowd < 120:

            explanation = (
                "The predicted crowd is moderate. "
                "Some passenger congestion may occur."
            )

        else:

            explanation = (
                "The predicted crowd is high. "
                "Passengers may experience significant congestion."
            )

        st.info(explanation)

# =========================================================
# MODEL INFORMATION
# =========================================================

with st.expander("ℹ️ About the AI Model"):

    st.write("""
    This project uses a Random Forest Regression model.

    The model considers:

    • Travel time
    • Day of the week
    • Weather condition
    • Route type

    The training data is simulated for demonstration purposes.
    Therefore, the prediction represents an estimated crowd level
    rather than real-time passenger data.
    """)

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<hr>

<p>
🚌 AI Transport Crowd Predictor
</p>

<p>
Built using Python • Streamlit • Machine Learning
</p>

</div>
""", unsafe_allow_html=True)
