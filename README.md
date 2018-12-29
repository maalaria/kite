# kite - Revolutionized note taking
A LaTeX package to optimize note taking, to transform information into knowledge.
Ever being annoyed that the content of a sentenced can be accessed from different perspectives?
Use this package to automatically distribute and connect it.  


**Features**

+ Create *kite* environment and pass an arbitrary number of topics as
  arguments
+ Each topic is compiled as a section, subsection down to subparagraph –
  to be specified in the main.tex
+ The statement within the environment is assigned to to all of the
  given topics/keys
+ Additionally a python script creates a list of hyperlinks below
  each statement according to the topics, so that you can easily
  access the affiliated topics and expand the net of your information
+ automatically generated index with keywords in the beginning of the document

# How to use

1. write your stuff into ```./sections/sectionX.tex```
2. include ```section.tex``` files into ```main.tex```using the command ```\processfile{./sections/sectionXPY.tex}```
3. order the keys in ```main.tex``` as ```\kitesections{}``` etc
4. compile using ```python2 cmpl.py```
	+ generates
		+ .keylist.sty
		+ .keylist.tex
		+ .sectionXPY.tex (preprocessed tex file containg ```\kiteKey{}```)

## Project structure

```
.
| cmpl.py
| main.tex
| (library.bib)
| .keylist.sty (generated by cmpl.py)
| .keylist.tex (generated by cmpl.py)
|
|─── /sections/
	| section1.tex
	|		...
```
+ __cmpl.py__
	+ requires python2
	+ compiles the document into a pdf file: ``` python2 cmpl.py ```
	+ here the document name (main.tex or whatever you want) and the section names need to be specified
	+ accepts argument ``` python2 cmpl.py library ``` to process the ```library.bib``` file
	+ generates three files
		+ .keylist.sty
		+ .keylist.tex
		+ .sectionXPY.tex (the preprocessed tex file containing the keys as links below each statement \kiteKey{[key1, key2, ...]})
+ __main.tex__
	+ \processfile{./sections/SECTION} to include the section.tex files containing the kite-formatted content
	+ determines the structure of the Topics by providing the commands ```\kitesection{KEY} ... \kitesubparagraph{KEY}```  
		MIND: Keys/Topics specified here must exisit in one of the sections! No empty topics are allowed yet (can be included by normal ```\section{} etc.```, though).
+ __./sections/SECTION.TEX__
	+ section.tex contain
```
\begin{kite}{key1, key2, ...}
		A STATEMENT
\end{kite}
```
formatted content
+ __.keylist.sty__ list of all existing keys without duplicates. Is generated by cmpl.py and is used by the ```kite.sty```
	+ each key in keylist.sty is used as a heading and all statements that
contain that key are assigned
+ __.keylist.tex__ tex-formatted list of all existing keys without duplicates to include an index

## Available commands

+ __Key formatting__
	+ ```\kitesection{}``` to ```\kitesubparagraph{}```
+ __Text formatting__
	+ ```kiteit{}```
	+ ```kitebf{}```
	+ ```\red{}```
