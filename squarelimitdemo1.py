from funcgeo import *

from fishmodel import fish

triangle = grid( 2, 2,
                 polygon( ((0, 0), (2, 0), (0, 2)) ))

letterF = grid( 8, 8,
                polygon( ( (2,1), (2,7), (6,7), (6,6), (3,6), (3,5), (5,5), (5,4), (3,4), (3,1) ) ))

pictureframe = grid( 2, 2,
                     polygon( ( (0.1,0.1), (1.9,0.1), (1.9,1.9), (0.1,1.9) ) ))

if __name__ == '__main__':

    # parts
    empty = blank()

    # henderson hosc figures
    # figure 1
    fig1 = letterF
    plot(fig1, title="Figure 1a: Letter F")
    plot(rot(fig1), title="Figure 1b: Letter F rot()")
    plot(flip(fig1), title="Figure 1c: Letter F flip()")
    plot(rot(flip(fig1)), title="Figure 1d: Letter F rot(flip())")

    # figure 2
    fig2 = letterF
    plot(above(fig2,fig2), title="Figure 2a: Letter F above()")
    plot(beside(fig2,fig2), title="Figure 2b: Letter F beside()")
    plot(above(beside(fig2,fig2), fig2), title="Figure 2c: Letter F above(beside())")

    fig2d = over(letterF, pictureframe)
    plot(rot45(fig2d), title="Figure 2d: Letter F rot45() with frame")
    

    
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
