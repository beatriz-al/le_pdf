import fitz  # pip install PyMuPDF
from tika import parser  # pip install tika
#raw = parser.from_file(pdf_path)
# print(raw['content'])

pdf_path = r'..\\read_pdf\\relação de bens moveis por UORG.pdf'
print(pdf_path)


def le_pdf(pdf_path):

    # faz leitura do PDF
    with fitz.open(pdf_path) as doc:
        #texto = ""
        blocks = []
        for pagina in doc:
            #texto += pagina.get_text()
            blocks.append(pagina.get_text("blocks"))
    # print(texto)
    str1 = 'DESTINAÇÃO'
    str2 = 'MIN.'

    marcador_linha = '+------------+-----------+----------------------------------------------------+'
    output = []

    for block in blocks:
        # isola a tabela
        tabela = str(block).partition(str1)[2].partition(str2)[0]
        linha = tabela.split(marcador_linha)

        for i in linha:
            try:
                item = i.split('|')

                # 81 => Cada linha
                # 83 => Diferenca do topo e rodape
                bloco_linha = (len(i) - 83)/81
                if bloco_linha >= 1:
                    txt = ''
                    for j in range(int(bloco_linha)):
                        value = 3 + (int(j) * 4)
                        txt = txt + str(item[int(value)]).strip()
                    if " '" in txt:
                        txt = txt.replace(" '", '')
                """             
                if len(i) < 164:
                    continue
                
                elif len(i) == 164:
                    item = str(item[3]).strip()

                elif len(i) > 164 and len(i) < 326: 
                    item = str(item[3]).strip() + str(item[7]).strip()
                    print(len(i))


                elif len(i) == 326: 
                    item = str(item[3]).strip() + str(item[7]).strip() +str(item[11]).strip() """

                if txt in output:
                    pass
                else:
                    output.append(txt)
            except:
                pass

    print(output)

    with open("Output.txt", "w") as file:
        content = str(output)
        file.write(content)
        file.close()


le_pdf(pdf_path)
