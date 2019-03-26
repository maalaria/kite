(TeX-add-style-hook
 "kite"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "pgffor"
    "environ"
    "ragged2e"
    "hyperref")
   (TeX-add-symbols
    '("printlist" ["argument"] 1)
    '("kitesubparagraph" 1)
    '("kiteparagraph" 1)
    '("kitesubsubsection" 1)
    '("kitesubsection" 1)
    '("kitesection" 1)
    '("kitecut" 2)
    '("red" 1)
    '("processfile" 1)
    "kiteit"
    "kitebf"
    "kiteKey"
    "kiteref")
   (LaTeX-add-labels
    "#1")
   (LaTeX-add-environments
    '("kite" 1)))
 :latex)

