(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("book" "man" "10pt" "a4paper")))
   (TeX-run-style-hooks
    "latex2e"
    "book"
    "bk10"
    "kite")
   (LaTeX-add-labels
    "Face selective cells"
    "Inferior temporal cortex"
    "Superior temporal sulcus"
    "Amygdala"
    "Prefrontal cortex"
    "Lateral intraparietal area"
    "Priority map"
    "Spatial attention"
    "Face perception"))
 :latex)

