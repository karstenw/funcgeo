## Functional Geometry ##

Original idea by Peter Henderson, see

http://www.ecs.soton.ac.uk/~ph/funcgeo.pdf
http://www.ecs.soton.ac.uk/~ph/papers/funcgeo2.pdf
http://www.brics.dk/~hosc/local/HOSC-15-4-pp349-365.pdf


Implemented in Lisp by Frank Buß, see
http://www.frank-buss.de/lisp/functional.html

Ported to Python and Haskell by Will McCutchen <mccutchen@gmail.com>


Run the squarelimit demos like this:

### create postscript ###
    python funcgeo.py > funcgeo.ps
    python squarelimitdemo1.py > squarelimitdemo1.ps
    python squarelimitdemo2.py > squarelimitdemo2.ps

### make a PDF from the generated postscript ###
    ps2pdf funcgeo.ps
    ps2pdf squarelimitdemo1.ps
    ps2pdf squarelimitdemo2.ps

or point your favorite postscript viewer to the .ps files.
