import datetime as dt
import webbrowser as wb

while 1:
    time = dt.datetime.now()
    hour = str(time.hour)
    minute = str(time.minute)

    password = hour + minute

    inp = str(input(">>> "))

    if inp != password:
        print("Kirishga ruxsat yo'q!")
    else:
        print("Kirishga ruxsat berildi")
        wb.open("https://asulaymon.netlify.app")