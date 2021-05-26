"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class StackPlates:
    def __init__(self, volume):
        self.plate_list = [[]]
        self.max_of_plates = volume
        self.stack_count = 0

    def stack_size(self):
        return len(self.plate_list)

    def push_in(self, count):
        if len(self.plate_list[self.stack_count]) == self.max_of_plates:
            self.plate_list.append([])
            self.stack_count += 1
        self.plate_list[self.stack_count].append(count)

    def pop_out(self):
        if not self.stack_size():
            plate = self.plate_list[self.stack_count].pop()
            if not self.stack_size() and not len(self.plate_list[self.stack_count]):
                self.plate_list.pop()
                self.stack_count -= 1
            return plate
        else:
            return 'В стопках нет тарелок'

    def all_stack_size(self):
        return self.plate_list


if __name__ == '__main__':

    stack = StackPlates(5)

    for i in range(1, 23):
        stack.push_in(i)
        print(stack.all_stack_size())

