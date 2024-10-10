import os
import shutil
import zipfile
from glob import glob
from time import sleep
import tkinter as tk
from tkinter import filedialog
import re

# GUI를 통한 파일 선택
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[('HWPX Files', '*.hwpx')])
    if file_path:
        process_file(file_path)
        success_label.config(text="Success")

def process_file(hwpx_file_path):
    # 압축 풀기 및 스타일 교체
    extract(hwpx_file_path)
    convert_styles("temp/Contents/header.xml")  # header.xml 파일에서 스타일을 교체
    
    # 다시 압축하여 저장
    with zipfile.ZipFile(hwpx_file_path.replace(".hwpx", "_Style_re.hwpx"), 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('temp', zipf)
    
    # 임시 폴더 삭제
    shutil.rmtree('temp')
    print("파일 처리가 완료되었습니다.")

def extract(path):
    os.chdir(os.path.dirname(path))
    target_path = os.path.join(os.getcwd(), "temp")
    with zipfile.ZipFile(path, 'r') as zf:
        zf.extractall(path=target_path)

def convert_styles(header_file_path):
    # header.xml에서 <hh:style> 부터 </hh:styles>까지의 내용을 사용자가 제공한 데이터로 교체
    with open(header_file_path, "r", encoding="utf-8") as file:
        data = file.read()
        
        # <hh:style>부터 </hh:styles>까지 매칭하여 교체
        new_styles = '''<hh:styles itemCnt="7">
<hh:style id="0" type="PARA" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0" nextStyleIDRef="0" langID="1042" lockForm="0"/>
<hh:style id="1" type="PARA" name="본문" engName="Body" paraPrIDRef="1" charPrIDRef="0" nextStyleIDRef="1" langID="1042" lockForm="0"/>
<hh:style id="2" type="PARA" name="개요 1" engName="Outline 1" paraPrIDRef="2" charPrIDRef="0" nextStyleIDRef="2" langID="1042" lockForm="0"/>
<hh:style id="3" type="PARA" name="개요 2" engName="Outline 2" paraPrIDRef="3" charPrIDRef="0" nextStyleIDRef="3" langID="1042" lockForm="0"/>
<hh:style id="4" type="PARA" name="개요 3" engName="Outline 3" paraPrIDRef="4" charPrIDRef="0" nextStyleIDRef="4" langID="1042" lockForm="0"/>
<hh:style id="5" type="PARA" name="개요 4" engName="Outline 4" paraPrIDRef="5" charPrIDRef="0" nextStyleIDRef="5" langID="1042" lockForm="0"/>
<hh:style id="6" type="PARA" name="개요 5" engName="Outline 5" paraPrIDRef="6" charPrIDRef="0" nextStyleIDRef="6" langID="1042" lockForm="0"/>
</hh:styles>'''
        
        data = re.sub(r'<hh:styles.*?</hh:styles>', new_styles, data, flags=re.DOTALL)
    
    with open(header_file_path, "w", encoding="utf-8") as file:
        file.write(data)

def zipdir(path, ziph):
    os.chdir(path)
    for root, dirs, files in os.walk("."):
        for file in files:
            ziph.write(os.path.join(root, file))
    os.chdir("..")

# GUI 설정 및 실행
root = tk.Tk()
root.title("HWPX Style Converter v1.0")
root.geometry("400x300")

# 프로그램 제목
title_label = tk.Label(root, text="HWPX 파일 스타일 변경 프로그램", font=("Arial", 16))
title_label.pack(pady=10)

# 파일 선택 지침
instruction_label = tk.Label(root, text="Please select an HWPX file.", font=("Arial", 10))
instruction_label.pack(pady=5)

# 파일 선택 버튼
select_button = tk.Button(root, text="Select HWPX File", command=select_file)
select_button.pack(pady=10)

# 성공 메시지
success_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
success_label.pack(pady=20)

# 하단 정보 표시
footer_label = tk.Label(root, text="Version 1.0V 		  		  	Developed by Hyunuk", font=("Arial", 8))
footer_label.pack(side="bottom", anchor="w", padx=10, pady=10)

root.mainloop()