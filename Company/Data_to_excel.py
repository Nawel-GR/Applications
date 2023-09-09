import os
import pandas as pd
import tabula as tb
import numpy as np
from window_values import WindowTK


def main():
    w = WindowTK()
    file_path = w.get_file()
    save_path = w.get_save()

    columns = [111.433, 175.142, 450.397, 543.008, 653.984]
    area = [103.287,35.394,578.02,788.594]

    # Read the pdf and extract the tables
    tables = tb.read_pdf(file_path, area=area, columns = columns, pages = 'all')


    # concat tables
    merged_table = pd.concat(tables, ignore_index=True)


    for i in range(1, len(merged_table)):
        # Verificar si la fila i tiene información en 'Descripción' pero todos los demás valores son NaN
        if not pd.notna(merged_table.at[i, 'Código']) and not pd.notna(merged_table.at[i, 'Secuencia']) and pd.notna(merged_table.at[i, 'Descripción']) and not pd.notna(merged_table.at[i, 'Código Anterior']) and not pd.notna(merged_table.at[i, 'Código Barra']):
            # Copiar la información de 'Descripción' de la fila i a la fila i-1
            merged_table.at[i - 1, 'Descripción'] = merged_table.at[i - 1, 'Descripción'] + ' ' + merged_table.at[i, 'Descripción']
            # Marcar la fila i como NaN en todas las columnas
            merged_table.at[i, 'Descripción'] = np.nan

    for i in range(1, len(merged_table)):
        if not pd.notna(merged_table.at[i, 'Código']) and not pd.notna(merged_table.at[i, 'Secuencia']) and not pd.notna(merged_table.at[i, 'Descripción']) and not pd.notna(merged_table.at[i, 'Código Anterior']) and not pd.notna(merged_table.at[i, 'Código Barra']) and pd.notna(merged_table.at[i, 'Ubicación Fisica']):
            # Copiar la información de 'Descripción' de la fila i a la fila i-1
            merged_table.at[i - 1, 'Ubicación Fisica'] = str(merged_table.at[i - 1, 'Ubicación Fisica']) + ' ' + str(merged_table.at[i, 'Ubicación Fisica'])
            # Marcar la fila i como NaN en todas las columnas
            merged_table.iloc[i] = np.nan


    merged_table.dropna(subset = ['Ubicación Fisica'],inplace=True, ignore_index = True)

    # Guardar la tabla completa en un archivo CSV
    merged_table.to_excel(f"{save_path}/informe_completo_merged.xlsx", sheet_name='Data', index=False)


if __name__ == '__main__':
    main()