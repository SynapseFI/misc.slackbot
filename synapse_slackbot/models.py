"""SQLAlchemy model class definitions."""
from .config import db


class User(db.Model):
    """Store Slack user id and Synapse user id together."""
    __tablename__ = 'users'
    slack_user_id = db.Column(db.String(15), primary_key=True)
    synapse_user_id = db.Column(db.String(30), unique=True)
    debit_node_id = db.Column(db.String(30), unique=True)
    savings_node_id = db.Column(db.String(30), unique=True)
    recurring_transactions = db.relationship('RecurringTransaction',
                                             backref='user')

    def __init__(self, slack_user_id, synapse_user_id):
        self.slack_user_id = slack_user_id
        self.synapse_user_id = synapse_user_id

    def __repr__(self):
        return '<User: (slack %r), (synapse: %r)>' % (self.slack_user_id,
                                                      self.synapse_user_id)


class RecurringTransaction(db.Model):
    """Transaction details for a recurring transaction."""
    __tablename__ = 'recurring_transactions'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    periodicity = db.Column(db.Integer)
    slack_user_id = db.Column(db.String(15),
                              db.ForeignKey('users.slack_user_id'))

    def __init__(self, **kwargs):
        self.amount = kwargs['amount']
        self.periodicity = kwargs['periodicity']
        self.slack_user_id = kwargs['slack_user_id']

    def __repr__(self):
        return ('<RecurringTransaction: %r every %r days (User: %r)' %
                (self.amount, self.periodicity, self.slack_user_id))
