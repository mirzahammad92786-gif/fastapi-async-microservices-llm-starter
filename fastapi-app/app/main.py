from fastapi import FastAPI

from api.auth.routes import router as auth_router
from api.users.routes import router as users_router
from api.tasks.routes import router as tasks_router
from api.ai.routes import router as ai_router

app = FastAPI(
    title="FastAPI Async Microservices LLM Starter",
    version="1.0.0",
    description="Production-style FastAPI backend with auth, users, tasks, and AI/LLM endpoints.",
)


@app.get("/")
async def health_check():
    return {
        "status": "ok",
        "service": "fastapi-async-microservices-llm-starter",
    }


# Register route groups
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
app.include_router(ai_router, prefix="/ai", tags=["ai"])
