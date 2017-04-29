import gspread
from authorize import authenticate_google_docs
from operator import itemgetter

gc = authenticate_google_docs()
sh = gc.open('id_list')
worksheet = sh.get_worksheet(0)

def add_user(name, input_id, class_id):
    data_list = [input_id, name, '2', class_id]
    worksheet.append_row(data_list)

def get_name(input_id):
    cell_location = worksheet.find(input_id)
    user_name = worksheet.cell(cell_location.row, 2)
    return user_name.value

def get_id(name):
    cell_location = worksheet.find(name)
    user_id = worksheet.cell(cell_location.row, 1)
    return user_id.value

def set_status(input_id, status):
    cell_location = worksheet.find(input_id)
    if(worksheet.cell(cell_location.row, 3).value == '2'):
        worksheet.update_cell(cell_location.row, 3, status)
    else:
        print('You already scanned your finger, dumbass')

def clear_status():
    for x in range(2, worksheet.row_count+1):
        worksheet.update_cell(x, 3, '2')

def get_message_text():
    message = 'Engineering 1: \n'
    student_list_1 = []
    student_list_2 = []
    for x in range(2, worksheet.row_count+1):
	if(worksheet.cell(x, 3) != 0):
	    temp = []
	    temp.append(worksheet.cell(x, 2).value)
	    temp.append(worksheet.cell(x, 3).value)
	    if(worksheet.cell(x, 4).value == '1'):
	    	student_list_1.append(temp)
	    else:
                 student_list_2.append(temp)
    sorted(student_list_1, key=itemgetter(0))
    sorted(student_list_2, key=itemgetter(0))
    for x in range(0, len(student_list_1)):
    	message+='    '+student_list_1[x][0] + ', '
    	if(student_list_1[x][1] == '2'):
    	    message+='A \n'
	else:
	    message+='T \n'
    message +='\nEngineering 2: \n'
    for x in range(0, len(student_list_2)):
        message+='    '+student_list_2[x][0] + ', '
        if(student_list_2[x][1] == '2'):
            message+='A \n'
        else:
            message+='T /n>'
    return message
