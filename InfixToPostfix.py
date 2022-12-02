import re

from Stack import Stack


class Convert:

    __operators = {'$': 5, '*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}
    __new_expression = ""
    __removed_elements = []

    def __init__(self):
        self.logs = []

    def __log(self, stack, newExpression, message):
        self.logs.append(
            ["Stack: ['"+"','".join(stack)+"']", newExpression, message])

    def getLogs(self):
        return self.logs

    def convert(self, expression):

        stack = Stack()

        # if expression is empty
        if not expression:
            return "Expression is empty"

        # checks for illegal symbol
        if re.search("[^a-zA-Z0-9+/*\-$()]", expression):
            return "Only a-z A-Z 0-9 * + \ - $ ( ) Are Allowed"

        for element in expression:

            # if operand
            if re.search("[a-zA-Z0-9]", element):

                self.__new_expression += element
                self.__log(stack.getStack(), self.__new_expression,
                           "print('" + element + "')")

            # if '('
            if element == '(':
                stack.push(element)
                self.__log(stack.getStack(), self.__new_expression,
                           "push('" + element + "')")

            # if ')'
            if element == ')':

                self.__log(stack.getStack(), self.__new_expression,
                           "found ')' poping")

                self.__log(stack.getStack(), self.__new_expression,
                           "until next '('")

                while stack.seek() != '(':

                    popped_element = stack.pop()

                    self.__new_expression += popped_element

                    self.__log(stack.getStack(), self.__new_expression,
                               "pop('" + popped_element + "') and print")

                self.__removed_elements.clear()

                stack.pop()
                self.__log(stack.getStack(), self.__new_expression, "pop('(')")

            # if operator
            if element in '+-/*$':
                while (stack.getStack() and self.__operators[element] <= self.__operators[stack.seek()]):
                    popped_element = stack.pop()

                    if popped_element != '(':
                        self.__removed_elements.append(popped_element)

                    self.__new_expression += popped_element

                    self.__log(stack.getStack(), self.__new_expression,
                               "print('" + popped_element + "')")

                stack.push(element)
                self.__log(stack.getStack(), self.__new_expression,
                           "push('" + element + "')")

        # if stack is not empty
        if stack.getStack():

            self.__log(stack.getStack(), self.__new_expression,
                       "popping and printing")

            self.__log(stack.getStack(), self.__new_expression,
                       "remaining elements")

        # while stack is not empty
        while stack.getStack():

            if stack.seek() == '(':
                stack.pop()
            else:
                popped_element = stack.pop()
                self.__new_expression += popped_element
                self.__log(stack.getStack(), self.__new_expression,
                           "pop('" + popped_element + "') and print")

        self.__log(stack.getStack(), self.__new_expression, "Conversion Done")

        return self.__new_expression
