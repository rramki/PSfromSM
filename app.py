import streamlit as st
import pandas as pd
from reddit_client import get_comments
from preprocess import clean_text
from sentiment import analyze_sentiment

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.title("📊 Social Media Sentiment Analyzer")

query = st.text_input("Enter Organization / Topic:")

if st.button("Analyze"):
    if query:
        with st.spinner("Fetching comments..."):
            comments = get_comments(query)

        st.success(f"Fetched {len(comments)} comments")

        results = []
        with st.spinner("Analyzing sentiment..."):
            for c in comments:
                cleaned = clean_text(c)
                sentiment = analyze_sentiment(cleaned)
                results.append([c, sentiment])

        df = pd.DataFrame(results, columns=["Comment", "Sentiment"])

        st.subheader("Results")
        st.dataframe(df)

        st.subheader("Sentiment Distribution")
        st.bar_chart(df["Sentiment"].value_counts())

        # Download option
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, "sentiment_results.csv")
    else:
        st.warning("Please enter a query")
