from funcgeo import *



if __name__ == '__main__':

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

    # triangle
    triangle = grid( 2, 2,
                     polygon( ((0, 0), (2, 0), (0, 2)) ))

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

    # parts
    empty = blank()

    # henderson hosc figures
    
    # figure 4
    fig4 = fish
    plot(fig4, title="Figure 4: fish")
    
    # figure 5
    fig5 = over(fish, rot(rot(fish)))
    plot( fig5, title="Figure 5")

    # figure 6
    fish2 = flip(rot45(fish))
    fish3 = rot(rot(rot(fish2)))
    t = over(fish, over(fish2, fish3))
    plot(t, title="Figure 6: t")

    # figure 7
    u = over(over(fish2, rot(fish2)),
             over(rot(rot(fish2)), rot(rot(rot(fish2)))))
    plot(u, title="Figure 7: u")

    # figure 8
    plot( quartet(u, u, u, u), title="Figure 8: quartet(u, u, u, u)")

    # figure 9
    v = cycle( rot(t) )
    plot(v, title="Figure 9, v")

    # figure 10
    plot( quartet(v, v, v, v), title="Figure 10: quartet(v, v, v, v)")

    # figure 11
    side1 = quartet( empty, empty, rot(t), t)
    plot( side1, title="Figure 11: side1")

    # figure 12
    side2 = quartet( side1, side1, rot(t), t)
    plot( side2, title="Figure 12: side2")

    # figure 13
    corner1 = quartet( empty, empty,
                       empty, u)
    plot( corner1, title="Figure 13: corner1")

    # figure 14
    corner2 = quartet( corner1,    side1,
                       rot(side1), u)
    plot( corner2, title="Figure 14: corner2")


    #
    squarelimit2 = nonet( corner2,      side2,           rot(rot(rot(corner2))),
                          rot(side2),   u,               rot(rot(rot(side2))),
                          rot(corner2), rot(rot(side2)), rot(rot(corner2)))
    plot( squarelimit2, title="Figure 15: squarelimit2")

    
    tri1 = triangle
    tri2 = flip(rot45(tri1))
    tri3 = rot(rot(rot(tri2)))
    
    t = over(tri1, over(tri2, tri3))
    u = over(over(tri2, rot(tri2)),
             over(rot(rot(tri2)), rot(rot(rot(tri2)))))
    v = cycle( rot(t) )
    side1 = quartet( empty, empty, rot(t), t)
    side2 = quartet( side1, side1, rot(t), t)
    corner1 = quartet( empty, empty,
                       empty, u)
    corner2 = quartet( corner1,    side1,
                       rot(side1), u)
    squarelimit2 = nonet( corner2,      side2,           rot(rot(rot(corner2))),
                          rot(side2),   u,               rot(rot(rot(side2))),
                          rot(corner2), rot(rot(side2)), rot(rot(corner2)))
    plot( squarelimit2, title="Figure 16: squarelimit2 triangle skeleton")
