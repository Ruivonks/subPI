import cv2 
import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR

y=1

possible1 = cv2.imread('dataset/possible/unknown1.png')
possible2 = cv2.imread('dataset/possible/unknown2.png')
possible3 = cv2.imread('dataset/possible/unknown3.png')
possible4 = cv2.imread('dataset/possible/unknown4.png')
possible5 = cv2.imread('dataset/possible/unknown5.png')
possible6 = cv2.imread('dataset/possible/unknown6.png')
possible7 = cv2.imread('dataset/possible/unknown7.png')
possible8 = cv2.imread('dataset/possible/unknown8.png')
possible9 = cv2.imread('dataset/possible/unknown9.png')
possible10 = cv2.imread('dataset/possible/unknown10.png')
#possible11 = cv2.imread('dataset/possible/unknown11.png')
#possible12 = cv2.imread('dataset/possible/unknown12.png')
#possible13 = cv2.imread('dataset/possible/unknown13.png')
#possible14 = cv2.imread('dataset/possible/unknown14.png')
#possible15 = cv2.imread('dataset/possible/unknown15.png')
#possible16 = cv2.imread('dataset/possible/unknown16.png')
#possible17 = cv2.imread('dataset/possible/unknown17.png')
#possible18 = cv2.imread('dataset/possible/unknown18.png')
#possible19 = cv2.imread('dataset/possible/unknown19.png')
#possible20 = cv2.imread('dataset/possible/unknown20.png')

impossible1 = cv2.imread('dataset/impossible/unknown1.png')
impossible2 = cv2.imread('dataset/impossible/unknown2.png')
impossible3 = cv2.imread('dataset/impossible/unknown3.png')
impossible4 = cv2.imread('dataset/impossible/unknown4.png')
impossible5 = cv2.imread('dataset/impossible/unknown5.png')
impossible6 = cv2.imread('dataset/impossible/unknown6.png')
impossible7 = cv2.imread('dataset/impossible/unknown7.png')
impossible8 = cv2.imread('dataset/impossible/unknown8.png')
impossible9 = cv2.imread('dataset/impossible/unknown9.png')
impossible10 = cv2.imread('dataset/impossible/unknown10.png')
#impossible11 = cv2.imread('dataset/impossible/unknown11.png')
#impossible12 = cv2.imread('dataset/impossible/unknown12.png')
#impossible13 = cv2.imread('dataset/impossible/unknown13.png')
#impossible14 = cv2.imread('dataset/impossible/unknown14.png')
#impossible15 = cv2.imread('dataset/impossible/unknown15.png')
#impossible16 = cv2.imread('dataset/impossible/unknown16.png')
#impossible17 = cv2.imread('dataset/impossible/unknown17.png')
#impossible18 = cv2.imread('dataset/impossible/unknown18.png')
#impossible19 = cv2.imread('dataset/impossible/unknown19.png')
#impossible20 = cv2.imread('dataset/impossible/unknown20.png')

#cenarios = np.concatenate((
#possible1,possible2,possible3,possible4,possible5,possible6,possible7,possible8,possible9,possible10,
#possible11,possible12,possible13,possible14,possible15,possible16,possible17,possible18,possible19,possible20,
#impossible1,impossible2,impossible3,impossible4,impossible5,impossible6,impossible7,impossible8,impossible9,impossible10,
#impossible11,impossible12,impossible13,impossible14,impossible15,impossible16,impossible17,impossible18,impossible19,impossible20)
#    ), axis=0)
cenarios = np.concatenate((possible1,possible2,possible3,possible4,possible5,possible6,possible7,possible8,possible9,possible10,
impossible1,impossible2,impossible3,impossible4,impossible5,impossible6,impossible7,impossible8,impossible9,impossible10), axis=0)

enum = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
#enum = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40])

linear = SVC(kernel='linear')
linear.fit(cenarios,enum)

for x in cenarios : 
	chicoxavier = linear.predict(x)
	accuracy = linear.score(cenarios,enum)
	
	if chicoxavier == 1:
		resultado = possible1
	elif chicoxavier == 2:
		resultado = possible2
	elif chicoxavier == 3:
		resultado = possible3
	elif chicoxavier == 4:
		resultado = possible4
	elif chicoxavier == 5:
		resultado = possible5
	elif chicoxavier == 6:
		resultado = possible6
	elif chicoxavier == 7:
		resultado = possible7
	elif chicoxavier == 8:
		resultado = possible8
	elif chicoxavier == 9:
		resultado = possible9
	elif chicoxavier == 10:
		resultado = possible10
	#elif chicoxavier == 11:
	#	resultado = possible11
	#elif chicoxavier == 12:
	#	resultado = possible12
	#elif chicoxavier == 13:
	#	resultado = possible13
	#elif chicoxavier == 14:
	#	resultado = possible14
	#elif chicoxavier == 15:
	#	resultado = possible15
	#elif chicoxavier == 16:
	#	resultado = possible16
	#elif chicoxavier == 17:
	#	resultado = possible17
	#elif chicoxavier == 18:
	#	resultado = possible18
	#elif chicoxavier == 19:
	#	resultado = possible19
	#elif chicoxavier == 20:
	#	resultado = possible20
	elif chicoxavier == 11:
		resultado = impossible1
	elif chicoxavier == 12:
		resultado = impossible2
	elif chicoxavier == 13:
		resultado = impossible3
	elif chicoxavier == 14:
		resultado = impossible4
	elif chicoxavier == 15:
		resultado = impossible5
	elif chicoxavier == 16:
		resultado = impossible6
	elif chicoxavier == 17:
		resultado = impossible7
	elif chicoxavier == 18:
		resultado = impossible8
	elif chicoxavier == 19:
		resultado = impossible9
	elif chicoxavier == 20:
		resultado = impossible10        
    #elif chicoxavier == 31:
	#	resultado = impossible11
	#elif chicoxavier == 32:
	#	resultado = impossible12
	#elif chicoxavier == 33:
	#	resultado = impossible13
	#elif chicoxavier == 34:
	#	resultado = impossible14
	#elif chicoxavier == 35:
	#	resultado = impossible15
	#elif chicoxavier == 36:
	#	resultado = impossible16
	#elif chicoxavier == 37:
	#	resultado = impossible17
	#elif chicoxavier == 38:
	#	resultado = impossible18
	#elif chicoxavier == 39:
	#	resultado = impossible19
	#elif chicoxavier == 40:
	#	resultado = impossible10

	if chicoxavier <= 10 :
		print('Cenário possível')
		cv2.imshow("O cenário "+ str(y) + " é possivel", resultado)

	elif chicoxavier > 10 :
		print('Cenário impossível')
		cv2.imshow("O cenário "+ str(y) + " é impossível", resultado)
	
    y+=1

cv2.waitKey(0)