from funcgeo import *

from fishmodel import fish


# the start symbol
start = ('u','c','b','r')


# all the substitutions needed for expanding the squarelimit quarters

shrinking_sq_rules = {
    #
    # these are the rules for the expanding squarelimit
    #
    # the idea is to construct a quarter of the picture which will be cycled() for
    # the final picture.
    #
    #
    # ucbr is the start symbol; will be expanded once
    #
    # u = up (upper left)
    # u -> e,e,u1,u2
    # u1 = up lower left expansion
    # u2 = up lower right expansion
    #
    # c = corner (upper right)
    # c -> e,e,c1,e
    # c1 = corner lower left expansion
    #
    # b1 = base (lower left)
    # base gets never expanded
    #
    # r = right (lower right)
    # r -> r1,e,r2,e
    # r1 = right upper right expansion
    # r2 = right lower right expansion
    #
    # e = empty
    
    # 3 parts get expanded, 1 stays constant
    start: ( ('e','e','u1','u2'),
             ('e','e','c1','e'),
              'b1',
             ('r1','e','r2','e') ),

    ('e','e','u1','u2'): ( ('e','e','u1','u2'),
                           ('e','e','u1','u2'),
                           'u1',
                           'u2' ),
    ('r1','e','r2','e'): ( 'r1',
                          ('r1','e','r2','e'),
                           'r2',
                          ('r1','e','r2','e') ),
    ('e','e','c1','e'): ( ('e','e','u1','u2'),
                         ('e','e','c1','e'),
                          'c1',
                         ('r1','e','r2','e')),
}

growing_sq_rules = {

    # 1 part gets expanded, 3 stay constant
    start: ('u1',
            'b1',
           ('u1', 'b1', 'e', 'u1'),
            'u1'),

    ('u1','b1','e','u1'): ('u1',
                           'b1',
                          ('u1', 'b1', 'e', 'u1'),
                           'u1'),
}


def makeparts_shrinking_squarelimit( basepict ):
    """Make the squarelimit parts; lots of vars packed up in a dict."""

    picture = basepict
    
    # two pictures filling a triangle
    pictriangle = over( flip( rot45(picture)),
                    flip( rot( rot45(picture))))

    b = over(picture, pictriangle)
    u1 = rot(b)
    u2 = b
    u = quartet(e,e,u1,u2)
    c1 = over(pictriangle, rot(rot(pictriangle)))
    c = quartet(e,e,c1,e)
    r1 = b
    r2 = rot(rot(rot(b)))
    r = quartet(r1,e,r2,e)
    result = {
        'e': blank(),
        'b': b,
        'b1': b,
        'u': u,
        'u1': u1,
        'u2': u2,
        'c': c,
        'c1': c1,
        'r': r,
        'r1': r1,
        'r2': r2
    }
    return result


def makeparts_growing_squarelimit( basepict ):
    """Make the squarelimit parts; lots of vars packed up in a dict."""

    picture = basepict
    
    # two pictures filling a triangle
    pictriangle = over( flip( rot45(picture)),
                    flip( rot( rot45(picture))))

    result = {
        'e': blank(),

        'b': rot(over(picture, rot(rot(picture)))),
        'b1': rot(over(picture, rot(rot(picture)))),

        'u': rot(rot(over(picture, pictriangle))),
        'u1': rot(rot(over(picture, pictriangle)))
    }
    
    return result


def substitute( item, rules ):
    """Run one symbol (char or tuple) through expansion for one level."""
    if item in rules:
        return rules[item]
    else:
        if type(item) in (list, tuple):
            result = []
            for i in item:
                result.append( substitute(i, rules) )
            return tuple( result )
        else:
            return item


def makelayout( start, level, rules ):
    """Expand all symbols."""
    symbols = start[:]
    while True:
        symbols = substitute(symbols, rules)
        level -= 1
        if level < 1:
            break
    return symbols


def makecalls( s, translator ):
    """Translate symbols to quartet calls"""
    args = []

    # convert strings to calls
    for i in s:
        if type(i) in (tuple, list):
            args.append( makecalls(i, translator) )
        elif type(i) in (str,):
            args.append( translator[i] )
        else:
            print "Should not happen."
            pdb.set_trace()
            print s
            print i
            print args
            
    if len(args) != 4:
        pdb.set_trace()
    result = []
    # a final clean up (because it's not clean...
    for i in args:
        try:
            item = result.append( translator[i] )
        except KeyError, err:
            item = i
        result.append(i)

    r = ()
    # debugging remnant
    try:
        r = quartet( *result )
    except TypeError, err:
        pdb.set_trace()
        print err
        print result
    return r


