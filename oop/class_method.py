import json

class User:
    def __init__(self, name:str, role:str):
        self.name = name
        self.role = role


    @classmethod
    def file_json(cls, json_str:str) -> "User":
        data = json.loads(json_str)
        return cls(name = data["name"], role = data["role"])

    @staticmethod
    def validate_role(role:str) -> bool:
        return role in ["Admin", "Editor", "Viewer"]


user_json = '{"name": "Bob", "role": "Admin"}'
if User.validate_role('Admin'):
    user = User.file_json(user_json)
    print(f"Created user: {user.name} with  role ({user.role})")

