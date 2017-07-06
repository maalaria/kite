(TeX-add-style-hook
 "kite"
 (lambda ()
   (TeX-run-style-hooks
    "environ"
    "pgffor"
    "xstring")
   (TeX-add-symbols
    "CurrentSubject"))
 :latex)

