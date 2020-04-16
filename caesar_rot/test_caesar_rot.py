import unittest
from ceaser_rot import rot_encrypt


class test_rot_encrypt(unittest.TestCase):

    def setUp(self):
        self.max_test_key = 100
        self.test_phrases = [
            'Genius without education is like silver in the mine',
            'Гений без образования, как серебро в шахте',
            'qwerty@booble.nerd'
            ]
        self.test_incorrect_cls_types = [int, float, bool, list]

    def test_encrypt_decrypt(self):
        for i in range(self.max_test_key + 1):
            for phrase in self.test_phrases:
                print('Testing => ', phrase, 'with key', i, end='')
                encrypt = rot_encrypt(phrase, i)
                decrypt = rot_encrypt(encrypt, i * -1)
                self.assertEqual(phrase, decrypt)
                print(' => Done')

    def test_input_type(self):
        with self.assertRaises(TypeError):
            for type_cls in self.test_incorrect_cls_types:
                rot_encrypt(type_cls(14))


if __name__ == "__main__":
    unittest.main()
