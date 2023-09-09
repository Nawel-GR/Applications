import PyPDF2
from aspose.slides import Presentation, export
import os

'''
Transforms a ppt file(s) to pdf

'''
def ppt_to_pdf(files_path:list, file_name = r'pdf_merged',export_path=r'') -> list:
    '''
    if type(files_path) != list:
        files = [files_path]
    '''
    for i in range(len(files_path)):
        presentation = Presentation(files_path[i])
        presentation.save(file_name[i], export.SaveFormat.PDF)


'''
Merge PDF's in one PDF and save it in the path

'''
def merge_pdf(pdf_files:list, file_name = r'pdf_merged', export_path=r'') -> None:
    if type(pdf_files) != list:
        files = [pdf_files]

    merged_pdf = PyPDF2.PdfMerger()

    for pdf_file in pdf_files:
        merged_pdf.append(pdf_file)

    # Save merged PDF 
    merged_pdf.write(export_path +'\\' +file_name + '.pdf')
    merged_pdf.close()


if __name__ == '__main__':
    
    current_path = os.getcwd()
    
    list_path = [
    f"{current_path}/File.docx",
    ]

    list_ppt_path = [
    f"{current_path}/File1.ppt",
    f"{current_path}/File2.ppt",
    ]

    list_ppt_name = [
        f"{current_path}/File1.pdf",
    f"{current_path}/File2.pdf",
    ]



    ppt_to_pdf(list_ppt_path, list_ppt_name)

    merge_pdf(list_path, file_name='sample_A')