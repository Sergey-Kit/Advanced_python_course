import latex_tools

data = [
    ["Заголовок 1", "Заголовок 2", "Заголовок 3"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

latex_code = latex_tools.generate_latex(data, "artifacts/img.jpg")

with open("artifacts/example_img.tex", "w") as file:
    file.write(latex_code)