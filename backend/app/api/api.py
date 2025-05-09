from fastapi import APIRouter
from .endpoints import pdf

api_router = APIRouter()

# Import and include other routers here
# Example:
# from .endpoints import presentations
# api_router.include_router(presentations.router, prefix="/presentations", tags=["presentations"])

# Include PDF upload router
api_router.include_router(pdf.router, prefix="/pdf", tags=["pdf"]) 