import flet as ft
import random
import copy

winMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
]

data = list(map(int, input("Nhập ma trận: ").split()))
matrix = [data[i:i + 3] for i in range(0, 9, 3)]

father = None
action = None
step = 0
fatherList = []
actionList = []
stepList = []
matrixInFrontier = []
frontier = [[matrix, father, action, step]]
matrixInFrontier.append(frontier[0][0])
reached = []
done = False


ui_logs = []

ui_logs.append("Chạy\n")

while (not done and frontier):
    node, father, action, step = frontier.pop(0)
    matrixInFrontier.pop(0)
    reached.append(node)
    fatherList.append(father)
    actionList.append(action)
    stepList.append(step)

    if node == winMatrix:
        print("Tìm được kết quả")

        ui_logs.append("TÌM ĐƯỢC KẾT QUẢ!")
        ui_logs.append("\n")

        pathMatrix = []
        pathAction = []
        pathStep = []

        pathNode = node

        while pathNode is not None:
            i = reached.index(pathNode)
            pathMatrix.append(reached[i])
            pathAction.append(actionList[i])
            pathStep.append(stepList[i])
            pathNode = fatherList[i]

        pathMatrix.reverse()
        pathAction.reverse()
        pathStep.reverse()

        ui_logs.append("ĐƯỜNG ĐI CHI TIẾT TỪ GỐC ĐẾN ĐÍCH:\n")
        print("Đường đi: \n")

        for i in range(len(pathMatrix)):
            log_str = f"Step: {pathStep[i]} | Action: {pathAction[i]}\n"
            for row in pathMatrix[i]:
                log_str += str(row) + "\n"
            ui_logs.append(log_str)

            print(f"Step: {pathStep[i]}")
            print(f"Action: {pathAction[i]}")
            for row in pathMatrix[i]:
                print(row)
            print("\n")

        done = True
        break

    for i in range(3):
        for j in range(3):
            if node[i][j] == 0:
                x, y = i, j

    if x > 0:
        newMatrix = copy.deepcopy(node)
        newMatrix[x][y] = newMatrix[x - 1][y]
        newMatrix[x - 1][y] = 0
        if newMatrix not in matrixInFrontier and newMatrix not in reached:
            frontier.append([newMatrix, node, "UP", step + 1])
            matrixInFrontier.append(newMatrix)

            log_str = f" Action: UP | Step: {step + 1}\n"
            for row in newMatrix:
                log_str += str(row) + "\n"
                print(row)
            ui_logs.append(log_str)
            print("\n")

    if x < 2:
        newMatrix = copy.deepcopy(node)
        newMatrix[x][y] = newMatrix[x + 1][y]
        newMatrix[x + 1][y] = 0
        if newMatrix not in matrixInFrontier and newMatrix not in reached:
            frontier.append([newMatrix, node, "DOWN", step + 1])
            matrixInFrontier.append(newMatrix)

            log_str = f" Action: DOWN | Step: {step + 1}\n"
            for row in newMatrix:
                log_str += str(row) + "\n"
                print(row)
            ui_logs.append(log_str)
            print("\n")

    if y > 0:
        newMatrix = copy.deepcopy(node)
        newMatrix[x][y] = newMatrix[x][y - 1]
        newMatrix[x][y - 1] = 0
        if newMatrix not in matrixInFrontier and newMatrix not in reached:
            frontier.append([newMatrix, node, "LEFT", step + 1])
            matrixInFrontier.append(newMatrix)

            log_str = f" Action: LEFT | Step: {step + 1}\n"
            for row in newMatrix:
                log_str += str(row) + "\n"
                print(row)
            ui_logs.append(log_str)
            print("\n")

    if y < 2:
        newMatrix = copy.deepcopy(node)
        newMatrix[x][y] = newMatrix[x][y + 1]
        newMatrix[x][y + 1] = 0
        if newMatrix not in matrixInFrontier and newMatrix not in reached:
            frontier.append([newMatrix, node, "RIGHT", step + 1])
            matrixInFrontier.append(newMatrix)

            log_str = f" Action: RIGHT | Step: {step + 1}\n"
            for row in newMatrix:
                log_str += str(row) + "\n"
                print(row)
            ui_logs.append(log_str)
            print("\n")

matrix_list = pathMatrix

def main(page: ft.Page):
    page.title = "8 Puzzle BFS "
    page.window.width = 450
    page.window.height = 750
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    current_index = [0]
    cells = [[None for _ in range(3)] for _ in range(3)]

    cell_border = ft.Border(
        top=ft.BorderSide(2, ft.Colors.BLACK87),
        right=ft.BorderSide(2, ft.Colors.BLACK87),
        bottom=ft.BorderSide(2, ft.Colors.BLACK87),
        left=ft.BorderSide(2, ft.Colors.BLACK87)
    )

    log_border = ft.Border(
        top=ft.BorderSide(1, ft.Colors.GREY_400),
        right=ft.BorderSide(1, ft.Colors.GREY_400),
        bottom=ft.BorderSide(1, ft.Colors.GREY_400),
        left=ft.BorderSide(1, ft.Colors.GREY_400)
    )

    grid_rows = []
    for row in range(3):
        row_controls = []
        for col in range(3):
            cell_text = ft.Text(value="", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)

            cell_container = ft.Container(
                content=cell_text,
                width=80,
                height=80,
                bgcolor=ft.Colors.WHITE,
                border=cell_border,
                border_radius=8,
                alignment=ft.Alignment(0, 0)
            )
            cells[row][col] = cell_container
            row_controls.append(cell_container)

        grid_rows.append(ft.Row(controls=row_controls, alignment=ft.MainAxisAlignment.CENTER))

    log_view = ft.ListView(
        expand=True,
        spacing=8,
        auto_scroll=False
    )

    for log_text in ui_logs:
        log_view.controls.append(
            ft.Text(log_text, font_family="Consolas", size=13, color=ft.Colors.BLUE)
        )

    log_container = ft.Container(
        content=log_view,
        border=log_border,
        border_radius=5,
        padding=10,
        expand=True,
        bgcolor=ft.Colors.GREY_100,
        width=350
    )

    def update_grid():
        matrix = matrix_list[current_index[0]]
        for row in range(3):
            for col in range(3):
                val = matrix[row][col]
                container = cells[row][col]
                text_control = container.content
                text_control.value = "" if val == 0 else str(val)
                container.bgcolor = ft.Colors.GREY_300 if val == 0 else ft.Colors.WHITE
        page.update()

    def next_matrix(e):
        if matrix_list and current_index[0] < len(matrix_list) - 1:
            current_index[0] += 1
            update_grid()

    next_btn = ft.ElevatedButton(
        content=ft.Text("Next Matrix", size=16, weight=ft.FontWeight.BOLD),
        on_click=next_matrix,
        width=220,
        height=45
    )

    page.add(
        ft.Column(controls=grid_rows, spacing=10),
        ft.Container(height=10),
        next_btn,
        ft.Container(height=15),
        log_container
    )

    update_grid()

ft.app(target=main)