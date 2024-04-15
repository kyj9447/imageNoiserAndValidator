## imageSigner
#### signImage("이미지 경로/이름", "주입할 문자열") => 문자열이 주입된 Image return

이미지파일의 RGB값(0~255) 중 중간값(127)에서 가장 먼 색상의 값의 홀,짝을 주입할 문자열의 binary값(0,1)에 맞춤

=> 육안으로 인식이 어려운 수준의 노이즈로 문자열을 이미지에 주입함

## imageValidator
#### validateImage("이미지 경로/이름") => 이미지에 주입된 문자열을 return
이미지파일의 RGB값(0~255) 중 중간값(127)에서 가장 먼 색상의 값의 홀,짝을 문자열의 binary로 인식

=> imageSigner로 주입한 문자열을 추출가능

## example
### 원본 (문자열 주입 전)
<img src="https://github.com/kyj9447/imageNoiserAndValidator/blob/main/original.png" width=600px>

### 주입 후 (문자열 "!Validation:kyj9447@mailmail.com\n" 주입됨)
<img src="https://github.com/kyj9447/imageNoiserAndValidator/blob/main/signed_original.png" width=600px>

### Validation 결과
<img src="https://github.com/kyj9447/imageNoiserAndValidator/assets/122734245/d6eaba0b-c76b-4229-9dbd-6dc5f0b23995" width=600px>

## etc
추후 (클라이언트)공개키 암호화 -> (서버)개인키 복호화 등의 방법으로 이미지 원본 검증 등 기능 구현 예정

