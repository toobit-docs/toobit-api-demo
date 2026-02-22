"""
TooBit API configuration management module
"""

import os
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class TooBitConfig(BaseModel):
    """TooBit API configuration class"""
    
    # API basic information
    api_key: str = Field(..., description="API Key")
    api_secret: str = Field(..., description="API Secret")
    base_url: str = Field(default="", description="API base URL")
    
    # Request Configuration
    timeout: int = Field(default=30, description="Request timeout time (seconds)")
    recv_window: int = Field(default=5000, description="Receive window time (milliseconds)")
    
    # Retry configuration
    max_retries: int = Field(default=3, description="Maximum retry count")
    retry_delay: float = Field(default=1.0, description="Retry delay (seconds)")
    
    # Rate limit configuration
    request_weight_limit: int = Field(default=1200, description="Request weight limit")
    orders_limit: int = Field(default=10, description="Order Limit")
    
    @classmethod
    def from_env(cls) -> "TooBitConfig":
        """Create configuration from environment variables"""
        return cls(
            api_key=os.getenv("TOOBIT_API_KEY", "o1BrE03MKxUXEVGxUYiKTeXDnLU0HZLdVGsjtTKUfLYSQSmkvZjYmUmhVFCqXHjI"),
            api_secret=os.getenv("TOOBIT_API_SECRET", "x4uIXXmYo7TxbqjUGzzGZmFAThwl3CaDc58eTSdqSSs3Ot0fO8ufHZ95mptSvjjC"),
            base_url=os.getenv("TOOBIT_BASE_URL", "https://api.test1.wcsbapp.com"),
            timeout=int(os.getenv("TOOBIT_TIMEOUT", "30")),
            recv_window=int(os.getenv("TOOBIT_RECV_WINDOW", "5000")),
            max_retries=int(os.getenv("TOOBIT_MAX_RETRIES", "3")),
            retry_delay=float(os.getenv("TOOBIT_RETRY_DELAY", "1.0")),
        )
    
    def validate(self) -> bool:
        """Validate if configuration is valid"""
        if not self.api_key or not self.api_secret:
            raise ValueError("API Key and API Secret cannot be empty")
        if self.recv_window > 60000:  # Maximum 60 seconds
            raise ValueError("recvWindow cannot exceed 60000 milliseconds")
        return True 