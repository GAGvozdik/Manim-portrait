from manim import *

class dater(Scene):

    def construct(self):

        # функция создающая врещение Mobject вокруг точки 0,0,0
        def updater_forth(mobj, dt):
            mobj.rotate(dt, about_point=[0, 0, 0])

        # функция создающая врещение Mobject вокруг точки, являющейся концом arrow
        def upd(mobj, dt):
            mobj.rotate(dt, about_point=arrow.get_end())

        # создаю два вектора
        arrow = Arrow([0, 0, 0], [1, 1, 0], buff=0)
        arrow_1 = Arrow([1, 1, 0], [2, 2, 0], buff=0)

        # добавляю круговое вращение первому вектору вокруг 0,0,0
        arrow.add_updater(updater_forth)
        # добавляю круговое вращение второму вектору вокруг 0,0,0
        arrow_1.add_updater(updater_forth)
        # добавляю круговое вращение, уже вращающемуся второму вектору вокруг конца первой стрелки
        arrow_1.add_updater(upd)

        # создаю сетку
        numberplane = NumberPlane()

        # создаю трассировку конца второй стрелки
        trace = TracedPath(arrow_1.get_end)

        # добавляю сетку, два вектора и линию трассировки
        self.add(numberplane, arrow, arrow_1, trace)

        # задаю время работы видео
        self.wait(20)
