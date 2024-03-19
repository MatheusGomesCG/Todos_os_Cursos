import win32com.client as win32

def abrir_excel(path, sheet_name, cell, content):
    try:
        excel = win32.Dispatch("Excel.Application")
        excel.Visible = True
        wb = excel.Workbooks.Add()
        sheet = wb.Sheets(1)

        #renomear
        sheet.name = sheet_name

        #escrever conteudo
        sheet.Range(cell).Value = content

        #salvar
        wb.SaveAs(path)

        excel.Quit()

    except Exception as e:
        print("Ocorreu o erro:", e)

path = 'exemplo 01.xlsx'
sheet_name = "Exemplo 01"
cell = "A1"
content = "Curso de automaziação SAP"

abrir_excel(path, sheet_name, cell, content)
print('instalação concluida')