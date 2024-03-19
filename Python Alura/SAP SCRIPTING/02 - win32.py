import win32com.client

w = win32com.client.Dispatch("Word.Application")
w.Visible = 1

w.WindowState = win32com.client.constants.wdWindowStateMinimize