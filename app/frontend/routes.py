from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()

# This file is mainly for FastAPI routes, but we're using NiceGUI as our primary UI
# So this is just a placeholder that redirects to the NiceGUI interface

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Redirect to the NiceGUI interface."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="0;url=/" />
        <title>Redirecting...</title>
    </head>
    <body>
        <p>Redirecting to the portfolio...</p>
    </body>
    </html>
    """