import sys
import os
from pathlib import Path

pdf_path = Path(r"d:/others/Nagaraj_aithal.pdf")
out_txt = Path(r"d:/profile/portfolio_Nagaraj_/assets/files/Nagaraj_aithal.txt")

def ensure_pypdf2():
    try:
        import PyPDF2
        return PyPDF2
    except Exception:
        print('PyPDF2 not found, attempting to install...')
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf2'])
        import PyPDF2
        return PyPDF2

def extract_text(pdf_path):
    PyPDF2 = ensure_pypdf2()
    text_parts = []
    with open(pdf_path, 'rb') as fh:
        reader = PyPDF2.PdfReader(fh)
        for page in reader.pages:
            try:
                text = page.extract_text() or ''
            except Exception:
                text = ''
            text_parts.append(text)
    return '\n\n'.join(text_parts)

def main():
    if not pdf_path.exists():
        print(f'PDF not found at: {pdf_path}')
        sys.exit(2)
    txt = extract_text(pdf_path)
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    with open(out_txt, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f'Extracted text written to: {out_txt}')

if __name__ == '__main__':
    main()
