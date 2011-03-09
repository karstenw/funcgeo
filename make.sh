#!/bin/sh

python funcgeo.py > funcgeo.ps && ps2pdf funcgeo.ps && open funcgeo.pdf
python squarelimitdemo1.py > squarelimitdemo1.ps && ps2pdf squarelimitdemo1.ps && open squarelimitdemo1.pdf
python squarelimitdemo2.py > squarelimitdemo2.ps && ps2pdf squarelimitdemo2.ps && open squarelimitdemo2.pdf
