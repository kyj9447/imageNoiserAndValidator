from PIL import Image

def binary_to_string(binary_code):
    string = ""
    for i in range(0, len(binary_code), 8):
        byte = binary_code[i:i+8]
        decimal = int(byte, 2)
        character = chr(decimal)
        string += character
    return string

def read_hidden_bit(image_path):
    # 비트 저장용 문자열
    hiddenBinary = ""

    # 이미지 열기
    img = Image.open(image_path)

    # 이미지의 너비와 높이 가져오기
    width, height = img.size

    # 이미지의 각 픽셀에 접근하여 값 확인
    for y in range(height):
        for x in range(width):
            # 현재 픽셀의 RGB 값을 가져옴
            r, g, b = img.getpixel((x, y))

            # 127과의 차이 계산
            diff_r = abs(r - 127)
            diff_g = abs(g - 127)
            diff_b = abs(b - 127)

            # 가장 먼 색상 찾기
            max_diff = max(diff_r, diff_g, diff_b)

            # 가장 먼 색상의 값이 짝수면 hiddenBinary에 1 추가, 홀수면 0 추가
            if max_diff % 2 == 0:
                hiddenBinary += "1"
            else:
                hiddenBinary += "0"
    
    return hiddenBinary

def deduplicate(arr):
    deduplicated = []
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            deduplicated.append(arr[i])
    return deduplicated

# main
def validateImage(image_path):
    resultBinary = read_hidden_bit(image_path)
    resultString = binary_to_string(resultBinary)
    deduplicated = deduplicate(resultString.split("\n"))
    deduplicatedJoined = "\n".join(deduplicated)
    return deduplicatedJoined
