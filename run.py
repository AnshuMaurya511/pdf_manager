import os
from app import create_app,db
from app.models import Notes
from app.models import User

app = create_app()
os.makedirs("uploads", exist_ok=True)
with app.app_context():
    db.create_all()

if __name__ =="__main__":
    app.run(debug=True)