import numpy as np
from scipy import misc
from utils.morse import encrypt, decrypt
import matplotlib.pyplot as plt

encode_image_dict = {'-': '1110',
                     '.': '10',
                     ' ': '00'}

def from_text_to_image(text, shape = None, display = False):
    """
        Show the encoding of the morse
        in an image where each pixel is a time point
        
        Arguments:
            text {str} -- Text to translate

        Returns:
            array -- Binary image representing the text
    """
    encoded = []
    for symbol in encrypt(text):
        encoded.append(encode_image_dict[symbol])
    encoded = ''.join(encoded)

    image = np.array([int(e) for e in encoded])
    
    if shape is not None:
        pad = np.zeros(np.prod(shape))
        lim = min(len(pad), len(image))
        pad[:lim] = image[:lim]
        image = pad.reshape(shape)

    if display:
        plt.imshow(image)
        plt.axis('off')
        plt.show()

    return image

def from_image_to_text(image_path, autocorrection = False):
    """
        Translates the last bit of images into text
        
        Arguments:
            image_path {str} -- Image to translate

        Returns:
            text -- BText found
    """
    # TODO: Viterbi correction in order to handle errors in morse
    img = misc.imread(image_path)

    morse_layer = img % 2
    if len(img.shape) == 3:
        morse_layer = morse_layer[:,:,-1]

    morse_layer = ''.join([str(m) for m in morse_layer.flatten()])

    # Replace all known code
    morse_layer = morse_layer.replace(encode_image_dict['-'], '-')
    morse_layer = morse_layer.replace(encode_image_dict['.'], '.')
    morse_layer = morse_layer.replace(encode_image_dict[' '], ' ')

    # Remove all other
    morse_layer = [symbol for symbol in morse_layer if symbol in encode_image_dict]

    return decrypt(''.join(morse_layer)).strip()

def hide_in_image(text, image_path, display = False):
    """
        Changes the last pixels of the image to hide 
        the given text
    
        Arguments:
            text {str} -- Text to hide
            image_path {str} -- Image in which to hide the text

        Returs:
            image -- Image with translated text
    """
    img = misc.imread(image_path)
    shape = img.shape

    morse_layer = img % 2
    if len(img.shape) == 3:
        shape = img.shape[:2]
        morse_layer = morse_layer[:,:,-1]

    morse_to_add = from_text_to_image(text, shape = shape)
    morse_to_add = np.abs(morse_layer - morse_to_add).astype(np.uint8)

    if len(img.shape) == 3:
        img[:,:,-1] -= morse_to_add
    else:
        img -= morse_to_add
    img = np.abs(img)

    if display:
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    
    return img