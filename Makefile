cv.pdf: tex_src cv_data
	./gen.py | pdflatex -jobname="cv"
