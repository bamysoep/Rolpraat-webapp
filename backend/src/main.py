import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.modules.users import router as users_router

app = FastAPI(
    title="Rolpraat API",
    description="Backend API for Rolpraat webapp",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users_router)


@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Rolpraat API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
