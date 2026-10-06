    input_data = pd.DataFrame(
        [[
            travel_time,
            day_number,
            route_number,
            weather_number
        ]],
        columns=[
            "hour",
            "day",
            "route",
            "weather"
        ]
    )

    predicted_crowd = model.predict(input_data)[0]

    st.markdown("---")

    # ========================================================
    # CROWD PREDICTION RESULT
    # ========================================================

    st.subheader("🤖 AI Crowd Prediction")

    st.markdown(
        f"""
        <div class="prediction-card">

            <div class="prediction-number">
                {predicted_crowd:.0f}
            </div>

            <div class="prediction-label">
                Estimated Passengers
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # CROWD LEVEL
    # ========================================================

    if predicted_crowd < 70:

        crowd_level = "🟢 Low Crowd"
        recommendation = (
            "This is a good time to travel. "
            "The bus is expected to have fewer passengers."
        )

    elif predicted_crowd < 120:

        crowd_level = "🟡 Medium Crowd"
        recommendation = (
            "Moderate crowd is expected. "
            "Consider travelling slightly earlier or later."
        )

    else:

        crowd_level = "🔴 High Crowd"
        recommendation = (
            "High crowd is expected. "
            "Consider travelling during a less busy time."
        )

    st.markdown(
        f"""
        <div class="card">

            <h2>{crowd_level}</h2>

            <div class="recommendation">
                💡 {recommendation}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # TRAVEL SUMMARY
    # ========================================================

    st.subheader("📊 Travel Summary")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:
        st.metric(
            "From",
            from_place
        )

    with summary_col2:
        st.metric(
            "To",
            to_place
        )

    with summary_col3:
        st.metric(
            "Travel Hour",
            f"{travel_time}:00"
        )

    st.info(
        "🤖 Crowd prediction is generated using a Random Forest "
        "machine-learning model trained on simulated public "
        "transport data."
    )
