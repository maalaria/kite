(TeX-add-style-hook
 "test"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "pgffor"
    "environ"
    "filecontents")
   (TeX-add-symbols
    '("printlist" ["argument"] 1)
    '("processfile" 1)))
 :latex)

