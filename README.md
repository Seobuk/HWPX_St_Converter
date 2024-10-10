# HWPX 스타일 변환기 v1.0
![GitHub Release](https://img.shields.io/github/v/release/Seobuk/HWPX_St_Converter?style=flat&logo=github)
![GitHub Issues](https://img.shields.io/github/issues/Seobuk/HWPX_St_Converter)
![GitHub Forks](https://img.shields.io/github/forks/Seobuk/HWPX_St_Converter)
![GitHub Stars](https://img.shields.io/github/stars/Seobuk/HWPX_St_Converter)
![GitHub License](https://img.shields.io/github/license/Seobuk/HWPX_St_Converter)

## 개요
HWPX 스타일 변환기는 HWPX 파일의 스타일을 수정하기 위해 설계된 Python 기반 도구입니다. 사용자가 HWPX 파일을 선택하고 처리할 수 있는 사용자 친화적인 GUI를 제공하며, `<hh:style>` 요소를 새 스타일로 교체할 수 있도록 해줍니다.

## 주요 기능
- GUI를 통해 HWPX 파일을 선택합니다.
- HWPX 파일을 자동으로 추출, 수정, 재압축합니다.
- `header.xml` 내 스타일을 지정된 형식으로 교체합니다.

## 요구 사항
- Python 3.x
- 다음 Python 패키지들이 필요합니다:
  - `tkinter` (GUI를 위해)
  - `shutil` (파일 작업을 위해)
  - `zipfile` (HWPX 파일을 처리하기 위해)
  - `re` (정규 표현식 작업을 위해)

## 설치
1. 리포지토리를 클론합니다:
   ```bash
   git clone https://github.com/yourusername/hwpx-style-converter.git
   ```
2. 프로젝트 디렉토리로 이동합니다:
   ```bash
   cd hwpx-style-converter
   ```
3. 필요한 종속성을 설치합니다. `pip`을 사용하여 누락된 패키지를 설치할 수 있습니다.

## 사용 방법
1. Python을 사용하여 스크립트를 실행합니다:
   ```bash
   python hwpx_style_converter.py
   ```
2. GUI 창이 열립니다. "Select HWPX File" 버튼을 클릭하여 수정할 HWPX 파일을 선택합니다.
3. 파일이 성공적으로 처리되면 "Success" 메시지가 나타납니다.
4. 수정된 파일은 동일한 디렉토리에 `_Style_re.hwpx`라는 이름으로 저장됩니다.

## GUI 세부 사항
- **제목**: "HWPX 스타일 변환기 v1.0"
- **지침**: "HWPX 파일을 선택하세요."
- **하단 정보**: Version 1.0V | Made by Hyunuk

## 라이선스
이 프로젝트는 MIT 라이선스 하에 제공됩니다 - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 작성자
- **Hyunuk Seo** - 초기 작업

## 감사의 말
- 오픈 소스 커뮤니티에 기여해주신 모든 분들께 감사드립니다. 그들의 귀중한 자료와 도움에 큰 감사를 드립니다.
