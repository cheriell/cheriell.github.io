import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def generate_background_picture_desktop():

    audio = mpimg.imread('audio.jpg')
    piano_roll = mpimg.imread('piano-roll.jpg')
    score = mpimg.imread('score.jpg')

    print(audio.shape, piano_roll.shape, score.shape)

    audio = audio[:, 400:800,:]
    audio_resize = np.zeros((audio.shape[0] * 2, audio.shape[1], audio.shape[2]))
    audio_resize[::2, :, :] = audio
    audio_resize[1::2, :, :] = audio
    audio = audio_resize
    piano_roll = piano_roll[10:628,:1000:2,:]
    score = score[200:1436:2,:2100:3,:]

    print(audio.shape, piano_roll.shape, score.shape)

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

    picture = np.zeros((audio.shape[0], 1400, 4), dtype=int)
    picture[:,:400,:3] += audio
    picture[:,300:800,:3] += piano_roll
    picture[:,700:,:3] += score

    picture[:,:,3] = 255
    transparent_mask = np.ones((audio.shape[0], 1400))
    transparent_mask[:30,:] = np.array([[i/30]*1400 for i in range(30)])
    transparent_mask[-30:,:] = np.array([[1-i/30]*1400 for i in range(30)])
    picture[:,:,3] = np.multiply(picture[:,:,3], transparent_mask).astype(int)

    plt.imsave('background-desktop.png', picture.astype(np.uint8))

def generate_background_picture_mobile():

    audio = mpimg.imread('audio.jpg')
    piano_roll = mpimg.imread('piano-roll.jpg')
    score = mpimg.imread('score.jpg')

    audio = audio[:,0:1116,:]
    piano_roll = piano_roll[:,0:1116,:]
    score = score[:,0:1116,:]

    audio_resize = np.zeros((audio.shape[0] * 2, audio.shape[1], audio.shape[2]))
    audio_resize[::2, :, :] = audio
    audio_resize[1::2, :, :] = audio
    audio = audio_resize
    score = score[::2, :, :]

    mask_audio = np.ones(audio.shape)
    mask_audio[audio.shape[0]-100:,:,:] = np.expand_dims(np.array([[1-(i/100)]*3 for i in range(100)]), axis=1)
    audio = np.multiply(audio,mask_audio).astype(int)

    mask_piano_roll = np.ones(piano_roll.shape)
    mask_piano_roll[:100,:,:] = np.expand_dims(np.array([[i/100]*3 for i in range(100)]), axis=1)
    mask_piano_roll[piano_roll.shape[0]-100:,:,:] = np.expand_dims(np.array([[1-(i/100)]*3 for i in range(100)]), axis=1)
    piano_roll = np.multiply(piano_roll, mask_piano_roll).astype(int)

    mask_score = np.ones(score.shape)
    mask_score[:100,:,:] = np.expand_dims(np.array([[i/100]*3 for i in range(100)]), axis=1)
    score = np.multiply(score, mask_score).astype(int)

    picture = np.zeros((audio.shape[0] + piano_roll.shape[0] + score.shape[0] - 200, audio.shape[1], 4), dtype=int)
    picture[:audio.shape[0],:,:3] += audio
    picture[audio.shape[0]-100:audio.shape[0] + piano_roll.shape[0] - 100,:,:3] += piano_roll
    picture[audio.shape[0] + piano_roll.shape[0] - 200:,:,:3] += score

    picture[:,:,3] = 255
    transparent_mask = np.ones((picture.shape[0], picture.shape[1]))
    transparent_mask[:30,:] = np.array([[i/30]*picture.shape[1] for i in range(30)])
    transparent_mask[-30:,:] = np.array([[1-i/30]*picture.shape[1] for i in range(30)])
    picture[:,:,3] = np.multiply(picture[:,:,3], transparent_mask).astype(int)

    plt.imsave('background-mobile.png', picture.astype(np.uint8))


generate_background_picture_desktop()
generate_background_picture_mobile()