from apps.test import _all_


class Result:
    def get_result(self):
        if 1 <= sum(_all_) < 3:
            result = (f'Ваши ответы {_all_}\n'
                  f'Cумма баллов {sum(_all_)}\n'
                  f'Начальные признаки синдрома дыхательных растройств')
            _all_.clear()
            return result

        elif 3 <= sum(_all_) <= 6:
            result = (f'Ваши ответы {_all_}\n'
                  f'Cумма баллов {sum(_all_)}\n'
                  f'Средняя степень тяжести синдрома дыхательных расстройств')
            _all_.clear()
            return result

        elif 7 <= sum(_all_):
            result = (f'Ваши ответы {_all_}\n'
                      f'Cумма баллов {sum(_all_)}\n'
                      f'Тяжелый синдром дыхательных расстройств')
            _all_.clear()
            return result

        else:
            result = (f'Ваши ответы {_all_}\n'
                      f'Cумма баллов {sum(_all_)}\n'
                      f'Признаков дыхательных расстройств нет')
            _all_.clear()
            return result
