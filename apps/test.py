from apps.scale import Theory

_all_ = []


class First_sym:
    @staticmethod
    def thorax_symptoms(the_sum: str):
        global _all_
        thorax0 = ' '.join(Theory.thorax.get('0'))
        thorax1 = ' '.join(Theory.thorax.get('1'))
        thorax2 = ' '.join(Theory.thorax.get('2'))
        while True:
            try:
                if int(the_sum) in range(0, 3):
                    if (the_sum in thorax0 or the_sum in thorax1 or the_sum in thorax2):
                        _all_.append(int(the_sum))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")


class Second_sym:
    @staticmethod
    def riber_symptoms(the_sum: str):
        global _all_
        riber0 = ' '.join(Theory.riber.get('0'))
        riber1 = ' '.join(Theory.riber.get('1'))
        riber2 = ' '.join(Theory.riber.get('2'))
        while True:
            try:
                if int(the_sum) in range(0, 3):
                    if (the_sum in riber0 or the_sum in riber1 or the_sum in riber2):
                        _all_.append(int(the_sum))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")


class Third_sym:
    @staticmethod
    def xiphoid_symptoms(the_sum: str):
        global _all_
        xiphoid0 = ' '.join(Theory.xiphoid.get('0'))
        xiphoid1 = ' '.join(Theory.xiphoid.get('1'))
        xiphoid2 = ' '.join(Theory.xiphoid.get('2'))
        while True:
            try:
                if int(the_sum) in range(0, 3):
                    if (the_sum in xiphoid0 or the_sum in xiphoid1 or the_sum in xiphoid2):
                        _all_.append(int(the_sum))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")


class Fourth_sym:
    @staticmethod
    def mandibula_symptoms(the_sum: str):
        global _all_
        mandibula0 = ' '.join(Theory.mandibula.get('0'))
        mandibula1 = ' '.join(Theory.mandibula.get('1'))
        mandibula2 = ' '.join(Theory.mandibula.get('2'))
        while True:
            try:
                if int(the_sum) in range(0, 3):
                    if (the_sum in mandibula0 or the_sum in mandibula1 or the_sum in mandibula2):
                        _all_.append(int(the_sum))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")


class Fith_sym:
    @staticmethod
    def breath_symptoms(the_sum: str):
        global _all_
        breath0 = ' '.join(Theory.breath.get('0'))
        breath1 = ' '.join(Theory.breath.get('1'))
        breath2 = ' '.join(Theory.breath.get('2'))
        while True:
            try:
                if int(the_sum) in range(0, 3):
                    if (the_sum in breath0 or the_sum in breath1 or the_sum in breath2):
                        _all_.append(int(the_sum))
                        return _all_
            except ValueError:
                print('Простите, но мы используем только числа!')
                continue
            else:
                print("Неправильно введено число!")
