from fastapi import FastAPI
from routes.user import user
from routes.post import post
from docs import tags_metadata

app = FastAPI(
    title="Api SocNet",
    description="REST API SOCNET",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(user)
app.include_router(post)
