import streamlit as st
import pandas as pd
import openai
import os

# Set up Streamlit UI
st.set_page_config(page_title="AI Passive Income Dashboard", layout="wide")
st.title("AI Passive Income Generator")
st.subheader("Track, optimize, and automate your income streams")

# Sidebar for user inputs
st.sidebar.header("Income Stream Selection")
income_streams = [
    "Affiliate Marketing",
    "Print-on-Demand",
    "Dividend Investing",
    "Digital Products",
    "YouTube AI Content",
    "E-Commerce Dropshipping",
    "Real Estate (REITs, Rental)"
]
selected_streams = st.sidebar.multiselect("Select passive income streams to track:", income_streams)

# Sample Data for Simulation
if selected_streams:
    data = {
        "Income Stream": selected_streams,
        "Monthly Earnings ($)": [500, 700, 300, 1000, 1500, 400, 800][:len(selected_streams)],
        "Effort Required (1-5)": [3, 3, 1, 3, 3, 4, 2][:len(selected_streams)],
        "Investment ($)": [100, 200, 10000, 50, 100, 500, 20000][:len(selected_streams)]
    }
    df = pd.DataFrame(data)
    st.subheader("Income Stream Performance")
    st.dataframe(df)

# AI Insights & Recommendations
if st.button("Generate AI Recommendations"):
    recommendations = []
    for stream in selected_streams:
        if stream == "Affiliate Marketing":
            recommendations.append("Focus on high-ticket affiliate programs and optimize SEO for higher traffic.")
        elif stream == "Print-on-Demand":
            recommendations.append("Use AI-generated designs and optimize trending niches.")
        elif stream == "Dividend Investing":
            recommendations.append("Reinvest dividends and diversify into high-yield ETFs for stable income.")
        elif stream == "Digital Products":
            recommendations.append("Automate sales funnels and scale with paid ads and content marketing.")
        elif stream == "YouTube AI Content":
            recommendations.append("Use AI-generated scripts and automate video production to scale earnings.")
        elif stream == "E-Commerce Dropshipping":
            recommendations.append("Focus on niche products with minimal competition and automate order fulfillment.")
        elif stream == "Real Estate (REITs, Rental)":
            recommendations.append("Invest in high-yield REITs for passive returns without property management.")
    
    st.subheader("AI-Driven Recommendations")
    for rec in recommendations:
        st.write(f"- {rec}")

# Future Enhancements
st.sidebar.header("Future AI Enhancements")
st.sidebar.write("✔ Auto-track revenue and trends\n✔ Predict profitable niches\n✔ AI chatbot for financial guidance")

# AI Chatbot Integration with API Key Handling
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.warning("OpenAI API key is missing. Set it as an environment variable OPENAI_API_KEY.")
else:
    def ai_chatbot(prompt):
        try:
            client = openai.OpenAI(api_key=openai_api_key)
            response = client.chat.completions.create(
                model="gpt-4-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"

    st.subheader("AI Passive Income Chatbot")
    user_input = st.text_input("Ask me anything about passive income:")
    if st.button("Get AI Advice"):
        if user_input:
            ai_response = ai_chatbot(user_input)
            st.write(ai_response)
        else:
            st.write("Please enter a question.")
