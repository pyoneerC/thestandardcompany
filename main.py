"""
The Standard Company - Landing Page Server
FastAPI + HTMX + Tailwind CSS
"""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(
    title="The Standard Company",
    description="Software for problems that deserve solutions.",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page for The Standard Company"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "The Standard Company | Software for problems that deserve solutions",
            "description": "An independent product studio building the future of trust and security."
        }
    )


@app.get("/api/newsletter", response_class=HTMLResponse)
async def newsletter_signup(request: Request, email: str = ""):
    """HTMX endpoint for newsletter signup"""
    if email:
        # In production, save to database
        return """
        <div class="newsletter-success animate-fade-in">
            <svg class="w-6 h-6 text-green-400 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            <span class="text-white font-medium">You're in! We'll keep you posted.</span>
        </div>
        """
    return """<span class="text-red-400">Please enter a valid email</span>"""


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
