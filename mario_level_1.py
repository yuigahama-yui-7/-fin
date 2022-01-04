#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
这里尝试重写马里奥的第一关
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()