from PIL import Image

class binaryProvider:

    # 생성자
    def __init__(self, hiddenString):
        self.hiddenbinary = self.str_to_binary(hiddenString)
        self.hiddenbinaryIndex = 0
        self.hiddenbinaryIndexMax = len(self.hiddenbinary)

    # String -> Binary[]
    def str_to_binary(self,string):
        # 빈 리스트 생성
        binarys = []
        
        # String 내 각 char에 대한 반복
        for char in string:
            # 각 char를 8비트로 변환하여 리스트에 추가
            binarys.append(bin(ord(char))[2:].zfill(8))
            
        # 리스트를 하나의 문자열로 결합
        return ''.join(binarys)

    # 다음 비트를 가져오는 함수
    def next_bit(self):
        # hiddenBinary의 인덱스가 최대값에 도달하면 0으로 초기화
        if self.hiddenbinaryIndex >= self.hiddenbinaryIndexMax:
            self.hiddenbinaryIndex = 0

        # hiddenBinary의 해당 인덱스의 비트를 가져옴
        bit = self.hiddenbinary[self.hiddenbinaryIndex]

        # hiddenBinary의 인덱스 증가
        self.hiddenbinaryIndex += 1

        return int(bit)

def add_hidden_bit(image_path, hiddenBinary):
    # 이미지 열기
    img = Image.open(image_path)

    # 이미지의 너비와 높이 가져오기
    width, height = img.size

    # 이미지의 각 픽셀에 접근하여 1비트 추가
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

            # 가장 먼 색상의 실제 값 읽기
            if max_diff == diff_r: 
                targetColorValue = r
            elif max_diff == diff_g:
                targetColorValue = g
            else:
                targetColorValue = b 
            
            # 가장 먼 색상이 127이상이면 감소방향, 127 미만이면 증가방향
            add_direction = 1 if targetColorValue < 127 else -1

            # 해당 index의 hiddenBinary값
            bit = hiddenBinary.next_bit()
            #print(bit)

            # 해당 픽셀의 RGB 값을 수정
            # next_bit()으로 가져온 비트가 0이면 해당 색상을 짝수로, 1이면 홀수로 만들어줌
            if max_diff == diff_r:
                # 실제 색상 값의 짝수, 홀수여부가 next_bit()의 값과 다르면
                if r % 2 != bit:
                    # 색상값을 증가 또는 감소시켜 next_bit()와 일치시킴
                    r += add_direction
            if max_diff == diff_g:
                if g % 2 != bit:
                    g += add_direction
            if max_diff == diff_b:
                if b % 2 != bit:
                    b += add_direction

            # 이미지의 해당 픽셀에 수정된 RGB 값을 설정
            img.putpixel((x,y), (r, g, b))

    # 수정된 이미지를 return
    return img

# main
# 이미지 경로 + 주입할 String => String 주입된 Image
def signImage(image_path, hiddenString) :
    hiddenBinary = binaryProvider(hiddenString)
    add_hidden_bit(image_path, hiddenBinary).save("signed_" + image_path)
