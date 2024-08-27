import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

# load environment variables
load_dotenv()
logpass= os.getenv('pgPassword')
loguse= os.getenv('pgUser')

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{loguse}:{logpass}@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'
    
    # register pet blueprint 
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app


# factory 


                
