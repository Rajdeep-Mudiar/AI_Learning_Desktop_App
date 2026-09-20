from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.community import (
    CommunityPost,
    CreatePostRequest
)
from app.services.community_service import (
    list_posts,
    create_community_post,
    upvote_post
)

router = APIRouter(prefix="/community", tags=["Community"])

@router.get("/posts", response_model=List[CommunityPost])
async def get_posts():
    """Retrieve community discussion and show-and-tell posts."""
    return list_posts()

@router.post("/posts", response_model=CommunityPost)
async def create_post(req: CreatePostRequest):
    """Publish a new discussion post or model showcase in the community."""
    return create_community_post(req)

@router.post("/posts/{post_id}/upvote", response_model=CommunityPost)
async def upvote(post_id: str):
    """Upvote a community discussion post."""
    p = upvote_post(post_id)
    if not p:
        raise HTTPException(status_code=404, detail="Post not found")
    return p
