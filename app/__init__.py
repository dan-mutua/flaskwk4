from flask import Flask

# Initializing application
app = Flask(__name__, template_folder='templates')


from app import views

return app
