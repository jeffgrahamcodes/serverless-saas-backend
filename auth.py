from fastapi import Security, HTTPException, Depends
from fastapi.security import HTTPBearer
import jwt  # This is fine if using PyJWT
import os

security = HTTPBearer()

# Replace with your actual AWS Cognito User Pool & Client IDs
COGNITO_USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
COGNITO_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")

def verify_token(token: str = Security(security)):
    """
    Decodes and verifies the JWT token from AWS Cognito.
    """
    try:
        # Decode the JWT (Assuming you're handling RS256)
        payload = jwt.decode(token.credentials, algorithms=["RS256"], options={"verify_aud": False})
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")