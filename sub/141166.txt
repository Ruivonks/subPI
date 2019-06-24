import cv2 
import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR

valido01_new = cv2.imread('Validos/JogoDaVelha.png')
valido02_new = cv2.imread('Validos/JogoDaVelha02.png')
valido03_new = cv2.imread('Validos/JogoDaVelha04.png')
valido04_new = cv2.imread('Validos/JogoDaVelha07.png')
valido05_new = cv2.imread('Validos/JogoDaVelha09.png')
valido06_new = cv2.imread('Validos/JogoDaVelha15.png')
valido07_new = cv2.imread('Validos/JogoDaVelha16.png')
valido08_new = cv2.imread('Validos/JogoDaVelha17.png')
valido09_new = cv2.imread('Validos/JogoDaVelha18.png')
valido10_new = cv2.imread('Validos/JogoDaVelha19.png')

invalido01_new = cv2.imread('Invalidos/JogoDaVelha01.png')
invalido02_new = cv2.imread('Invalidos/JogoDaVelha03.png')
invalido03_new = cv2.imread('Invalidos/JogoDaVelha05.png')
invalido04_new = cv2.imread('Invalidos/JogoDaVelha06.png')
invalido05_new = cv2.imread('Invalidos/JogoDaVelha08.png')
invalido06_new = cv2.imread('Invalidos/JogoDaVelha10.png')
invalido07_new = cv2.imread('Invalidos/JogoDaVelha11.png')
invalido08_new = cv2.imread('Invalidos/JogoDaVelha12.png')
invalido09_new = cv2.imread('Invalidos/JogoDaVelha13.png')
invalido10_new = cv2.imread('Invalidos/JogoDaVelha14.png')

valido01 = cv2.resize(valido01_new, (10,10))
valido02 = cv2.resize(valido02_new, (10,10))
valido03 = cv2.resize(valido03_new, (10,10))
valido04 = cv2.resize(valido04_new, (10,10))
valido05 = cv2.resize(valido05_new, (10,10))
valido06 = cv2.resize(valido06_new, (10,10))
valido07 = cv2.resize(valido07_new, (10,10))
valido08 = cv2.resize(valido08_new, (10,10))
valido09 = cv2.resize(valido09_new, (10,10))
valido10 = cv2.resize(valido10_new, (10,10))

invalido01 = cv2.resize(invalido01_new, (10,10))
invalido02 = cv2.resize(invalido02_new, (10,10))
invalido03 = cv2.resize(invalido03_new, (10,10))
invalido04 = cv2.resize(invalido04_new, (10,10))
invalido05 = cv2.resize(invalido05_new, (10,10))
invalido06 = cv2.resize(invalido06_new, (10,10))
invalido07 = cv2.resize(invalido07_new, (10,10))
invalido08 = cv2.resize(invalido08_new, (10,10))
invalido09 = cv2.resize(invalido09_new, (10,10))
invalido10 = cv2.resize(invalido10_new, (10,10))

X = np.concatenate((valido01,valido02,valido03,valido04,valido05,valido06,valido07,valido08,valido09,valido10,
invalido01,invalido02,invalido03,invalido04,invalido05,invalido06,invalido07,invalido08,invalido09,invalido10 ), axis=0)

y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

y = np.array(y)

Y = y.reshape(-1)

X = X.reshape(len(y), -1)

classifier_linear = SVC(kernel='linear')

print(40 * '-')
print('Started train of SVC model')

classifier_linear.fit(X,Y)
print('Finished train')
print(40 * '-')

i  = 1;
for x in X : 
	prediction = classifier_linear.predict(x.reshape(1,-1))

	score = classifier_linear.score(X,Y)

	print('Result: {}'.format(prediction))
	print('Score of precision: {:.1f}%'.format(score * 100))

	if prediction == 1:
		result = valido01_new
	elif prediction == 2:
		result = valido02_new
	elif prediction == 3:
		result = valido03_new
	elif prediction == 4:
		result = valido04_new
	elif prediction == 5:
		result = valido05_new
	elif prediction == 6:
		result = valido06_new
	elif prediction == 7:
		result = valido07_new
	elif prediction == 8:
		result = valido08_new
	elif prediction == 9:
		result = valido09_new
	elif prediction == 10:
		result = valido10_new
	elif prediction == 11:
		result = invalido01_new
	elif prediction == 12:
		result = invalido02_new
	elif prediction == 13:
		result = invalido03_new
	elif prediction == 14:
		result = invalido04_new
	elif prediction == 15:
		result = invalido05_new
	elif prediction == 16:
		result = invalido06_new
	elif prediction == 17:
		result = invalido07_new
	elif prediction == 18:
		result = invalido08_new
	elif prediction == 19:
		result = invalido09_new
	elif prediction == 20:
		result = invalido10_new

	if prediction <= 10 :
		print('A Imagem é Valida!')
		cv2.imshow("A Imagem "+str(i) + " e Valida!", result)
		i+=1
	elif prediction > 10 :
		print('A Imagem é invalida!')
		cv2.imshow("A Imagem "+str(i) + " e Invalida!", result)
		i+=1

cv2.waitKey(0)