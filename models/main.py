from .settings import Settings
from .table_data import TableData
from .calculate import Calculate
from .rtf_table import create_rtf_table
import win32clipboard


class Model:
    def __init__(self):
        self.settings = Settings()
        self.table_data = TableData(self.settings.get_number_of_elements())
        self.calculate = None

    def set_calculate(self):
        self.calculate = Calculate(self.settings.get_type_of_works(), self.settings.get_width_main_field(), self.settings.get_track(),
                                   self.settings.get_indicators_of_subgrade_slope(), self.table_data.get_table_data())

    def copy_table(self, info: list):
        rtf_table = create_rtf_table(self.table_data.get_table_headers(), self.table_data.get_table_data(), info)

        CF_RTF = win32clipboard.RegisterClipboardFormat("Rich Text Format")

        rtf = bytearray(rtf_table, 'cp1251')
        win32clipboard.OpenClipboard(0)
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(CF_RTF, rtf)
        win32clipboard.CloseClipboard()
