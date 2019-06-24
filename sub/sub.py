from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.layers import Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from numpy import expand_dims, argmax

imgW, imgH = 266, 263
kernel, downscale = 3, 2
path = 'C:\\Users\\lucas\\Downloads\\facul\\PI\\sub\\dataset'

trainImgs = ImageDataGenerator()
testImgs = ImageDataGenerator()

trainI = trainImgs.flow_from_directory(path + '/impossible/train', target_size = (imgW, imgH),batch_size = 16, class_mode = 'categorical')
testI = testImgs.flow_from_directory(path + '/impossible/test', target_size = (imgW, imgH),batch_size = 16, class_mode = 'categorical')
trainP = trainImgs.flow_from_directory(path + '/possible/train', target_size = (imgW, imgH),batch_size = 16, class_mode = 'categorical')
testP = testImgs.flow_from_directory(path + '/possible/test', target_size = (imgW, imgH), batch_size = 16, class_mode = 'categorical')

classesI = list(trainI.class_indices.keys())
classesP = list(trainP.class_indices.keys())

cnn = Sequential()

cnn.add(Conv2D(32, kernel, input_shape = (imgW, imgH, 3),activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (downscale, downscale)))
cnn.add(Conv2D(64, kernel, activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (downscale, downscale)))
cnn.add(Flatten())

cnn.add(Dense(units = 128, activation = 'relu'))
cnn.add(Dense(units = len(classesI), activation = 'softmax'))
cnn.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])

cnn.fit_generator(trainI, steps_per_epoch = 512, epochs = 1, validation_data = testI, validation_steps = 512)

cnn.save('cnn-tictactoe.h5')

cnn = load_model('cnn-tictactoe.h5')

for i in range(0, 12):
    file = path + '/unknown' + str(i+1) + '.png'
    img = image.load_img(file, target_size = (imgW, imgH))
    y = cnn.predict(expand_dims(image.img_to_array(img), axis = 0))
    print('Jogo:', file, ':', classes[argmax(y)])
