#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import brainfuck

test_code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
test_result = 'Hello World!\n'


class TestParser(unittest.TestCase):
    def setUp(self):
        self.bf = brainfuck.BFParser()

    def test_increment_data_ptr(self):
        self.assertEqual(len(self.bf.data), 1)
        self.bf.parse('>')
        self.assertEqual(len(self.bf.data), 2)

    def test_decrement_data_ptr(self):
        self.bf.data = [1,2,3,4]
        self.bf.data_ptr = 3
        self.assertEqual(self.bf.data[self.bf.data_ptr], 4)
        self.bf.parse('<')
        self.assertEqual(self.bf.data_ptr, 2)
        self.assertEqual(self.bf.data[self.bf.data_ptr], 3)

    def test_increment_data_value(self):
        self.bf.parse('+')
        self.assertEqual(self.bf.data[0], 1)
        
    def test_decrement_data_value(self):
        self.bf.parse('-')
        self.assertEqual(self.bf.data[0], -1)

    def test_output_data(self):
        self.bf.parse('.')
        self.assertEqual(self.bf.result, '\0')

    def test_loop(self):
        self.bf.parse('+++++[>+<-]')
        self.assertEqual(self.bf.data, [0,5])

    def test_hello(self):
        self.bf.parse(test_code)
        self.assertEqual(self.bf.result, test_result)

if __name__ == '__main__':
    unittest.main()

