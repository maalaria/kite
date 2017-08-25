import copy

### GENERATE KEYLIST.STY FROM MAIN.TEX

with open('lit_research.tex', 'r') as cc:
	content = cc.readlines()

content = [x.strip() for x in content] 

keywords = []
for ii in range(len(content)):
	if content[ii].find('printlist') != -1:
    		keywords.append(content[ii][11:-1])

keywords.sort()

head_ = '\usepackage{luacode,luatexbase}\n\\newcommand{\kiteref}{\\noexpand\hyperref}\n\n%% Lua-side code\n\\begin{luacode}\nfunction ktrf ( buff )\n'
foot_ = 'return buff\nend\n\\end{luacode}\n\n%% TeX-side code\n\\newcommand\ktrfOn{\directlua{luatexbase.add_to_callback ( "process_input_buffer" , ktrf , "ktrf" )}}\n\\newcommand\ktrfOff{\directlua{luatexbase.remove_from_callback ( "process_input_buffer" , "ktrf" )}}\n\AtBeginDocument{\ktrfOn} % turn Lua function on by default'

with open('keylist.sty','wb') as f:
	f.write( head_ )

	for kk_ in keywords:
    		f.write('\tbuff = string.gsub ( buff, "' + kk_.lower() + '", "\\\kiteref[' + kk_ + ']{' + kk_ + '}" )\n')

	f.write( foot_ )


#### GENERATE DOCUMETN WITH KEYLIST FROM ORIGIN
## TODO: read all files from section that contain kite environment and process


with open('./sections/neuroN.tex', 'r') as f:
    content = f.readlines()
    
content = [x.strip() for x in content] 
content_ = copy.deepcopy(content)

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

    if content[ii].find('end{kite}') != -1:
        content_.insert(ii+inserted_, '\par\kiteKey{[' + to_[13:-1].lower() + ']}' )   
        inserted_ = inserted_ + 1
        
with open('./sections/neuroNPY.tex', 'w') as fw:
    for item in content_:
        fw.write("%s\n" % item)
