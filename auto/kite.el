(TeX-add-style-hook
 "kite"
 (lambda ()
   (TeX-run-style-hooks
    "pgffor"
    "environ"
    "keylist"
    "ragged2e")
   (TeX-add-symbols
    '("printlist" ["argument"] 1)
    '("kitecut" 2)
    '("red" 1)
    '("processfile" 1)
    "kiteit"
    "kitebf"
    "kiteKey"
    "kiteref")
   (LaTeX-add-environments
    '("kite" 1)))
 :latex)

