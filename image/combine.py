import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

audio = mpimg.imread('audio.jpg')
piano_roll = mpimg.imread('piano-roll.jpg')
score = mpimg.imread('score.jpg')

audio = audio[:, 400:800,:]
piano_roll = piano_roll[10:628:2,:1000:2,:]
score = score[200:1745:5,:2100:3,:]

mask_audio = np.ones(audio.shape)
mask_audio[:,300:,:] = [[1-(i/100)]*3 for i in range(100)]
audio = np.multiply(audio,mask_audio).astype(int)

mask_piano_roll = np.ones(piano_roll.shape)
mask_piano_roll[:,:100,:] = [[i/100]*3 for i in range(100)]
mask_piano_roll[:,400:,:] = [[1-(i/100)]*3 for i in range(100)]
piano_roll = np.multiply(piano_roll, mask_piano_roll).astype(int)

mask_score = np.ones(score.shape)
mask_score[:,:100,:] = [[i/100]*3 for i in range(100)]
score = np.multiply(score, mask_score).astype(int)

picture = np.zeros((309, 1400, 4), dtype=int)
picture[:,:400,:3] += audio
picture[:,300:800,:3] += piano_roll
picture[:,700:,:3] += score

picture[:,:,3] = 255
transparent_mask = np.ones((309, 1400))
transparent_mask[:30,:] = np.array([[i/30]*1400 for i in range(30)])
transparent_mask[-30:,:] = np.array([[1-i/30]*1400 for i in range(30)])
picture[:,:,3] = np.multiply(picture[:,:,3], transparent_mask).astype(int)

print(audio.shape)
print(piano_roll.shape)
print(score.shape)

plt.imsave('picture.png', picture.astype(np.uint8))

plt.figure()
plt.imshow(picture)
plt.show()