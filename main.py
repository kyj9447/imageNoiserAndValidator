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

    signedImage = signImage(image, string+"\n") # string 끝에 줄바꿈 추가
    signedImage.save("signed_"+image)
    print("signed_"+image+ " 파일이 작성되었습니다.")

elif choice == "2":

    image = "signed_original.png"

    validation = validateImage(image)
    with open("validation_result.txt", "w") as file:
        file.write(validation)
    print("validation_result.txt 파일이 작성되었습니다.")
    # print(validation)
    
else:
    print("잘못된 입력입니다.")