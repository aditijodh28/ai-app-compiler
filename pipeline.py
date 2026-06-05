def extract_intent(user_prompt):
    return {
        "app_type": "CRM",
        "features": [
            "login",
            "contacts",
            "dashboard"
        ],
        "roles": [
            "admin",
            "user"
        ]
    }

def system_design(intent):
    return {
        "entities": [
            "User",
            "Contact"
        ]
    }

def generate_schema(design):

    return {
        "ui": {
            "pages": ["dashboard", "contacts"]
        },

        "api": {
            "endpoints": ["/contacts"]
        },

        "database": {
            "tables": ["users", "contacts"]
        },

        "auth": {
            "roles": ["admin", "user"]
        }
    }