latex_header = r"""\documentclass[a4paper, landscape, 12pt]{memoir}
\usepackage[portuges]{babel}
\usepackage[utf8]{inputenc}
\usepackage[top=0cm, bottom=1cm, outer=1cm, inner=1cm]{geometry}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage[scaled]{helvet}
\renewcommand\familydefault{\sfdefault} 
\usepackage[T1]{fontenc}

\begin{document}
"""

latex_footer = r"""
\end{document}"""

background = r"""
\tikz[remember picture,overlay] \node[opacity=0.5,inner sep=0pt] at (current page.center){\includegraphics[width=\paperwidth,height=\paperheight]{background.pdf}};
"""

header_image = r"""
\begin{figure}[h]
\includegraphics[width=\textwidth]{header.pdf}
\end{figure}"""

footer_image = r"""

\begin{figure}[b]
\includegraphics[width=\textwidth]{footer.pdf}
\end{figure}
"""

def assemble_text(nome, curso, evento, local, data, carga, autenticacao):
    text = r"""\begin{vplace}[0.5]
\begin{center}

\Huge
\textbf{Certificamos que} 

\vspace{5mm}

\Huge
\textbf{"""

    text += nome
    text += r"""}
\vspace{5mm}

\huge

Participou do \textbf{"""

    text += curso
    text += r"""}, como parte do evento \textbf{"""
    text += evento
    text += r"""}, realizado em  \textbf{"""
    text += data
    text += r"""}, com duração de \textbf{"""
    text += carga
    text += r"""}, """
    text += local
    text += r""".

\vspace{5mm}
\large
Código de Autenticação: """
    text += autenticacao
    text += r"""
\end{center}
\end{vplace}"""

    return text

def assemble_document(text):
    return latex_header + background + header_image + text + footer_image + latex_footer
