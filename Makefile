cv.pdf: gen.py tex_templates/* cv_data
	./$< | pdflatex -jobname="cv"
