from funcgeo import *

import pprint
pp = pprint.pprint
import pdb

__all__ = ( 'fish')
# fish parts 

# outline
fish1 = grid(
            80, 80,
            polygon( ((  0, 0), ( 20, 20), ( 30, 16), ( 38, 12), ( 44,  4),
                      ( 50, 4), ( 60,  4), ( 72,  2), ( 80,  0), ( 75,  3),
                      ( 68, 8), ( 63, 13), ( 60, 16), ( 53, 15), ( 46, 17),
                      ( 40,20), ( 32, 32), ( 40, 40), ( 40, 60), ( 33, 63),
                      ( 27,65), ( 20, 64), ( 17, 67), ( 12, 72), (  5, 77),
                      (  0,80), ( -2, 72), ( -4, 60), ( -4, 50), ( -4, 44),
                      (-12,38), (-16, 30), (-20, 20), (  0,  0) )))

# outer eye
fish2 = grid( 80, 80,
              polygon(( (0,64), (0,54), (4,58), (0,64)) ) )

# inner eye
fish3 = grid( 80, 80,
              polygon( ( (8,68), (8,58), (12,60), (8,68)) ))

# fin line
fish4 = grid( 80, 80,
              polygon( ( (8,54), (16,42), (28,26), (40,16), (58,10)), False ))

# outer fin
fish5 = grid( 80, 80,
              polygon( ( (-4,44), (6,28), (20,20) ), False ))

# fin line 1
fish6 = grid( 80, 80,
              polygon( ( (-2,36), (-8,30), (-12,22) ), False ))

# fin line 2
fish7 = grid( 80, 80,
              polygon( ( (2,30), (-6,22), (-8,16) ), False ))

# fin line 3
fish8 = grid( 80, 80,
              polygon( ( (8,24), (-2,16), (-4,10) ), False ))

# fin line 4
fish9 = grid( 80, 80,
              polygon( ( (10,18), (2,10), (0,6)), False ))

# inner fin
fish10 = grid( 80, 80,
               polygon( ( (20,64), (24,56), (26,44), (32,32) ), False ))

# fin line 1
fish11 = grid( 80, 80,
               polygon( ((26,56), (30,58), (34,58), (40,54)),
                        False ))

# fin line 2
fish12 = grid( 80, 80,
               polygon( ((28,50), (32,52), (36,52), (40,50)),
                        False ))

# fin line 3
fish13 = grid( 80, 80,
               polygon( ( (30,42), (34,46), (40,46) ), False ))

# shadow line 1
fish14 = grid( 80, 80,
               polygon( ( (38,36), (40,34) ), False ))

# shadow line 2
fish15 = grid( 80, 80,
               polygon( ( (38,32), (40,30) ), False ))

# shadow line 3
fish16 = grid( 80, 80,
               polygon( ( (36,30), (40,26) ), False ))

# put the pieces together
fish = over( fish1,
        over( fish2,
         over( fish3,
          over( fish4,
           over( fish5,
            over( fish6,
             over( fish7,
              over( fish8,
               over( fish9,
                over( fish10,
                 over( fish11,
                  over( fish12,
                   over( fish13,
                    over( fish14,
                     over( fish15,
                           fish16)))))))))))))))
