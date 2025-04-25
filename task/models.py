from extensions import db
from datetime import datetime
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)
    archived = db.Column(db.Boolean, default=False) 
    priority = db.Column(db.String(10), default='Medium')  # Low, Medium, High
    due_date = db.Column(db.Date)  # Optional
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Task {self.title}>"
