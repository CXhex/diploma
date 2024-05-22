# Функция для создания RTF-строки из списка данных
def create_rtf_table(titles, data, info):

    rtf_table = "{\\rtf1\\ansi\\ansicpg1251\\deff0\\deflang1049{\\fonttbl{\\f0\\fnil\\fcharset204 Times New Roman;}{\\f1\\fnil\\fcharset0 Times New Roman;}}\\trowd\\sl360\\slmult1{"
    titles_copy = titles.copy()
    titles_copy.insert(0, "№")

    table_len = 440 + len(titles_copy) * 1440
    for title, c in zip(titles_copy, range(440, table_len, 1440)):
        title = title.replace("\n", "\\line")
        rtf_table += "\\clbrdrt\\brdrs\\clbrdrl\\brdrs\\clbrdrb\\brdrs\\clbrdrr\\brdrs"
        rtf_table += f"\\clvertalc\\cellx{str(c)} {str(title)}\\qc\\intbl\\cell"
    
    rtf_table += "\\row"

    for row, number in zip(data, range(1, len(data) + 1)):
        c = 440
        rtf_table += "\\trowd\\clbrdrt\\brdrs\\clbrdrl\\brdrs\\clbrdrb\\brdrs\\clbrdrr\\brdrs"
        rtf_table += f"\\clvertalc\\cellx{str(c)} {str(number)}\\qc\\intbl\\cell"
        for col in row:
            c += 1440
            rtf_table += "\\clbrdrt\\brdrs\\clbrdrl\\brdrs\\clbrdrb\\brdrs\\clbrdrr\\brdrs"
            rtf_table += f"\\clvertalc\\cellx{str(c)} {str(col)}\\qc\\intbl\\cell"
            
        rtf_table += "\\row"
        
    rtf_table += "}{"
    
    for item in info:
        rtf_table += f"\\fs28{item}\\par"
        
    rtf_table += "}}}"
    
    return rtf_table
