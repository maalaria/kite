(TeX-add-style-hook
 "test"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "kite")
   (LaTeX-add-environments
    '("kite" LaTeX-env-args ["argument"] 0)))
 :latex)

