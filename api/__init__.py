from fastapi import APIRouter

from .polls import router as polls_router
from .auth import router as auth_router
from .votes import router as votes_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(polls_router)
router.include_router(votes_router)
