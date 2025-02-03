import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk


def show_frame(frame):
    """פונקציה להציג מסגרת מסוימת ולהסתיר את השאר"""
    frame.tkraise()

def test_info(user_name, password, password_ver):
    #מוריד רווחים בסיסמאות
    password = password.get().strip()
    password_ver = password_ver.get().strip()

    # get() מביא לי את הערך ממה שהמשתמש הכניס
    user_name = user_name.get()
    if len(user_name) == 0:
        messagebox.showerror("שגיאה", "הכנס שם משתמש")
        return 0
    if len(user_name) < 5 or len(user_name) > 30:
        messagebox.showerror("שגיאה", "אורך שם משתמש לא תקין")
        return 0
    if password != password_ver:
        messagebox.showerror("שגיאה", "אימות סיסמא לא תקין")
        return 0
    if len(password) < 5 or len(password) > 15:
        messagebox.showerror("שגיאה", "אורך הסיסמא לא תקין")
        return 0

    file_path = 'data.csv'
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == user_name:
                messagebox.showerror("שגיאה", "שם משתמש קיים, בחר שם משתמש אחר")
                return 0
    new_data = [user_name, password]
    # הוספת הערכים לקובץ CSV
    with open("data.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(new_data)
    messagebox.showinfo("אישור","יצירת החשבון הצליחה")
    return 0

def login_details(user_name, user_password):
    user_password = user_password.get().strip()
    user_name = user_name.get()
    if len(user_name) == 0:
        messagebox.showerror("שגיאה","הכנס שם משתמש")
        return 0
    if len(user_password) == 0:
        messagebox.showerror("שגיאה", "הכנס סיסמא")
        return 0
    file_path = 'data.csv'
    with open(file_path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == user_name and row[1] == user_password:
                messagebox.showinfo("אישור", "התחברות הצליחה")
                messagebox.showinfo("ברוך הבא", f"{user_name}")
                return 0
        messagebox.showerror("שגיאה", "שם משתמש או סיסמא לא נכונים")
        return 0

def clear_input(user_delet,password_delet,password_ver):
    user_delet.delete(0, tk.END)
    password_delet.delete(0, tk.END)
    password_ver.delete(0, tk.END)




# יצירת החלון הראשי
root = tk.Tk()
root.title("התחברות משתמש")
root.geometry("600x600")


# יצירת מסגרות (Frames) עבור המסכים
home_page = tk.Frame(root)
page1 = tk.Frame(root)
page2 = tk.Frame(root)

# הוספת תמונה למסך הבית
canvas = tk.Canvas(home_page, width=600, height=600)
canvas.pack()

image = Image.open("con_pic.png")  # תומך בפורמטים כמו JPEG, PNG, וכו'
image = image.resize((300, 300))  # התאמת גודל (אופציונלי)
pic = ImageTk.PhotoImage(image)

canvas.create_image(300, 300, image=pic)


for frame in (home_page, page1, page2):
    frame.place(relwidth=1, relheight=1)  # למלא את כל החלון

button_new = tk.Button(home_page, text="יצירת חשבון חדש", command=lambda: show_frame(page1))
button_new.pack()
button_new.place(x=470, y=400)

button_open = tk.Button(home_page, text="כניסה לחשבון קיים", command=lambda: show_frame(page2))
button_open.pack()
button_open.place(x=30, y=400)

label_bass = tk.Label(home_page, text="ברוכים הבאים לאתר ההתחברות", font=("Arial",24))
label_bass.place(x=100, y=100)


# תוכן של עמוד 1
button1 = tk.Button(page1, text="חזור",width=10, command=lambda: show_frame(home_page))
button1.pack()
button1.place(x=480, y=20)

label1 = tk.Label(page1, text="יצירת חשבון חדש", font=("Arial", 24))
label1.place(x=350, y=100)

label2 = tk.Label(page1, text="שם המשתמש יכיל מעל 4 תווים ועד 30 תווים", font=("Arial", 10))
label2.place(x=330, y=180)
input_userName = tk.Entry(page1, width=30)
input_userName.place(x=370, y=210)

label3 = tk.Label(page1, text="הסיסמא תכיל מעל 5 תווים ועד 15 תווים", font=("Arial", 10))
label3.place(x=355, y=250)
input_password = tk.Entry(page1, width=30)
input_password.place(x=370, y=280)

label4 = tk.Label(page1, text="אימות סיסמא", font=("Arial", 10))
label4.place(x=485, y=310)
input_password_ver = tk.Entry(page1, width=30)
input_password_ver.place(x=370, y=340)

button_save = tk.Button(page1, text="יצירת חשבון", bg="#1877F2", fg="white", width=10, height=1, font=("Arial", 16),
                        command=lambda: test_info(input_userName, input_password, input_password_ver))
button_save.pack()
button_save.place(x=250, y=400)

delete_button = tk.Button(page1, text="מחיקת תוכן", font=("Arial", 10), command=lambda: clear_input(input_userName,
                                                                                                    input_password, input_password_ver))
delete_button.pack()
delete_button.place(x=40, y=20)



# תוכן של עמוד 2
button2 = tk.Button(page2, text="חזור",width=10, command=lambda: show_frame(home_page))
button2.pack()
button2.place(x=480, y=20)

label5 = tk.Label(page2, text="הכנס את פרטי החשבון להתחברות", font=("Arial", 24))
label5.place(x=100, y=100)

label6 = tk.Label(page2, text="הכנס שם משתמש", font=("Arial", 10))
label6.place(x=430, y=170)
input_user_Name = tk.Entry(page2, width=30)
input_user_Name.place(x=340, y=200)

label7 = tk.Label(page2, text="הכנס סיסמא", font=("Arial", 10))
label7.place(x=460, y=230)
input_user_password = tk.Entry(page2, width=30)
input_user_password.place(x=340, y=260)

butoon_conect = tk.Button(page2, text="התחברות", bg="#1877F2", fg="white",  width=10, height=1, font=("Arial", 16),
                          command=lambda: login_details(input_user_Name, input_user_password))
butoon_conect.pack()
butoon_conect.place(x=250, y=400)


# להציג עמוד כברירת מחדל
show_frame(home_page)

# הרצת הלולאה הראשית
root.mainloop()
