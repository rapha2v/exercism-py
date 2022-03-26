import re


def parse(markdown):
  lines = markdown.split('\n')
  res = ''
  in_list = False
  in_list_append = False
  for line in lines:
    line = check_if_header(line)
    m = re.match(r'\* (.*)', line)
    if m:
      if not in_list:
        in_list = True
        is_bold = False
        is_italic = False
        curr = m.group(1)
        m1 = re.match('(.*)__(.*)__(.*)', curr)
        if m1:
          curr = m1.group(1) + '<strong>' + \
              m1.group(2) + '</strong>' + m1.group(3)
          is_bold = True
        m1 = re.match('(.*)_(.*)_(.*)', curr)
        if m1:
          curr = m1.group(1) + '<em>' + m1.group(2) + \
              '</em>' + m1.group(3)
          is_italic = True
        line = '<ul><li>' + curr + '</li>'
      else:
        is_bold = False
        is_italic = False
        curr = m.group(1)
        m1 = re.match('(.*)__(.*)__(.*)', curr)
        if m1:
          is_bold = True
        m1 = re.match('(.*)_(.*)_(.*)', curr)
        if m1:
          is_italic = True
        if is_bold:
          curr = m1.group(1) + '<strong>' + \
              m1.group(2) + '</strong>' + m1.group(3)
        if is_italic:
          curr = m1.group(1) + '<em>' + m1.group(2) + \
              '</em>' + m1.group(3)
        line = '<li>' + curr + '</li>'
    else:
      if in_list:
        in_list_append = True
        in_list = False

    m = re.match('<h|<ul|<p|<li', line)
    if not m:
      line = '<p>' + line + '</p>'
    m = re.match('(.*)__(.*)__(.*)', line)
    if m:
      line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    m = re.match('(.*)_(.*)_(.*)', line)
    if m:
      line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    if in_list_append:
      line = '</ul>' + line
      in_list_append = False
    res += line
  if in_list:
    res += '</ul>'

  print(res)
  return res


def check_if_header(line):
  if re.match('###### (.*)', line) is not None:
    line = '<h6>' + line[7:] + '</h6>'
  elif re.match('##### (.*)', line) is not None:
    line = '<h5>' + line[6:] + '</h5>'
  elif re.match('#### (.*)', line) is not None:
    line = '<h4>' + line[5:] + '</h4>'
  elif re.match('### (.*)', line) is not None:
    line = '<h3>' + line[4:] + '</h3>'
  elif re.match('## (.*)', line) is not None:
    line = '<h2>' + line[3:] + '</h2>'
  elif re.match('# (.*)', line) is not None:
    line = '<h1>' + line[2:] + '</h1>'
  return line


parse("# Header!\n* __Bold Item__\n* _Italic Item_")
