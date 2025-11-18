from flask import Flask, render_template
from supabase import create_client, Client
import os

app = Flask(__name__)

# You can later set these in Render environment variables again
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://mkitrmvlscuzdqrmbjkk.supabase.co")
SUPABASE_KEY = os.getenv(
    "SUPABASE_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1raXRybXZsc2N1emRxcm1iamtrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjQ2NzY5MCwiZXhwIjoyMDcyMDQzNjkwfQ.Y2DYjeBkHDpvGtR2Co6NbfcwvQv5XStBe9AlTYPye7s"
)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
def view_contacts():
    try:
        response = supabase.table("contact_queries").select("*").execute()
        contacts = response.data if hasattr(response, "data") else []
        return render_template("view.html", contacts=contacts)
    except Exception as e:
        return f"Something went wrong: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
