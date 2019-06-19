### REQUIRES PYTHON2

import copy
from subprocess import call
import sys
import numpy as np

### DESCRIPTON
# generates KEYLIST.STY from main tex document by reading \kiteXXX{} contents
#	these are used to insert keys as links into the section document XXX.tex specified in line 67
#	which is saved as .XXXPY.tex
#
# then the main.tex is compiled (use bib argument to compile the bibliography: python2 cmpl.py bib)
#
#
#
#
###


### VARIABLES
doc_name = 'main.tex'
sections = ['section1.tex'] # ['section1.tex', 'section2.tex',...]


### GENERATE KEYLIST.STY FROM MAIN.TEX
with open(doc_name, 'r') as cc:
	content = cc.readlines()

content = [x.strip() for x in content]

keywords = []
for ii in range(len(content)): # loop over rows of the document
	#if content[ii].find('printlist') != -1 :
    	#	keywords.append(content[ii][11:-1]) # append the words in \printlist environmentg
	if len(content[ii]) > 0: # skip comment rows and empty of the tex document
		if content[ii][0] is '%':
			continue
	else:
		continue
	if content[ii].find('kitesection') != -1:
		keywords.append(content[ii][13:-1])
	if content[ii].find('kitesubsection') != -1:
		keywords.append(content[ii][16:-1])
	if content[ii].find('kitesubsubsection') != -1:
		keywords.append(content[ii][19:-1])
	if content[ii].find('kiteparagraph') != -1:
		keywords.append(content[ii][15:-1])
	if content[ii].find('kitesubparagraph') != -1:
		keywords.append(content[ii][18:-1])


keywords.sort()
# keylist.tex for Appendix
kk_old = " " # init kk_old
with open('.keylist.tex','w') as f:
	for cntr, kk_ in enumerate(keywords):
		if kk_[0].upper() != kk_old[0].upper() or cntr == 0: # if current key starts with different letter than the last
			f.write( "\\textit{}\\\[0.2cm]\\textbf{" + kk_[0].upper() + "} \\\[0.1cm]\n" ) # make heading
		#
		f.write(kk_ + r" \ref{" + kk_ + "}" + r"\\" + "\n") # write key
		kk_old = copy.deepcopy(kk_)


keywords.sort(key=len, reverse=True) # necessary to deal with e.g. "Memory guided saccades" versus "Saccades"

head_ = '\\usepackage{luacode,luatexbase}\n\n%% Lua-side code\n\\begin{luacode}\nfunction ktrf ( buff )\n'
foot_ = 'return buff\nend\n\\end{luacode}\n\n%% TeX-side code\n\\newcommand\ktrfOn{\directlua{luatexbase.add_to_callback ( "process_input_buffer" , ktrf , "ktrf" )}}\n\\newcommand\ktrfOff{\directlua{luatexbase.remove_from_callback ( "process_input_buffer" , "ktrf" )}}\n\AtBeginDocument{\ktrfOn} % turn Lua function on by default'


# keylist.sty
with open('.keylist.sty','w') as f:
	f.write( head_ )
	for kk_ in keywords:
		f.write('\tbuff = string.gsub ( buff, "' + kk_.upper() + '", "\\\kiteref[' + kk_ + ']{' + kk_ + '}" )\n')
	#
	f.write( foot_ )


#### GENERATE (HIDDEN) DOCUMENT CONTAINING THE  HYPERLINKS (THIS ONE IS COMPILED BY LATEX, NOT THE ONE YOU WRITE)

for s_ in sections:

	#
	with open('./sections/'+s_, 'r') as f:
	    content = f.readlines()

	#
	content = [x.strip() for x in content]
	content_ = copy.deepcopy(content)

	### read the topics of KITE environment and save them in var to_
	inserted_ = 0

	#
	for ii in range(len(content)):
		cntr = 0
		print(ii)

		##
		if content[ii].find('begin{kite}') != -1:
			to_ = content[ii]

			###
			if content[ii][12:].find('}') == -1:
				cntr = 1
				to_ = to_ + ' ' + content[ii+cntr]

				####
				while content[ii+cntr].find('}') == -1:
					cntr = cntr+1
					to_ = to_ + ' ' + content[ii+cntr]

	    ## insert var to_ in var content
		if content[ii].find('end{kite}') != -1:
			content_.insert(ii+inserted_, '\par\kiteKey{[' + to_[13:-1].upper() + ']}' )   ######## lower -> upper
			inserted_ = inserted_ + 1

	# write modified var content to file
	#
	with open('./sections/.'+s_[:-4]+'PY.tex', 'w') as fw:
		##
		for item in content_:
			fw.write("%s\n" % item)


##### COMPILE LATEX
call(["lualatex", doc_name])
if len(sys.argv) > 1 and sys.argv[1] == 'bib':
	call(["biber", doc_name[:-4]+".bcf"])
	call(["lualatex", doc_name])
	print('Bib file processed')
call(["open", doc_name[:-4]+".pdf"])
