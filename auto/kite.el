(TeX-add-style-hook
 "kite"
 (lambda ()
   (TeX-run-style-hooks
    "pgffor"
    "environ"
    "keylist")
   (TeX-add-symbols
    '("printlist" ["argument"] 1)
    '("red" 1)
    '("processfile" 1)
    "kiteit"
    "kitebf"
    "kiteKey")
   (LaTeX-add-environments
    '("kite" 1)))
 :latex)

