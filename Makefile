cv.pdf: data tex_src
	./gen.py | pdflatex -jobname="cv"
