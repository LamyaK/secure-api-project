from flask import Flask, jsonify
from api.routes import register_routes

def create_app():
    app = Flask(__name__)
    
    # Configuration de base
    app.config['SECRET_KEY'] = 'une_cle_secrete_temporaire'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Enregistrer les routes
    register_routes(app)
    
    @app.route('/health')
    def health_check():
        return jsonify({"status": "ok"})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
