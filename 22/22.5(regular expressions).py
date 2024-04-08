#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

pattern = r'\s*([А-Яа-яЁё]+)(\d+)\s*'
string = r'---   Опять45   ---'
match = re.search(pattern, string)
print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
print(f'Группа букв >{match[1]}< с позиции {match.start(1)} до {match.end(1)}')
print(f'Группа цифр >{match[2]}< с позиции {match.start(2)} до {match.end(2)}', flush=True)
###
# -> Найдена подстрока >   Опять45   < с позиции 3 до 16
# -> Группа букв >Опять< с позиции 6 до 11
# -> Группа цифр >45< с позиции 11 до 13

import sys
print(sys.stdout.encoding)
