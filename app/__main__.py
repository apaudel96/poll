import dotenv

dotenv.load_dotenv()
import os
from app.app import app

production = os.getenv("ENV", "PROD") == "PROD"
app.run(
    debug=False if production else True,
    port=os.getenv("PORT", 5000),
    host="0.0.0.0" if production else "localhost",
)
