class Stationary:
    title = 'Picture'

    def draw(self):
        print('Stationary')


class Pen(Stationary):

    def draw(self):
        print('Middle')


class Pencil(Stationary):

    def draw(self):
        print('Thin')


class Handle(Stationary):

    def draw(self):
        print('Tall')


Stationary().draw()
Pen().draw()
Pencil().draw()
Handle().draw()
