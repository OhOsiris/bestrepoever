from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import hackathons, journeys, drafts, playbook, export

app = FastAPI(
    title="Hack2Skill Email Command Center",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hackathons.router)
app.include_router(journeys.router)
app.include_router(drafts.router)
app.include_router(playbook.router)
app.include_router(export.router)

@app.get("/health")
async def health():
    return {"status": "healthy"}
