# student_manager.py
def add_student(name, year_of_birth, address):
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for s in student_list:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")


def search_student(search_name):
    print("--- KET QUA TIM KIEM ---")
    found = False
    for s in student_list:
        if search_name.lower() in s['name'].lower():
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
            found = True
    if not found:
        print("Khong tim thay sinh vien nao.")
