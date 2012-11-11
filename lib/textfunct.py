# -*- coding: utf-8 -*-
import md5

md5x2 = lambda x, salt='': md5.md5(md5.md5(x + salt).hexdigest()).hexdigest()
