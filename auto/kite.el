(TeX-add-style-hook
 "kite"
 (lambda ()
   (TeX-run-style-hooks
    "pgffor")
   (TeX-add-symbols)
   (LaTeX-add-environments
    '("kite" LaTeX-env-args ["argument"] 0)))
 :latex)

