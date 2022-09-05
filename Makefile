cv.pdf: tex_templates/* cv_data gen.py
	./gen.py | pdflatex -jobname="cv"
