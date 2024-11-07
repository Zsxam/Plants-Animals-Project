def register_teacher():
    pass
def login_teacher():
    pass
def create_class():
    pass
def self_mode():
    pass
def class_mode():
    pass

def main():
    print("Selamat datang di Plants & Animals!")
    print("1. Registrasi Guru")
    print("2. Login Guru")
    print("3. Mode Mandiri")
    print("4. Mode Kelas")

    choice = input("Pilih opsi (1-4): ")
    if choice == "1":
        register_teacher()
    elif choice == "2":
        teacher_email = login_teacher()
        if teacher_email:
            print("1. Buat Kelas")
            sub_choice = input("Pilih opsi (1): ")
            if sub_choice == "1":
                create_class(teacher_email)
    elif choice == "3":
        self_mode()
    elif choice == "4":
        class_mode()
    else:
        print("Pilihan tidak valid.")

main()