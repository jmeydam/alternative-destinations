import os
from app import create_app, db
from app.models import Airport, Destination

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
#print(dir(app))
#print(app.config)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Airport=Airport, Destination=Destination)

@app.cli.command()
def test():
    """Run tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
