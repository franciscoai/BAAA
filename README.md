Scripts to assist in the editorial work of the CRAAA and BAAA

--To download: 
	
	git clone https://github.com/franciscoai/BAAA.git

--Usage: 

	python3 checkCRAAA.py test_CRAAA.tex

--Required Packages (with Anaconda):

	conda install -c conda-forge termcolor

	conda install -c conda-forge pypdf2

	conda install -c conda-forge pandas

	conda install -c conda-forge pylatexenc

--IMPROVEMENTS (TODO):

	Check for final punctuation and capital letters in title

	Allow for two separated words in authors last names

	Avoid error when only one keyword is present (no separator)

	Keyword check with special characters(e.g. Hertzsprung–Russell and C–M diagrams)

	Better suggestion for affiliation and keywords (more cleaver word search). E.g. it does not suggest "Departamento de F\'isica, Facultad de Ciencias Exactas y Naturales, UBA, Argentina" when "Departamento de F\'isica, FCEyN--UBA, Argentina" is found. )
