import datetime

"""
import PyPDF2
pdf_file = open('C:\\Users\\cande\\Desktop\\uni_dates.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
page_content.encode('utf-8')
content_list = page_content.split('\n')
content_list = content_list[getDateLabel(23)]]
"""
def getDateLabel(index):
	if index == 0:
		return "summer_start_date"
	elif index == 1:
		return "break_mid_term_start_date"
	elif index == 2:
		return "break_mid_term_end_date"
	elif index == 3:	
		return "summer_end_date"
	elif index == 4:
		return "summer_exam_start"
	elif index == 5:
		return "summer_exam_end"
	elif index == 6:
		return "semester_1_start_date"
	elif index == 7:
		return "semester_1_break_start_date"
	elif index == 8:
		return "semester_1_break_end_date"
	elif index == 9:	
		return "semester_1_end_date"
	elif index == 10:
		return "semester_1_exam_start"
	elif index ==11:
		return "semester_1_exam_end"
	elif index == 12:
		return "semester_2_start_date"
	elif index == 13:
		return "semester_2_break_start_date"
	elif index == 14:
		return "semester_2_break_end_date"
	elif index == 15:	
		return "semester_2_end_date"
	elif index == 16:
		return "semester_2_exam_start"
	elif index == 17:
		return "semester_2_exam_end"

universities = {}
uni_info = {}

uni_info[getDateLabel(0)] = datetime.datetime.strptime("02 Jan 17", "%d %b %y")
uni_info[getDateLabel(1)]= "N/A"
uni_info[getDateLabel(2)]= "N/A"
uni_info[getDateLabel(3)]= datetime.datetime.strptime("09 Feb 18", "%d %b %y")
uni_info[getDateLabel(4)]= datetime.datetime.strptime("12 Feb 18", "%d %b %y")
uni_info[getDateLabel(5)]= datetime.datetime.strptime("16 Feb 18", "%d %b %y")
uni_info[getDateLabel(6)]= datetime.datetime.strptime("26 Feb 18", "%d %b %y")
uni_info[getDateLabel(7)]= datetime.datetime.strptime("30 Mar 18", "%d %b %y")
uni_info[getDateLabel(8)]= datetime.datetime.strptime("08 Apr  18", "%d %b %y")
uni_info[getDateLabel(9)]= datetime.datetime.strptime("27 May 18", "%d %b %y")
uni_info[getDateLabel(10)] = datetime.datetime.strptime("04 Jun 18", "%d %b %y")
uni_info[getDateLabel(11)] = datetime.datetime.strptime("22 Jun 18", "%d %b %y")
uni_info[getDateLabel(12)] = datetime.datetime.strptime("23 Jul 18", "%d %b %y")
uni_info[getDateLabel(13)] = datetime.datetime.strptime("24 Sep 18", "%d %b %y")
uni_info[getDateLabel(14)] = datetime.datetime.strptime("30 Sep 18", "%d %b %y")
uni_info[getDateLabel(15)] = datetime.datetime.strptime("21 Oct 18", "%d %b %y")
uni_info[getDateLabel(16)] = datetime.datetime.strptime("29 Oct 18", "%d %b %y")
uni_info[getDateLabel(17)] = datetime.datetime.strptime("16 Nov 18", "%d %b %y")

universities["University of Melbourne"] = uni_info

"""
state_name = ""
university_name = ""
universities = {}
uni_info = {}
index_count = 0

for s in content_list:
	if s.isupper(): # If string is state
		state_name = s
		print(s)
	elif s.isalpha(): # If string is university name
		universities[getDateLabel(un)]versity_name] = uni_info
		univeristy_name = s
		uni_info = {}
		uni_info["state"] = state_name
		index_count = 0
	elif s != "-":
		uni_info[getDateLabel(ge)]DateLabel(index_count)] = s
		index_count += 1

print(universities)
"""
