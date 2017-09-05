import copy
from subprocess import call


### GENERATE KEYLIST.STY FROM MAIN.TEX

with open('main.tex', 'r') as cc:
	content = cc.readlines()

content = [x.strip() for x in content] 

keywords = []
for ii in range(len(content)):
	if content[ii].find('printlist') != -1:
    		keywords.append(content[ii][11:-1]) # append the words in \printlist environmentg

keywords.sort()
keywords.sort(key=len, reverse=True) # necessary to deal with e.g. "Memroy guided saccades" versus "Saccades"

head_ = '\usepackage{luacode,luatexbase}\n\n%% Lua-side code\n\\begin{luacode}\nfunction ktrf ( buff )\n'
foot_ = 'return buff\nend\n\\end{luacode}\n\n%% TeX-side code\n\\newcommand\ktrfOn{\directlua{luatexbase.add_to_callback ( "process_input_buffer" , ktrf , "ktrf" )}}\n\\newcommand\ktrfOff{\directlua{luatexbase.remove_from_callback ( "process_input_buffer" , "ktrf" )}}\n\AtBeginDocument{\ktrfOn} % turn Lua function on by default'

with open('keylist.sty','wb') as f:
	f.write( head_ )

	for kk_ in keywords:
    		f.write('\tbuff = string.gsub ( buff, "' + kk_.upper() + '", "\\\kiteref[' + kk_ + ']{' + kk_ + '}" )\n')

	f.write( foot_ )


#### GENERATE DOCUMENT WITH LINKS (THIS ONE IS COMPILED, NOT THE ONE YOU WRITE)
## TODO: read all files from section that contain kite environment and process

with open('./sections/section1.tex', 'r') as f:
    content = f.readlines()
    
content = [x.strip() for x in content] 
content_ = copy.deepcopy(content)

# read the topics of KITE environment and save them in var to_
inserted_ = 0
for ii in range(len(content)):
    cntr = 0
    if content[ii].find('begin{kite}') != -1:
        to_ = content[ii]
        if content[ii][12:].find('}') == -1: 
            cntr = 1
            to_ = to_ + ' ' + content[ii+cntr]
            while content[ii+cntr].find('}') == -1:
                cntr = cntr+1
                to_ = to_ + ' ' + content[ii+cntr]

    # insert var to_ in var content
    if content[ii].find('end{kite}') != -1:
        content_.insert(ii+inserted_, '\par\kiteKey{[' + to_[13:-1].upper() + ']}' )   ######## lower -> upper
        inserted_ = inserted_ + 1

# write modified var content to file
with open('./sections/section1PY.tex', 'w') as fw:
    for item in content_:
        fw.write("%s\n" % item)


##### COMPILE LATEX
call(["lualatex", "main.tex"])
#call(["biber", "lit_research.bcf"])
#call(["lualatex", "lit_research.tex"])
call(["evince", "main.pdf"])


