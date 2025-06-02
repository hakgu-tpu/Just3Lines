#!/usr/bin/env python3
"""
Railway Railpack 호환을 위한 app.py 파일
"""

from app.main import app

if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)