import utils.image as image
from scipy.misc import imsave

text = open('test/alice_wonderland.txt', 'r').read()
hide = image.hide_in_image(text, 'test/PolarLight.jpg', display=True)
imsave('test/alice.png', hide)
text_res = image.from_image_to_text('test/alice.png')
print(text_res)