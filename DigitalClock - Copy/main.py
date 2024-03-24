from tkinter import *
import datetime


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    lab_hr.config(text=hr)
    lab_min.config(text=minute)
    lab_sec.config(text=second)
    lab_am.config(text=am_pm)
    lab_hr.after(200,date_time)#200miliseconds

    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)



#print(datetime.datetime.now())

clock = Tk()

clock.title("DIGITAL CLOCK")
clock.geometry('1000x500')
clock.config(bg='#07091E')

custom_font = 'Seven Segment'
font_color = 'white'
box_background= '#2C9BF4'
text_font_color = 'white'
text_box_background='#1D86D9'
#text_font= 'century gothic'
#text_font= 'poppins regular'
text_font= 'Lato'



am_day_box = '#FF006A'
text_am_day_box ='#EC0062'


lab_hr =Label(clock,text='00',font=(custom_font,55,"bold"),bg=box_background,fg=font_color)
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_text = Label(clock, text='Hour', font=(text_font, 20, "normal"), bg=text_box_background, fg=text_font_color)
lab_hr_text.place(x=120, y=190, height=40, width=100)



lab_min =Label(clock,text='00',font=(custom_font,55,"bold"),bg=box_background,fg=font_color)
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_text =Label(clock,text='Min.',font=(text_font,20,"normal"),bg=text_box_background,fg=text_font_color)
lab_min_text.place(x=340,y=190,height=40,width=100)


lab_sec =Label(clock,text='00',font=(custom_font,55,"bold"),bg=box_background,fg=font_color)
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_text =Label(clock,text='Sec',font=(text_font,20,"normal"),bg=text_box_background,fg=text_font_color)
lab_sec_text.place(x=560,y=190,height=40,width=100)


lab_am =Label(clock,text='00',font=(custom_font,50,"bold"),bg=am_day_box,fg=font_color)
lab_am.place(x=780,y=50,height=110,width=100)
lab_am_text =Label(clock,text='AM/PM',font=(text_font,20,"normal"),bg=text_am_day_box,fg=text_font_color)
lab_am_text.place(x=780,y=190,height=40,width=100)





lab_date =Label(clock,text='00',font=(custom_font,55,"bold"),bg=box_background,fg=font_color)
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_text =Label(clock,text='Date',font=(text_font,20,"normal"),bg=text_box_background,fg=text_font_color)
lab_date_text.place(x=120,y=410,height=40,width=100)

lab_mon =Label(clock,text='00',font=(custom_font,55,"bold"),bg=box_background,fg=font_color)
lab_mon.place(x=340,y=270,height=110,width=100)
lab_mon_text =Label(clock,text='Month',font=(text_font,20,"normal"),bg=text_box_background,fg=text_font_color)
lab_mon_text.place(x=340,y=410,height=40,width=100)

lab_year =Label(clock,text='00',font=(custom_font,55,"bold"),bg=box_background,fg=font_color)
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_text =Label(clock,text='Year',font=(text_font,20,"normal"),bg=text_box_background,fg=text_font_color)
lab_year_text.place(x=560,y=410,height=40,width=100)

lab_day =Label(clock,text='00',font=(custom_font,35,"bold"),bg=am_day_box,fg=font_color)
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_text =Label(clock,text='Day',font=(text_font,20,"normal"),bg=text_am_day_box,fg=text_font_color)
lab_day_text.place(x=780,y=410,height=40,width=100)


date_time()

clock.mainloop()