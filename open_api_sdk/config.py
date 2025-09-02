"""
TooBit API 配置管理模块
"""

import os
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


class TooBitConfig(BaseModel):
    """TooBit API 配置类"""
    
    # API 基础信息
    api_key: str = Field(..., description="API Key")
    api_secret: str = Field(..., description="API Secret")
    base_url: str = Field(default="https://api.test1.wcsbapp.com", description="API基础URL")
    
    # 请求配置
    timeout: int = Field(default=30, description="请求超时时间(秒)")
    recv_window: int = Field(default=5000, description="接收窗口时间(毫秒)")
    
    # 重试配置
    max_retries: int = Field(default=3, description="最大重试次数")
    retry_delay: float = Field(default=1.0, description="重试延迟(秒)")
    
    # 速率限制配置
    request_weight_limit: int = Field(default=1200, description="请求权重限制")
    orders_limit: int = Field(default=10, description="订单限制")
    
    @classmethod
    def from_env(cls) -> "TooBitConfig":
        """从环境变量创建配置"""
        return cls(
            api_key=os.getenv("TOOBIT_API_KEY", ""),
            api_secret=os.getenv("TOOBIT_API_SECRET", ""),
            base_url=os.getenv("TOOBIT_BASE_URL", "https://api.test1.wcsbapp.com"),
            timeout=int(os.getenv("TOOBIT_TIMEOUT", "30")),
            recv_window=int(os.getenv("TOOBIT_RECV_WINDOW", "5000")),
            max_retries=int(os.getenv("TOOBIT_MAX_RETRIES", "3")),
            retry_delay=float(os.getenv("TOOBIT_RETRY_DELAY", "1.0")),
        )
    
    def validate(self) -> bool:
        """验证配置是否有效"""
        if not self.api_key or not self.api_secret:
            raise ValueError("API Key 和 API Secret 不能为空")
        if self.recv_window > 60000:  # 最大60秒
            raise ValueError("recvWindow 不能超过60000毫秒")
        return True 