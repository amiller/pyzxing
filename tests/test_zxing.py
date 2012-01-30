import pyzxing
import unittest
import Image


data = [
    ('qr-code-business-card-39-500x375.jpg', 'MECARD:N:Stephanie Obodda;TEL:4014020444;URL:http://wwww.stephanieobodda.com;EMAIL:sobodda@gmail.com;;'),
    ('qr-code-times-square.jpg', 'HTTP://SCN.BY/9T9AB0HTW8GN97'),
    ('facebook_like_QR-594x445.jpg', 'http://www.facebook.com/tailormadehotel'),
    ('QRCodeCoaster500.jpg', 'http://qr2.it/Go/71946'),
    ('Marlboro_QR_code.JPG.scaled500.jpg', 'HTTP://SCN.BY/9T9AB0HTW8HQCA'),
    ('qr-code.jpg', 'http://theory.isthereason.com'),
]


class TestZxing(unittest.TestCase):
    def test_samples(self):
        for filename, expected in data:
            img = Image.open('tests/samples/' + filename)
            self.assertEqual(expected, pyzxing.decode_image(img))

if __name__ == '__main__':
    unittest.main()
