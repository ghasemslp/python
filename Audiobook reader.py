#کتابخانه ها
from tkinter import *
import PyPDF2
import pyttsx3
from tkinter.filedialog import askopenfilename

#ساخت پنجره و نامگذاری
window = Tk()
window.title("KETAB")

#تنظیم سایز پنجره
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=600, weight=1)

#ساخت الگوریتم
def open_file():
    #انتخاب فایل
    file = askopenfilename(title="Select file", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    #پیدا کردن فایل 
    if file:
        pdf_file = PyPDF2.PdfFileReader(file)
        page_numbers = pdf_file.numPages
        for page in range(page_numbers):
            # تلاش برای تبدیل پی دی اف 
            # اضافه کردن به پنجره
            #مدیریت خطا
            try:
                CURRENT_page = pdf_file.getPage(page)
                text = CURRENT_page.extractText()
                txt_edit.insert(END, text)
            except:
                pass
#تابع خواندن متن های درون صفحه
def red_file():
    Text = txt_edit.get("1.0", END).splitlines()
    engine = pyttsx3.init()

    # تنظیمات صدا
    voices = engine.getProperty('voices')
    # انتخاب صدای زن (معمولاً صدای زن در اندیس ۱ قرار دارد)
    engine.setProperty('voice', voices[1].id)  # تغییر به صدای زن
    engine.setProperty("rate", 150)  # تنظیم سرعت خواندن

    for line in Text:
        engine.say(line)
    engine.runAndWait()
#باتون ها
txt_edit = Text(window)
frm_btuns = Frame(window, relief=RAISED, bd=2)
btn_open = Button(frm_btuns, text="بازکردن فایل", command=open_file)
btn_read = Button(frm_btuns, text="خواندن فایل", command=red_file)
btn_open.grid(row=0, column=0, sticky="EW", padx=5, pady=5)
btn_read.grid(row=1, column=0, sticky="EW", padx=5, pady=5)
frm_btuns.grid(row=0, column=0, sticky="NS")
txt_edit.grid(row=0, column=1, sticky="NSEW")

window.mainloop()

#Git_hub : Ghasemslp
#Instageram : Ghasem_slp
   #لطفا حمایت کنید
