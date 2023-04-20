import PyPDF2
from aspose.slides import Presentation, export

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
