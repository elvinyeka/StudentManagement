student_code_list = []
student_name_list = []
student_surname_list = []
student_email_list = []
student_phone_list = []

def start():
    xususiEmr = int(input("""
    Aşağıdakı Əmrlerden Birinin sıra nomrəsini daxil edin :
    1.Yeni tələbə əlavə edilməsi
    2.Tələbə koduna görə tələbə məlumatlarının silinməsi
    3.Tələbə koduna görə tələbə məlumatlarının dəyişdirilməsi
    4.Tələbə adina gore telebe melumatinin gosterilmesi
    5.Bütün tələbə melumatlarının gösterilməsi
    """))
    if xususiEmr == 1:
        TelebeElaveEt()
        print(f"{student_name_list} adli telebe elave olundu")
        start()
    elif xususiEmr == 2:
        KodaGoreMelumatSil()
        start()
    elif xususiEmr == 3:
        KodaGoreMelumatDeyisdir()
        start()
    elif xususiEmr == 4:
        KodaGoreMelumatDeyisdir()
        start()
    elif xususiEmr == 5:
        ButunTelebeMelumatlari()
        start()
    else:
        print("Duzgun daxil edin!")


def TelebeElaveEt():
    telebe_sayi = int(input("Ne qeder telebe melumati daxil edeceksiniz?:"))

    m = 1

    while m <= telebe_sayi:

        student_code = int(input("Telebe kodunu daxil edin:"))

        student_name = input("Telebenin adi:")

        student_surname = input("Telebenin soyadi:")

        student_email = input("Telebenin email adresi:")

        student_phone = input("Telebenin nomresi:")
        m += 1

        if 2 < len(str(student_code)) < 4:
            student_code_list.append(student_code)
        else:
            student_code = int(input("Zehmet olmasa 3 reqemli telebe kodu daxil edin:"))
            student_code_list.append(student_code)

        ## Data append to list ##

        student_name_list.append(student_name)
        student_surname_list.append(student_surname)
        student_email_list.append(student_email)
        student_phone_list.append(student_phone)



def TelebeAdinaGoreAxtar():
    search_student_name = input("Melumatlari axtarilan telebe adini daxil edin:")

    for s in student_name_list:
        if s == search_student_name:
            name_index = student_name_list.index(s)
            print("{}-adli telebenin, telebe kodu {}, soyadi {}, email unvani {}, telefon nomresi {}".format(
                search_student_name, student_code_list[name_index],
                student_surname_list[name_index], student_email_list[name_index],
                student_phone_list[name_index]))


def KodaGoreMelumatDeyisdir():
    input_student_code = int(input("Telebe kodunu daxil edin:"))
    print("""Telebenin hansi melumatini deyisdirmek isteyirsinizse onu asagidaki kimi daxil edin:
kodunu deyisdirmek isteyirsinizse =>kod,adini deyisdirmek isteyirsinizse => ad, soyadini deyisdirmek isteyirsinizse => soyad, emailini deyisdirmek isteyirsinizse =>email,
telefon nomresini deyisdirmek isteyirsinizse => telefon --kimi qeyd edin!""")
    sayi = int(input("Ne qeder melumati deyisdirmek isteyirsinizse sayini qeyd edin:"))

    m = 1
    while m <= sayi:
        change = input("Deyisdirmek istediyiniz melumatin yuxarida gosterilen formada acar sozunu daxil edin:")
        change = change.lower()

        replace_data = input("ne ile deyisdirmek isteyirsiz?:")

        m += 1

        for s in student_code_list:
            if s == input_student_code:
                index_code = student_code_list.index(s)

                if change == "kod":
                    student_code_list.remove(student_code_list[index_code])
                    student_code_list.insert(index_code, int(replace_data))

                if change == "ad":
                    student_name_list.remove(student_name_list[index_code])
                    student_name_list.insert(index_code, replace_data)

                if change == "soyad":
                    student_surname_list.remove(student_surname_list[index_code])
                    student_surname_list.insert(index_code, replace_data)

                if change == "email":
                    student_email_list.remove(student_email_list[index_code])
                    student_email_list.insert(index_code, replace_data)

                if change == "telefon":
                    student_phone_list.remove(student_phone_list[index_code])
                    student_phone_list.insert(index_code, replace_data)


def KodaGoreMelumatSil():
    input_student_code = int(input("Tələbə kodunu daxil edin:"))

    for s in student_code_list:
        if s == input_student_code:
            index_code = student_code_list.index(s)

            student_code_list.remove(student_code_list[index_code])
            student_name_list.remove(student_name_list[index_code])
            student_surname_list.remove(student_surname_list[index_code])
            student_email_list.remove(student_email_list[index_code])
            student_phone_list.remove(student_phone_list[index_code])


def ButunTelebeMelumatlari():
    for s in student_name_list:
        info_index = student_name_list.index(s)
        print("Kodu: {}  Adı: {}  Soyadı: {}  Email: {}  Telefon: {}".format(student_code_list[info_index],
                                                                             student_name_list[info_index],
                                                                             student_surname_list[info_index],
                                                                             student_email_list[info_index],
                                                                             student_phone_list[info_index]))






start()



