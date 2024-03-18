from latex_builder.latex_tools import generate_latex

data = [
    ["Заголовок 1", "Заголовок 2", "Заголовок 3"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

latex_code = generate_latex(data, "img.jpg")

with open("artifacts/example_img.tex", "w") as file:
    file.write(latex_code)

