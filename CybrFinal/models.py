from flask_mongoengine import MongoEngine

db = MongoEngine()


class PaperSubmission(db.Document): """Model representing a conference paper submission in ConfFlow"""


title = db.StringField(max_length=300, required=True)
track = db.StringField(max_length=100, required=True)  # e.g., Ethical AI, NLP, Robotics
authors = db.ListField(db.StringField(max_length=100))  # list of author names
country = db.StringField(max_length=100, required=True)
submission_date = db.DateTimeField(required=True)
status = db.StringField(max_length=50, default="pending")  # e.g., pending, assigned, reviewed

assigned_reviewers = db.ListField(db.StringField(max_length=100))  # reviewer usernames or IDs
conflicts_flagged = db.BooleanField(default=False)
auto_assigned = db.BooleanField(default=False)
reviewer_notifications_sent = db.BooleanField(default=False)

meta = {
    'collection': 'paper_submissions',
    'ordering': ['-submission_date'],
    'auto_create_index': False,
}
