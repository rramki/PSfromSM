import praw
import streamlit as st

def get_comments(query, limit=20):
    reddit = praw.Reddit(
        client_id=st.secrets["REDDIT_CLIENT_ID"],
        client_secret=st.secrets["REDDIT_SECRET"],
        user_agent="sentiment-app"
    )

    comments = []

    for submission in reddit.subreddit("all").search(query, limit=limit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comments.append(comment.body)

    return comments[:100]  # limit total comments
