import streamlit as st
import sqlite3
from textblob import TextBlob
import pandas as pd

st.title("Self-Care Journal")

# Mood Tracker
mood = st.selectbox("How do you feel today?", ["Happy", "Sad", "Stressed", "Anxious", "Excited"])
journal_entry = st.text_area("Write your journal entry here:")

if st.button("Submit"):
    # Connect to the database
    conn = sqlite3.connect('self_care_journal.db')
    c = conn.cursor()
    
    # Save mood entry
    c.execute("INSERT INTO moods (mood) VALUES (?)", (mood,))
    
    # Save journal entry
    c.execute("INSERT INTO journals (entry, mood) VALUES (?, ?)", (journal_entry, mood))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
    # Display a success message
    st.success("Entry saved!")

if st.button("Submit"):
    # Existing code to save entries...
    
    # Perform sentiment analysis
    blob = TextBlob(journal_entry)
    sentiment_score = blob.sentiment.polarity  # Range: -1 (negative) to 1 (positive)
    
    # Display sentiment score
    st.write(f"Sentiment Score: {sentiment_score:.2f}")
