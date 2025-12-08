import os

JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
JWT_EXP_MIN = int(os.getenv("JWT_EXP_MIN", "15"))