if __name__ == '__main__':

    # alternate picture
    triangle = grid( 2, 2,
                 polygon( ((0, 0), (2, 0), (0, 2)) ))

    e = blank()

    weirdtriangle = over(triangle, nonet( e,e,e,
                                          triangle,triangle,e,
                                          e,e,e))

    # variation of this theme
    weirdtriangle2 = over(triangle, nonet( e,e,e,
                                          triangle,triangle,e,
                                          triangle,e,triangle,))

    plot(triangle)
    plot(weirdtriangle)
    plot(weirdtriangle2)
    plot(fish)

    # make lots of squarelimit pictures
    layout_shrinking = layout_growing = start
    
    for i in range(2):
        # 2 layouts
        layout_shrinking = makelayout( layout_shrinking, i, shrinking_sq_rules)
        layout_growing = makelayout( layout_growing, i, growing_sq_rules)
    
        # 4 pictures * 2 layouts
        # fish
        fish_shrinking = makeparts_shrinking_squarelimit( fish )
        fish_growing = makeparts_growing_squarelimit( fish )

        # 
        triangle_shrinking = makeparts_shrinking_squarelimit( triangle )
        triangle_growing = makeparts_growing_squarelimit( triangle )

        # funny looking accidentally discovered
        weirdtriangle_shrinking = makeparts_shrinking_squarelimit( weirdtriangle )
        weirdtriangle_growing = makeparts_growing_squarelimit( weirdtriangle )

        # a variation of the previous
        weirdtriangle2_shrinking = makeparts_shrinking_squarelimit( weirdtriangle2 )
        weirdtriangle2_growing = makeparts_growing_squarelimit( weirdtriangle2 )


        # 4 quarters each in a shrinking and a growing style
        fishquarters_s = makecalls(layout_shrinking, fish_shrinking)
        fishquarters_g = makecalls(layout_growing, fish_growing)

        triquarters_s = makecalls(layout_shrinking, triangle_shrinking)
        triquarters_g = makecalls(layout_growing, triangle_growing)

        weirdquarters_s = makecalls(layout_shrinking, weirdtriangle_shrinking)
        weirdquarters_g = makecalls(layout_growing, weirdtriangle_growing)

        weirdquarters2_s = makecalls(layout_shrinking, weirdtriangle2_shrinking)
        weirdquarters2_g = makecalls(layout_growing, weirdtriangle2_growing)
    
        # triangle quarters
        plot(triquarters_s, title="triangle quarter shrinking " + str(i))
        plot(triquarters_g, title="triangle quarter growing " + str(i))
    
        # draw the weird triangle quarter
        plot(weirdquarters_s, title="3 triangles quarter shrinking " + str(i))
        plot(weirdquarters_g, title="3 triangles quarter growing " + str(i))

        plot(weirdquarters2_s, title="5 triangles quarter shrinking " + str(i))
        plot(weirdquarters2_g, title="5 triangles quarter growing " + str(i))
    
        # draw the fish quarter
        plot(fishquarters_s, title="shrinking fish quarter " + str(i))
        plot(fishquarters_g, title="growing fish quarter " + str(i))
    
        # draw triangle squarelimit
        plot( cycle(rot(triquarters_s)), title="shrinking triangle squarelimit level "+str(i))
        plot( cycle(rot(triquarters_g)), title="growing triangle squarelimit level "+str(i))
    
        # draw weird triangle squarelimit
        plot( cycle(rot(weirdquarters_s)), title="shrinking 3 triangles squarelimit level "+str(i))
        plot( cycle(rot(weirdquarters_g)), title="growing 3 triangles squarelimit level "+str(i))
    
        # draw weird triangle squarelimit
        plot( cycle(rot(weirdquarters2_s)), title="shrinking 5 triangles squarelimit level "+str(i))
        plot( cycle(rot(weirdquarters2_g)), title="growing 5 triangles squarelimit level "+str(i))
    
        # draw fish squarelimit
        plot( cycle(rot(fishquarters_s)), title="shrinking fish squarelimit level "+str(i))
        plot( cycle(rot(fishquarters_g)), title="growing fish squarelimit level "+str(i))
