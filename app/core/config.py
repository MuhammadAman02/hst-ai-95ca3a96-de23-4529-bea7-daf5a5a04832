from pydantic_settings import BaseSettings
from typing import List, Optional
import os

class Settings(BaseSettings):
    """Application settings with validation."""
    
    # Application Settings
    APP_NAME: str = "AI Engineer Portfolio"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = "development"
    DEBUG: bool = True
    
    # Portfolio Owner Information
    OWNER_NAME: str = "John Doe"
    OWNER_TITLE: str = "AI Engineer & Machine Learning Specialist"
    OWNER_EMAIL: str = "contact@example.com"
    OWNER_GITHUB: str = "https://github.com/yourusername"
    OWNER_LINKEDIN: str = "https://linkedin.com/in/yourusername"
    OWNER_TWITTER: Optional[str] = None
    OWNER_PROFILE_IMAGE: str = "profile.jpg"
    
    # Server Settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Global configuration instance
settings = Settings()