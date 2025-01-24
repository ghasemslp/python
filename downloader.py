#کتابخانه های مورد نیاز
from urllib.parse import urlparse
from colorama import Fore,init
import time,os,httpx
init()

def Downloader(pasvand):
    x = 0
    List = []
    for i in range(len(List_date_org)):
        line_img = List_date_org[x].count("img")
        if line_img == True:
            try:
                start = List_date_org[x].find("data-src=")
                end = List_date_org[x].find(pasvand)
                end += len(pasvand)
                start += 10
                url_img = List_date_org[x][start:end]
                List.append(url_img)
                x += 1
            except ValueError:
                x += 1
        else:
            x += 1
    List_org = [string for string in List if string]
    x = 0
    print(Fore.YELLOW+"Download photo with "+Fore.RED +pasvand+ Fore.YELLOW+" extension"+Fore.WHITE)
    for i in range(len(List_org)):
        #ادرس دادن به دانلودر
        Addres_photo = List_org[x]
        # پیدا کردن اسم اصلی عکس برای ذخیره
        Name = urlparse(Addres_photo)
        Photo_name = (os.path.basename(Name.path))
        #تشخیص درست بودن لینک
        Request = httpx.get(Addres_photo)
        #درخواست ذخیره
        new_path = "download img"
        full_path = os.path.join(new_path, Photo_name)
        with open(full_path,"wb") as Photo:
            Photo.write(Request.content)
            if True:
                print("The photo {"+Fore.GREEN+Photo_name+Fore.WHITE+"} was downloaded")
        x += 1
        if len(List_org) == 0:
            os.system("cls")
            print("You don't have permission to access this resource.")
#خوش آمد گویی
os.system("cls")
print("Hi",end="\r")
time.sleep(1)
print("Welcome To Python app")
time.sleep(2)
os.system("cls")
print("Start Download:")

#ساخت فولدری در صورت وجود نداشتن
try:
    os.makedirs("download img", exist_ok=True)
except:
    pass

#دریافت سایت
#برسی لینک
os.system("cls")
while True:
    link = input("Please enter a Site link: ")
    if link.startswith("https://"):
        break
    else:
        print("Invalid link. Please enter a link starting with 'https://'.")
links = link.find(",")
if links != 0:
    links = link.split(",")
    x = 0
    List_date_site = []
    reshte_test = " "
    List_date_orgs = []
    #دریافت کد های سایت
    for i in range(len(links)):
        response = httpx.get(links[x])
        Data_site = response.text
        # List_date_site.append(Data_site)
        reshte_test += Data_site 
        x += 1
    date_up = reshte_test.split("\n")
    line_dates = []
    x = 0
    for i in range(len(date_up)):
        line = date_up[x].strip()
        line_dates.append(line)
        x += 1
    List_date_org = [string for string in line_dates if string]
    Downloader("png")
    Downloader("jpg")
    Downloader("jpeg")
    Downloader("svg")
    Downloader("webp")
else:
    #دریافت کد های سایت
    response = httpx.get(link)
    Data_site = response.text


    #وارد لیست کردن اطلاعات سایت
    data_up = Data_site.split("\n")
    #و حذف فاصله ها
    List_date = []
    x = 0
    for i in range(len(data_up)):
        line = data_up[x].strip()
        List_date.append(line)
        x += 1

    #حذف رشته های خالی
    List_date_org = [string for string in List_date if string]

    Downloader("png")
    Downloader("jpg")
    Downloader("jpeg")
    Downloader("svg")
    Downloader("webp")

#instageram = Ghasem_slp
#Git_hob = Ghasemslp