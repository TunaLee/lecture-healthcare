#!/usr/bin/env python3
"""
HTML을 PDF로 변환하는 스크립트
이미지가 없어도 작동하도록 처리됩니다.
"""

from weasyprint import HTML, CSS
from pathlib import Path
import sys

def convert_html_to_pdf(html_path, pdf_path):
    """HTML 파일을 PDF로 변환"""
    
    # 추가 CSS - 인쇄용 스타일
    print_css = CSS(string='''
        @page {
            size: A4 landscape;
            margin: 0;
        }
        
        body {
            margin: 0;
            padding: 0;
        }
        
        .slide {
            display: block !important;
            page-break-after: always;
            page-break-inside: avoid;
            width: 100%;
            height: 100vh;
        }
        
        .slide:last-child {
            page-break-after: auto;
        }
        
        .controls, .keyboard-hint {
            display: none !important;
        }
        
        /* 이미지 에러 처리 */
        .image-placeholder img {
            display: block;
        }
        
        /* 이미지 로드 실패시 placeholder 스타일 */
        .image-placeholder {
            background: #f5f5f5;
            border: 3px dashed #999;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .image-placeholder::after {
            content: "이미지 영역";
            color: #999;
            font-size: 18px;
        }
    ''')
    
    try:
        print(f"📄 HTML 파일 읽는 중: {html_path}")
        
        # HTML을 PDF로 변환
        html = HTML(filename=html_path)
        
        print("🔄 PDF 변환 중...")
        html.write_pdf(
            pdf_path,
            stylesheets=[print_css]
        )
        
        print(f"✅ PDF 생성 완료: {pdf_path}")
        return True
        
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False

def main():
    # 입력/출력 경로 설정
    html_file = "./1강/slide.html"
    pdf_file = "./1강/머신러닝1강.pdf"
    
    # 변환 실행
    success = convert_html_to_pdf(html_file, pdf_file)
    
    if success:
        print("\n" + "="*50)
        print("PDF 파일이 생성되었습니다!")
        print(f"위치: {pdf_file}")
        print("="*50)
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())