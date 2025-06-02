#!/usr/bin/env python3
"""
Just3Lines 애플리케이션 진입점
Railway Railpack이 자동으로 감지할 수 있도록 루트에 위치
"""

if __name__ == "__main__":
    import uvicorn
    import os
    
    # Railway에서 제공하는 PORT 환경변수 사용
    port = int(os.getenv("PORT", 8000))
    
    # FastAPI 앱 실행
    uvicorn.run(
        "app.main:app",  # app 디렉토리의 main.py에서 app 객체 가져오기
        host="0.0.0.0",
        port=port,
        reload=False  # 프로덕션에서는 reload 비활성화
    )