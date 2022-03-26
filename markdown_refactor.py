import re


class MarkdownToHTML:
    def __init__(self, texto_markdown: str):
        self.texto = texto_markdown.split('\n')

    def converter(self):
        for i, texto in enumerate(self.texto):
            texto = self.check_is_paragraph(texto)
            texto = self.check_is_header(texto)
            texto = self.check_is_bold(texto)
            texto = self.check_is_italic(texto)
            texto = self.check_is_list(texto)
            self.texto[i] = texto
        self.check_encapsulate_list()
        return ''.join(self.texto)

    @staticmethod
    def check_is_header(texto: str):
        check_which_header = re.match(r"(^[#]{1,6}) ([\s\w]+)", texto)
        if check_which_header is not None:
            header_len = len(check_which_header.group(1))
            return f"<h{header_len}>{check_which_header.group(2).strip()}</h{header_len}>"
        else:
            return texto

    @staticmethod
    def check_is_paragraph(texto: str):
        check_if_is_paragraph = re.match(r"^[#]{1,6} [\s\w]+|^\* ", texto)
        if check_if_is_paragraph is None:
            return f"<p>{texto.strip()}</p>"
        return texto

    @staticmethod
    def check_is_bold(texto: str):
        check_bold = re.findall(r"__([^_]*(?:_[^_]+)*)__", texto, flags=re.IGNORECASE)
        if check_bold is not None:
            for word in check_bold:
                texto = texto.replace(f"__{word}__", f"<strong>{word}</strong>")
        return texto

    @staticmethod
    def check_is_italic(texto: str):
        check_italic = re.findall(r"_([^_]*(?:_[^_]+)*)_", texto, flags=re.IGNORECASE)
        if check_italic is not None:
            for word in check_italic:
                texto = texto.replace(f"_{word}_", f"<em>{word}</em>")
        return texto

    @staticmethod
    def check_is_list(texto: str):
        check_list = re.match(r"^\* (.*)", texto)
        if check_list is not None:
            return f"<li>{check_list.group(1)}</li>"
        return texto

    def check_encapsulate_list(self):
        texto = [texto.startswith('<li>') for texto in self.texto]
        list_start = False
        for i, boolList in enumerate(texto):
            if boolList:
                list_start = self.encapsulate_list(list_start, i)

    def encapsulate_list(self, list_start: bool, i: int):
        if not list_start:
            self.texto[i] = f"<ul>{self.texto[i]}"
            return True
        if (len(self.texto) > i + 1 and not self.texto[i + 1].startswith('<li>')) or len(self.texto) == i + 1:
            self.texto[i] = f"{self.texto[i]}</ul>"
            return False


def parse(markdown):
    class_converter = MarkdownToHTML(markdown)
    print(class_converter.converter())
    print('======================')


parse("This will be a paragraph")
parse("_This will be italic_")
parse("__This will be bold__")
parse("This will _be_ __mixed__")
parse("# This will be an h1")
parse("## This will be an h2")
parse("### This will be an h3")
parse("#### This will be an h4")
parse("##### This will be an h5")
parse("###### This will be an h6")
parse("####### This will not be an h7")
parse("* Item 1\n* Item 2")
parse("# Header!\n* __Bold Item__\n* _Italic Item_")
parse("# This is a header with # and * in the text")
parse("* Item 1 with a # in the text\n* Item 2 with * in the text")
parse("This is a paragraph with # and * in the text")
parse("# Start a list\n* Item 1\n* Item 2\nEnd a list")
parse("# Start a list\n* Item 1\n* Item 2\n* Item 3\nEnd a list")
parse("# Start a list\n* Item 1\n* Item 2\n* Item 3\n* Item 4\nEnd a list")
