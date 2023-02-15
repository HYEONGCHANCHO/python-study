#외부 모듈 읽어오기
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pilimg

#이미지 파일 불러오기
im1=pilimg.open(r'C:\Users\a11\Downloads\jeju_summer.jpg')
im2=pilimg.open(r'C:\Users\a11\Downloads\baby1.jpg')
im3=pilimg.open(r'C:\Users\a11\Downloads\baby2.jpg')

pix1=np.array(im1)
print(pix1)

#사진의 사이즈 변경
resizeX2=pix1.shape[1]/2 #홀수인지 체크해서 

if(pix1.shape[1]%2>0):
    resizeX1= pix1.shape[1]/2+1
else :
    resizeX1=pix1.shape[1]/2

im2=im2.resize((int(resizeX1),int(pix1.shape[0])))
pix2=np.array(im2)

im3=im3.resize((int(resizeX2),int(pix1.shape[0])))
pix3=np.array(im3)

pix4=np.concatenate((pix2,pix3),axis=1)

pix1=(1/255)*pix1
pix4=(1/255)*pix4
weight=0.3

pix5=(pix1*weight)+(pix4*(1-weight))
pix6=(pix1*(1-weight))+(pix4*weight)

#배경이미지 출력
plt.subplot(141)
plt.imshow(pix1)
plt.axis("off")
plt.title("background")
#아기사진1출력
plt.subplot(142)
plt.imshow(pix4)
plt.axis("off")
plt.title("picture of baby")
#아기사진70%합성
plt.subplot(143)
plt.imshow(pix5)
plt.axis("off")
plt.title("70% blended")
#아기사진30%합성
plt.subplot(144)
plt.imshow(pix6)
plt.axis("off")
plt.title("30% blended")

plt.show()
#subplot()함수를 사용하여 한 그림에 여러 개의 그림을 그릴 수 있습니다.
#numpy 배열은 각 인덱스가 대응하는 요소의 수를 갖는 튜플을 반환하는 shape라는 속성을 갖는다
