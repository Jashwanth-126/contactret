from flask import Flask, render_template
from supabase import create_client, Client
import os
import pathlib # <-- Import the pathlib library

# --- Initialize Flask with explicit path ---
# This ensures Flask looks for the 'templates' folder in the project's root 
# directory, not inside the 'api' directory.
ROOT_DIR = pathlib.Path(__file__).parent.parent
app = Flask(__name__, root_path=ROOT_DIR)

# --- Supabase Configuration (Remains the same) ---
SUPABASE_URL = os.getenv("SUPABASE_URL", "https://mkitrmvlscuzdqrmbjkk.supabase.co")
SUPABASE_KEY = os.getenv(
    "SUPABASE_KEY",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1raXRybXZsc2N1emRxcm1iamtrIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1NjQ2NzY5MCwiZXhwIjoyMDcyMDQzNjkwfQ.Y2DYjeBkHDpvGtR2Co6NbfcwvQv5XStBe9AlTYPye7s"
)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Flask Routes ---
@app.route("/")
def view_contacts():
    try:
        response = supabase.table("contact_queries").select("*").execute()
        contacts = response.data if response and hasattr(response, "data") else []
        
        # This line should now correctly find the template:
        return render_template("view.html", contacts=contacts)
        
    except Exception as e:
        return f"Something went wrong: {str(e)}"

# The local run block should be fine if you kept it.
# if __name__ == "__main__":
#     app.run(debug=True)