import jwt
import os

from fastapi import Header
from fastapi.exceptions import HTTPException
from server.database import SessionLocal

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

async def get_user(token: str = Header(...)):
  decoded_user = jwt.decode(token, os.environ.get("JWT_SECRET"), algorithms='HS256')
    
  return decoded_user

async def protected_route(token: str = Header(...)):
  if token is None:
    raise HTTPException(status_code=401, detail="Authorization token not found.")
  try:
    jwt.decode(token, os.environ.get("JWT_SECRET"), algorithms='HS256')
    
    pass
  except: 
    raise HTTPException(status_code=403, detail="Invalid JWT Token.")
 