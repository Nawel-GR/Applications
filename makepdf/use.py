import mergepdf as merge


list_path = [
    r"C:\Users\nahue\Downloads\mini control2.1 - s4.pdf",
    r"C:\Users\nahue\Downloads\mini control2.2 - s4.pdf",
    r"C:\Users\nahue\Downloads\mini control2.b - s4.pdf"
]

list_ppt_path = [
    r"C:\Users\nahue\Downloads\Evaluacion_proyectos_TI_2023 (1).ppt",
    r"C:\Users\nahue\Downloads\Evaluacion_proyectos_TI_2023.ppt"

]

list_ppt_name = [
    r"C:\Users\nahue\Downloads\test_final1.pdf",
    r"C:\Users\nahue\Downloads\test_final2.pdf"
]



merge.ppt_to_pdf(list_ppt_path, list_ppt_name)

#merge.merge_pdf(list_path, file_name='test', export_path=r"C:\Users\nahue\Downloads\\")