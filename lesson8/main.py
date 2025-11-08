from database.db_manager import DataBaseManager
from utils.menu import Menu

def main():
    db = DataBaseManager()

    while True:
        choice = Menu.show_menu()

        if choice == "1":
            f = input("Name: ")
            l = input("Firts Name")
            a = int(input("Age: "))
            sid = input("ID Student: ")
            db.add_student(f, l, a, sid)

        elif choice == "2":
            for s in db.list_student():
                print(s)

        elif choice == "3":
            sid = int(input("ID student: "))
            cid = int(input("ID Courses: "))
            g = float(input("Grades: "))
            db.add_grade(sid, cid, g)
            print("OK")

        elif choice == "0":
            for row in db.get_average_by_course():
                print(f"{row[0]} - {row[1]:2f}")

        elif choice == "0":
            print("Exit")
            break

        else:
            print("Error")

main()