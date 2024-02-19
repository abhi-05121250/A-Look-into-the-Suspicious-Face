import pandas as pd
from datetime import datetime
from datetime import date

def format_col_width(ws):
    ws.set_row('A:B', 20)

# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': []})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_image.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

# Insert an image.
#worksheet.insert_image('D3', 'D:\python\Ai and ml\code\opencv_frame_1.png',{})
unkimg='D:\python\Ai and ml\code\opencv_frame_1.png'
x_scale=0.2
y_scale=0.1
worksheet.insert_image('A1', unkimg,{'x_scale':x_scale , 'y_scale': y_scale})
worksheet.insert_image('A3', 'D:\python\Ai and ml\code\opencv_frame_2.png',{'x_scale':x_scale , 'y_scale': y_scale})

# Close the Pandas Excel writer and output the Excel file.
writer.save()
