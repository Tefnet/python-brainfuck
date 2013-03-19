#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BFParser(object):
    def __init__(self, code=None):
        self.data = [0,]
        self.data_ptr = 0
        self.result = ""
        
        if code:
            self.parse(code)

    def parse(self, code):
        self.code = code
        self.pos = 0
        self.loops = []
        self.code_len = len(code)
        while self.pos < self.code_len:
            instruction = self.code[self.pos]
            if instruction == '[':
                self.loops.append(self.pos)

            elif instruction == ']':
                if self.data[self.data_ptr] > 0:
                    self.pos = self.loops[-1]
                else:
                    self.loops.pop()

            elif instruction == '>':
                self.data_ptr += 1
                if len(self.data) == self.data_ptr:
                    self.data.append(0)

            elif instruction == '<':
                self.data_ptr -= 1 if self.data_ptr > 0 else 0

            elif instruction == '+':
                self.data[self.data_ptr] = self.data[self.data_ptr] + 1 if self.data[self.data_ptr] < 255 else 0

            elif instruction == '-':
                self.data[self.data_ptr] = self.data[self.data_ptr] - 1 if self.data[self.data_ptr] > 0 else 255

            elif instruction == '.':
                self.result += chr(self.data[self.data_ptr])

            self.pos += 1

