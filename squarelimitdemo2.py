from funcgeo import *

from fishmodel import fish


# the start symbol
start = ('u','c','b','r')


# all the substitutions needed for expanding the squarelimit quarter
layoutexpansions = {
    # ucbr is start symbol; gets expanded once
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
    
    ('u','c','b','r'): ( ('e','e','u1','u2'),
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


def makeparts( basepict ):
    """Make the squarelimit parts; lots of vars packed up in a dict."""

    picture = basepict
    
    # two pictures filling a triangle
    pictriangle = over( flip( rot45(picture)),
                    flip( rot( rot45(picture))))

    # parts named here for mnemotic 
    e = blank()
    b = over(picture, pictriangle)
    b1 = b
    u1 = rot(b)
    u2 = b
    u = quartet(e,e,u1,u2)
    c1 = over(pictriangle, rot(rot(pictriangle)))
    c = quartet(e,e,c1,e)
    r1 = b
    r2 = rot(rot(rot(b)))
    r = quartet(r1,e,r2,e)
    return (e,b,b1,u1,u2,u,c1,c,r1,r2,r)


def maketranslator( picture ):
    e,b,b1,u1,u2,u,c1,c,r1,r2,r = makeparts( picture )
    callers = {
        'e': e,
        'b1': b1,
        'b': b,
        'u1': u1,
        'u2': u2,
        'c1': c1,
        'c': c,
        'r1': r1,
        'r2': r2,
        'r': r
    }
    return callers


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
                                          e,e,e,))

    # make several squarelimit pictures
    layout = start
    
    for i in range(3):
        # 1 layout
        layout = makelayout( layout, i, layoutexpansions)
    
        # 3 translators
        fishtranslator = maketranslator( fish )
        triangletranslator = maketranslator( triangle )
        weirdtriangletranslator = maketranslator( weirdtriangle )

        # 3 pictures
        fishquarters = makecalls(layout, fishtranslator)
        triquarters = makecalls(layout, triangletranslator)
        weirdquarters = makecalls(layout, weirdtriangletranslator)
    
        # draw the triangle quarter
        plot(triquarters, title="triangle quarter " + str(i))
    
        # draw the weird triangle quarter
        plot(weirdquarters, title="3 triangles quarter " + str(i))
    
        # draw the fish quarter
        plot(fishquarters, title="fish quarter " + str(i))
    
        # draw triangle squarelimit
        plot( cycle(rot(triquarters)), title="triangle squarelimit level "+str(i))
    
        # draw weird triangle squarelimit
        plot( cycle(rot(weirdquarters)), title="3 triangles squarelimit level "+str(i))
    
        # draw fish squarelimit
        plot( cycle(rot(fishquarters)), title="fish squarelimit level "+str(i))