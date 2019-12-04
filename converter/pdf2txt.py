import sys
import os
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

def find_textboxes_recursively(layout_obj):
  if isinstance(layout_obj, LTTextBox):
    return [layout_obj]
  if isinstance(layout_obj, LTContainer):
    boxes = []
    for child in layout_obj:
      boxes.extend(find_textboxes_recursively(child))
    return boxes
  return []

def pdf2txt(filepath):
  laparams = LAParams(detect_vertical=True)
  resource_manager = PDFResourceManager()
  device = PDFPageAggregator(resource_manager, laparams=laparams)
  interpreter = PDFPageInterpreter(resource_manager, device)
  pdf_text = ''
  with open(filepath, 'rb') as f:
    for page in PDFPage.get_pages(f):
      interpreter.process_page(page)
      layout = device.get_result()
      boxes = find_textboxes_recursively(layout)
      boxes.sort(key=lambda b: (-b.y1, b.x0))
      for box in boxes:
        pdf_text += box.get_text()
  return pdf_text

def main():
  path_list = ['..', 'articles']
  path = os.path.join(*path_list)
  print('search dir :', path)
  dirs = os.listdir(path)
  print(dirs)
  for pdf in dirs:
    pdf = os.path.join(*path_list, pdf)
    print(pdf)
    text = pdf2txt(pdf)
    with open(pdf.replace('articles', 'plane_text').replace('pdf', 'txt'), mode='w') as f:
      f.write(text)

if __name__ == '__main__':
  main()

