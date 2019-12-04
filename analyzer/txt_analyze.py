import sys
import os
from collections import Counter

### my lib ####
sys.path.append('../')
from .converter.pdf2txt import pdf2txt

stop_words = [ ' am ', ' is ', ' of ', ' and ', ' the ', ' to ', ' it ', ' for ', ' in ', ' as ', ' or ', ' are ', ' be ', ' this ', ' that ', ' will ', ' there ', ' was ', ' a ']

def load_txt(path):
  with open(path) as f:
    text = f.readlines()
  text = ''.join(text)
  return text

def remove_stop_words(txt, stop_words):
  for stop_word in stop_words:
    txt = txt.replace(stop_word, ' ')
  txt = txt.replace('  ', ' ')
  return txt

def main():
  path_list = ['..', 'plane_text']
  path = os.path.join(*path_list)
  print('analyze dir :', path)
  dirs = os.listdir(path)
  dirs.remove('.DS_Store')
  for txt_path in dirs:
    txt_path = os.path.join(*path_list, txt_path)
    print(txt_path)
    txt = load_txt(txt_path)
    txt = txt.replace('-\n', '')
    txt = txt.replace('\n', ' ')
    txt = txt.lower()
    txt = remove_stop_words(txt, stop_words)
    txt_list = txt.split()
    count = Counter(txt_list)
#    print(count)
#    with open(txt_path.replace('plane_text', 'analyze'), mode='w') as f:
#      print('writing ... ', txt_path.replace('plane_txt', 'analyze'))
#      f.write(txt)

if __name__ == '__main__':
  main()

