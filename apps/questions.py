from apps.scale import Theory

thorax0 = ' '.join(Theory.thorax.get('0'))
thorax1 = ' '.join(Theory.thorax.get('1'))
thorax2 = ' '.join(Theory.thorax.get('2'))
question1 = (f'Оценка движения грудной клетки\n'
             f'Что из этого?\n'
             f'{thorax0}\n{thorax1}\n{thorax2}\n')

riber0 = ' '.join(Theory.riber.get('0'))
riber1 = ' '.join(Theory.riber.get('1'))
riber2 = ' '.join(Theory.riber.get('2'))
question2 = (f'Оценка втяжения межреберных\n'
             f'Что из этого?\n'
             f'{riber0}\n{riber1}\n{riber2}\n')


xiphoid0 = ' '.join(Theory.xiphoid.get('0'))
xiphoid1 = ' '.join(Theory.xiphoid.get('1'))
xiphoid2 = ' '.join(Theory.xiphoid.get('2'))
question3 = (f'Оценка втяжение мечевидного отростка\n'
             f'Что из этого?\n'
             f'{xiphoid0}\n{xiphoid1}\n{xiphoid2}\n')

mandibula0 = ' '.join(Theory.mandibula.get('0'))
mandibula1 = ' '.join(Theory.mandibula.get('1'))
mandibula2 = ' '.join(Theory.mandibula.get('2'))
question4 = (f'Оценка положения нижней челюсти\n'
             f'Что из этого?\n'
             f'{mandibula0}\n{mandibula1}\n{mandibula2}\n')

breath0 = ' '.join(Theory.breath.get('0'))
breath1 = ' '.join(Theory.breath.get('1'))
breath2 = ' '.join(Theory.breath.get('2'))

question5 = (f'Оценка звучности дыхания\n'
             f'Что из этого?\n'
             f'{breath0}\n{breath1}\n{breath2}\n')