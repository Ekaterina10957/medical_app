import argon2

PH = argon2.PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    hash_len=32,
    salt_len=16
)

def hash_password(password):
    """Хеширует пароль с использованием Argon2."""
    try:
        hashed_password = PH.hash(password)
        return hashed_password
    except argon2.exceptions.HashingError as e:
        print(f"Ошибка при хешировании пароля: {e}")
        return None

def verify_password(hashed_password, password):
    """Проверяет, соответствует ли пароль хешу Argon2."""
    try:
        return PH.verify(hashed_password, password)
    except argon2.exceptions.VerifyMismatchError:
        return False
    except argon2.exceptions.VerificationError as e:
        print(f"Ошибка при верификации пароля: {e}")
        return False
