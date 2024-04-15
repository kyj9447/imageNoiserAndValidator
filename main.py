from imageSigner import signImage
from imageValidator import validateImage

# main

choice = input("작업을 선택하세요\n1. Sign Image\n2. Validate Image\n")

if choice == "1":

    image = "original.png"
    string = input("주입할 문자열을 입력하세요: ")

    if string == "":
        print("입력이 없습니다. 기본값으로 설정합니다. (!Validation:kyj9447@mailmail.com)")
        string = "!Validation:kyj9447@mailmail.com"

    signImage(image, string+"\n") # string 끝에 줄바꿈 추가
    print("문자열 주입이 완료되었습니다.\nsigned_"+image)

elif choice == "2":
    validation = validateImage("signed_original.png")
    print(validation)
else:
    print("잘못된 입력입니다.")