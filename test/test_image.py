import utils.image as image
from scipy.misc import imsave
import unittest

class Image(unittest.TestCase):
    
    def test_from_text_to_image(self):
        img = image.from_text_to_image("patate", shape=(5,5))
        self.assertListEqual(list(img.shape), [5,5])
        img = image.from_text_to_image("patate", shape=(1,1))
        self.assertListEqual(list(img.shape), [1,1])

    def test_hide_in_image(self):
        text = 'test 123'
        hide = image.hide_in_image(text, 'test/PolarLight.jpg')
        imsave('test/test.png', hide)
        text_res = image.from_image_to_text('test/test.png')
        self.assertEqual(text.upper(), text_res)

if __name__ == '__main__':
    unittest.main()