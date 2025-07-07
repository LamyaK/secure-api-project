from flask import jsonify, request

def register_routes(app):
    # Route pour obtenir tous les utilisateurs
    @app.route('/api/users', methods=['GET'])
    def get_users():
        # Simuler des données pour l'instant
        users = [
            {"id": 1, "username": "user1", "email": "user1@example.com"},
            {"id": 2, "username": "user2", "email": "user2@example.com"}
        ]
        return jsonify(users)
    
    # Route pour obtenir un utilisateur par ID
    @app.route('/api/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        # Simuler la recherche d'un utilisateur
        user = {"id": user_id, "username": f"user{user_id}", "email": f"user{user_id}@example.com"}
        return jsonify(user)
    
    # Route pour créer un nouvel utilisateur
    @app.route('/api/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        # Dans un vrai projet, on sauvegarderait dans une base de données
        return jsonify({"message": "Utilisateur créé", "user": data}), 201
