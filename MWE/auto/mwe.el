(TeX-add-style-hook
 "mwe"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("scrartcl" "man" "10pt" "a4paper")))
   (TeX-run-style-hooks
    "latex2e"
    "content"
    "scrartcl"
    "scrartcl10"
    "kite"))
 :latex)

