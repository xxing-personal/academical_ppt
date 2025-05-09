from fastapi import APIRouter

api_router = APIRouter()

# Import and include other routers here
# Example:
# from .endpoints import presentations
# api_router.include_router(presentations.router, prefix="/presentations", tags=["presentations"]) 