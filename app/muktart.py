#!/usr/bin/env python3

# Copyright (C) 2023 MuKonqi (Muhammed Abdurrahman)

# Muktart is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Muktart is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Muktart.  If not, see <https://www.gnu.org/licenses/>.

from tkinter import *
from tkinter import messagebox
from subprocess import *
import subprocess
import os
import getpass
username=getpass.getuser()

en="/home/"+username+"/.by-mukonqi/muktart/en.txt"
tr="/home/"+username+"/.by-mukonqi/muktart/tr.txt"

def settings():
    if not os.path.isfile("/home/"+username+"/.by-mukonqi/muktart/dark.txt") and not os.path.isfile("/home/"+username+"/.by-mukonqi/muktart/light.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    if os.path.isfile("/home/"+username+"/.by-mukonqi/muktart/dark.txt"):
        bg="#000000"
        fg="#FFFFFF"
        button_bg="#FFFFFF"
        button_fg="#000000"
        a_button_bg="#000000"
        a_button_fg="#FFFFFF"
    elif os.path.isfile("/home/"+username+"/.by-mukonqi/muktart/light.txt"):
        bg="#FFFFFF"
        fg="#000000"
        button_bg="#000000"
        button_fg="#FFFFFF"
        a_button_bg="#FFFFFF"
        a_button_fg="#000000"
    def dark():
        os.system("cd /home/"+username+"/.by-mukonqi/muktart/ ; rm light.txt ; touch dark.txt")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Successful! Dark theme applied.")
        if os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Koyu tema uygulandı.")
        swindow.destroy()
        os.system("python3 /usr/local/bin/muktart/muktart.py")
    def light():
        os.system("cd /home/"+username+"/.by-mukonqi/muktart/ ; rm dark.txt ; touch light.txt")
        if os.path.isfile(en):
            messagebox.showinfo("Information","Successful! Light theme applied.")
        if os.path.isfile(tr):
            messagebox.showinfo("Bilgilendirme","Başarılı! Açık tema uygulandı.")
        swindow.destroy()
        os.system("python3 /usr/local/bin/muktart/muktart.py")
    def langen():
        os.system("cd /home/"+username+"/.by-mukonqi/muktart/ ; rm tr.txt ; touch en.txt")
        messagebox.showinfo("Information","Successful! English language applied.")
        swindow.destroy()
        os.system("python3 /usr/local/bin/muktart/muktart.py")
    def langtr():
        os.system("cd /home/"+username+"/.by-mukonqi/muktart/ ; rm en.txt ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","Başarılı! Türkçe dili uygulandı.") 
        swindow.destroy()
        os.system("python3 /usr/local/bin/muktart/muktart.py")
    swindow=Tk()
    swindow.config(background=bg)
    swindow.resizable(0, 0)
    if os.path.isfile(en):
        swindow.title("Settings | Muktart")
        stext1=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="Please select the theme you want to apply.")
        sspace1=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(swindow, text="Dark", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth="3 ")
        sbutton2=Button(swindow, text="Light", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3" )
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="You can change your language preferences below.")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton3=Button(swindow, text="English (English)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font=",arial 10", cursor="hand2", borderwidth ="3")
        sbutton4=Button(swindow, text="Turkish (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth= "3")
    if os.path.isfile(tr):
        swindow.title("Ayarlar | Muktart")
        stext1=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="Lütfen uygulamak istediğiniz temayı seçiniz.")
        sspace1=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton1=Button(swindow, text="Koyu", command=dark, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        sbutton2=Button(swindow, text="Açık", command=light, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n\n")
        stext2=Label(swindow, background=bg, foreground=fg, font="arial 10 bold", text="Aşağıdan dil tercihlerinizi değiştirebilirsiniz.")
        sspace2=Label(swindow, background=bg, foreground=fg, font="arial 3", text="\n")
        sbutton3=Button(swindow, text="English (İngilizce)", command=langen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
        sbutton4=Button(swindow, text="Türkçe (Turkish)", command=langtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    stext1.pack()
    sspace1.pack()
    sbutton1.pack()
    sbutton2.pack()
    sspace2.pack()
    stext2.pack()
    sspace2.pack()
    sbutton3.pack()
    sbutton4.pack()
    mainloop()
    exit()
    
def first_start():
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
    def llangen():
        os.system("cd /home/"+username+"/.by-mukonqi/muktart ; touch en.txt")
        messagebox.showinfo("Information","English language applied! When you click 'OK', Muktart settings will open.")
        lwindow.destroy()
        settings()
    def llangtr():
        os.system("cd /home/"+username+"/.by-mukonqi/muktart ; touch tr.txt")
        messagebox.showinfo("Bilgilendirme","İstenilen dil uygulandı! 'OK' tuşuna bastığınızda Muktart ayarları açılacak.")
        lwindow.destroy()
        settings()
    lwindow=Tk()
    lwindow.title("Choose a language for Muktart")
    lwindow.config(background=bg)
    lwindow.resizable(0, 0)
    ltext1=Label(lwindow, background=bg, foreground=fg, font="arial 10 bold", text="Please choose a language.\nLütfen bir dil seçin.")
    ltext1.pack()
    lspace1=Label(lwindow, background=bg, foreground=fg, font="arial 3", text="\n")
    lspace1.pack()
    lbutton1=Button(lwindow, text="English (İngilizce)", command=llangen, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg,  font=",arial 10", cursor="hand2", borderwidth="3")
    lbutton1.pack()
    lbutton2=Button(lwindow, text="Türkçe (Turkish)", command=llangtr, background=button_bg, foreground=button_fg, activebackground=a_button_bg, activeforeground=a_button_fg, font="arial 10", cursor="hand2", borderwidth="3")
    lbutton2.pack()
    mainloop()

if not os.path.isdir("/home/"+username+"/.by-mukonqi/"):
    os.system("cd /home/"+username+" ; mkdir .by-mukonqi")
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir muktart")
    first_start()
if not os.path.isdir("/home/"+username+"/.by-mukonqi/muktart"):
    os.system("cd /home/"+username+"/.by-mukonqi ; mkdir muktart")
    first_start()
    
bg=""
fg=""
button_bg=""
button_fg=""
a_button_bg=""
a_button_fg=""
if os.path.isfile("/home/"+username+"/.by-mukonqi/muktart/dark.txt"):
    bg="#000000"
    fg="#FFFFFF"
    button_bg="#FFFFFF"
    button_fg="#000000"
    a_button_bg="#000000"
    a_button_fg="#FFFFFF"
elif os.path.isfile("/home/"+username+"/.by-mukonqi/muktart/light.txt"):
    bg="#FFFFFF"
    fg="#000000"
    button_bg="#000000"
    button_fg="#FFFFFF"
    a_button_bg="#FFFFFF"
    a_button_fg="#000000"
else:
    if os.path.isfile(en):
        messagebox.showwarning("Warning","Can't found theme config. When you click 'OK' settings will open.")
    elif os.path.isfile(tr):
        messagebox.showwarning("Uyarı","Tema yapılandırması bulunamadı, ayarlar 'OK' tuşuna bastığınızda açılacaktır.")
    settings()
    exit()
    
def module_exit():
    exit("\nThis module is shutting down...\nModül kapatılıyor...")

window=Tk()
window.config(background=bg)
window.resizable(0, 0)
name=Entry()

cmd='/^Exec=/ {sub("^Exec=", ""); gsub(" ?%[cDdFfikmNnUuv]", ""); exit system($0)}'
def run():
    if appentry.get() == "" or appentry.get() == "Application Name" or appentry.get() == "Uygulama Adı":
        if os.path.isfile(en):
            messagebox.showerror("Fatal error!","You didn't type a application name.")
        elif os.path.isfile(tr):
            messagebox.showerror("Ölümcül hata!","Herhangi bir uygulama adı girmediniz.")
            return None
            
    def show():
        outputs=Toplevel()
        outputs.config(background=bg)
        outputs.resizable(0, 0) 
        if os.path.isfile(en):
            outputs.title("Outputs")
            scroll=Scrollbar(outputs)
            text4=Label(outputs, background=bg, foreground=fg, font="arial 14", text="\nThe output is below.\n")
            text5=Text(outputs, yscrollcommand=scroll.set)
            text5.insert(END, out)
            text5.insert(END, err)
            scroll.config(command=text5.yview)
            space5=Label(outputs, background=bg, foreground=fg, text="\n", font="arial 3")
            button2=Button(outputs, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Close window", command=outputs.destroy)
        elif os.path.isfile(tr):
            outputs.title("Çıktılar")
            scroll=Scrollbar(outputs)
            text4=Label(outputs, background=bg, foreground=fg, font="arial 14", text="\nÇıktı aşağıdadır.\n")
            text5=Text(outputs, yscrollcommand=scroll.set)            
            text5.insert(END, out)
            text5.insert(END, err)
            scroll.config(command=text5.yview)
            space5=Label(outputs, background=bg, foreground=fg, text="\n", font="arial 3")
            button2=Button(outputs, cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, background=button_bg, foreground=button_fg, borderwidth="3", text="Pencereyi kapat", command=outputs.destroy)            
        scroll.pack(side=RIGHT,fill=Y)
        text4.pack()
        text5.pack()
        text5.config(state=DISABLED)
        space5.pack()
        button2.pack()
          
    if os.path.isfile(en):
        rtext3=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Status: Running, please wait.")
    elif os.path.isfile(tr):
        rtext3=Label(window, background=bg, foreground=fg, font="arial 10 bold", text="Durum: Çalışıyor, lütfen bekleyin.")
    rtext3.pack() 
    if passentry.get() == "Password (for sudo)" or passentry.get() == "Şifre (sudo için)" or passentry.get() == "":
        result = subprocess.Popen("awk '"+cmd+"' /usr/share/applications/"+appentry.get()+".desktop", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
    else:
        result = subprocess.Popen("echo "+passentry.get()+" | sudo -S "+"awk '"+cmd+"' /usr/share/applications/"+appentry.get()+".desktop", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True)
    (out, err) = result.communicate()
    if os.path.isfile(en):
        rtext3.config(text="Status: Completed. Output is ready.")
        rbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Show results",command=show)
    elif os.path.isfile(tr):
        rtext3.config(text="Durum: Tamamlandı. Çıktı hazır.")
        rbutton1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Sonuçları göster",command=show)
    rbutton1.pack()
def dae(e):
    appentry.delete(0, END)
def dpe(e):
    passentry.delete(0, END)

space1=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
space2=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
space3=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
space4=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")
space5=Label(window, background=bg, foreground=fg, text="\n", font="arial 3")

apps = subprocess.Popen("cd /usr/share/applications ; ls *.desktop -1 | sed -e 's/\.desktop$//'", shell=TRUE, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE,universal_newlines=True)
(out, err)=apps.communicate() 
scroll=Scrollbar(window)
text1=Text(window, yscrollcommand=scroll.set)
text1.insert(END, out)
text1.insert(END, err)
scroll.config(command=text1.yview)
text1.config(state=DISABLED)
if os.path.isfile(en):
    window.title("Main Page | Muktart")
    label1=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="The applications are listed below.")
    label2=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="Please type a application name below.\nJust fill in the password box whenever you want to use sudo.")        
    appentry=Entry(window)
    appentry.insert(0, "Application Name")
    appentry.bind("<FocusIn>", dae)
    passentry=Entry(window)
    passentry.insert(0, "Password (for sudo)")
    passentry.bind("<FocusIn>", dpe)        
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Start",command=run)
elif os.path.isfile(tr):
    window.title("Ana Sayfa | Muktart")
    label1=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="Aşağıda uygulamalar listelenmiştir.")
    label2=Label(window, background=bg, foreground=fg, font="arial 14 bold", text="Lütfen aşağıya bir uygulama adı yazın.\nSadece sudo kullanmak istediğiniz zamanlarda şifre kutucuğunu doldurun.")  
    appentry=Entry(window)
    appentry.insert(0, "Uygulama Adı")
    appentry.bind("<FocusIn>", dae)
    passentry=Entry(window)
    passentry.insert(0, "Şifre (sudo için)")
    passentry.bind("<FocusIn>", dpe)
    button1=Button(window, font="arial 10", cursor="hand2", activebackground=a_button_bg, activeforeground=a_button_fg, foreground=button_fg, borderwidth="3", background=button_bg, text="Başlat",command=run)        
scroll.pack(side=RIGHT, fill=Y)
space1.pack()
label1.pack()
space2.pack()
text1.pack()
space3.pack()
label2.pack()
space4.pack()
appentry.pack()
passentry.pack()
space5.pack()
button1.pack()
mainloop()