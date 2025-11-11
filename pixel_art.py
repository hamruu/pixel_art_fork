def define_smile():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    black = [0, 0, 0]
    yellow = [1.0, 0.85, 0]
    pink = [1, 0.753, 0.796]
    grey = [0.15] * 3

    image_mat = np.ones((15, 15, 3)) * grey

    # specify which pixels are which colour
    image_mat[3:12, 3:12] = yellow
    image_mat[4:11, 2:13] = yellow
    image_mat[5:10, 1:14] = yellow
    
    image_mat[5:7, 5:7] = black  
    image_mat[5:7, 9:11] = black
    
    image_mat[9, 5:11] = black
    image_mat[10, 6:10] = black
    image_mat[11, 7:9] = black

    return image_mat
    
def define_butterfly():
    import numpy as np

    # make an empty numpy array for storing the image
    image_mat = np.full((16, 16, 3), 1.0)

    # define some colours
    black = [0, 0, 0]
    blue = [0.2, 0.4, 0.8]

    # specify which pixels are which colour
    c = 8
    # centre of butterfly
    image_mat[2:13, c] = black
    
    # generate mirror image at the same time
    for i in [-1, 1]:
        # outline
        image_mat[1, i*1+c] = black
        image_mat[0, i*2+c] = black
        image_mat[4, i*1+c] = black
        image_mat[3, [i*j+c for j in [2, 3]]] = black
        image_mat[2, [i*j+c for j in [4, 5]]] = black
        image_mat[3, i*6+c] = black
        image_mat[4:7, i*7+c] = black
        image_mat[7, [i*j+c for j in [6, 5]]] = black
        image_mat[8, [i*j+c for j in [4, 3, 2]]] = black
        image_mat[7, i*1+c] = black
        image_mat[9, i*5+c] = black
        image_mat[10:12, i*6+c] = black
        image_mat[12, i*5+c] = black
        image_mat[13, [i*j+c for j in [4, 3]]] = black
        image_mat[12, i*2+c] = black
        image_mat[11, i*1+c] = black
        
        # fill in the centre line by line
        image_mat[3, [i*j+c for j in [4, 5]]] = blue
        image_mat[4, [i*j+c for j in range(2,7)]] = blue
        image_mat[5:7, [i*j+c for j in range(1,7)]] = blue
        image_mat[7, [i*j+c for j in range(2,5)]] = blue
        image_mat[8, i*1+c] = blue
        image_mat[9, [i*j+c for j in range(1,5)]] = blue
        image_mat[10, [i*j+c for j in range(1,6)]] = blue
        image_mat[11, [i*j+c for j in range(2,6)]] = blue
        image_mat[12, [i*j+c for j in range(3,5)]] = blue
    
    return image_mat



def plot_image(image):
    import matplotlib.pyplot as plt

    plt.axis('off')
    plt.imshow(image)
    plt.show()


smile = define_smile()
plot_image(smile)
butterfly = define_butterfly()
plot_image(butterfly)
