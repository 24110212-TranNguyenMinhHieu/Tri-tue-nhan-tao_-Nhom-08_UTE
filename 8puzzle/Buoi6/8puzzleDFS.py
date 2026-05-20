import flet as ft
import copy
import asyncio


def main(page: ft.Page):
    page.title = "8-Puzzle BFS Visualizer"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 900
    page.window.height = 850
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    input_field = ft.TextField(
        label="Nhập ma trận (ví dụ: 1 2 3 4 0 6 7 5 8)",
        value="1 2 3 4 0 6 7 5 8",
        width=400
    )
    log_view = ft.ListView(expand=True, spacing=5, padding=10)
    grid_container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def create_puzzle_ui(matrix):
        rows = []
        for r in range(3):
            cols = []
            for c in range(3):
                val = matrix[r][c]
                cols.append(
                    ft.Container(
                        content=ft.Text(str(val) if val != 0 else "", size=25, weight="bold"),
                        # Cách fix lỗi alignment trên các version mới: dùng string hoặc Alignment(0,0)
                        alignment=ft.Alignment(0, 0),
                        width=70, height=70,
                        bgcolor=ft.Colors.BLUE_ACCENT_700 if val != 0 else ft.Colors.GREY_900,
                        border_radius=10,
                    )
                )
            rows.append(ft.Row(cols, alignment=ft.MainAxisAlignment.CENTER))
        return ft.Container(content=ft.Column(rows), padding=20)

    async def solve_and_animate(e):
        try:
            raw_data = list(map(int, input_field.value.split()))
            if len(raw_data) != 9: raise ValueError
            matrix = [raw_data[i:i + 3] for i in range(0, 9, 3)]
        except:
            log_view.controls.append(ft.Text("Lỗi: Nhập đúng 9 số!", color="red"))
            page.update()
            return

        winMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        father, action, step = None, None, 0
        fatherList, actionList, stepList = [], [], []
        matrixInFrontier, reached = [], []
        frontier = [[matrix, father, action, step]]
        matrixInFrontier.append(frontier[0][0])
        done = False

        log_view.controls.clear()
        log_view.controls.append(ft.Text("Đang tính toán...", color="yellow"))
        page.update()

        if matrix == winMatrix:
            done = True

        while (not done and frontier):
            node, father, action, step = frontier.pop(0)
            if matrixInFrontier: matrixInFrontier.pop(0)

            reached.append(node)
            fatherList.append(father)
            actionList.append(action)
            stepList.append(step)

            x, y = 0, 0
            for i in range(3):
                for j in range(3):
                    if node[i][j] == 0: x, y = i, j

            moves = [
                (x > 0, x - 1, y, "UP"),
                (not done and x < 2, x + 1, y, "DOWN"),
                (not done and y > 0, x, y - 1, "LEFT"),
                (not done and y < 2, x, y + 1, "RIGHT")
            ]

            for condition, nx, ny, move_name in moves:
                if condition:
                    newMatrix = copy.deepcopy(node)
                    newMatrix[x][y] = newMatrix[nx][ny]
                    newMatrix[nx][ny] = 0
                    if newMatrix not in matrixInFrontier and newMatrix not in reached:
                        if newMatrix == winMatrix:
                            reached.append(newMatrix)
                            fatherList.append(node)
                            actionList.append(move_name)
                            stepList.append(step + 1)
                            done = True
                            break
                        else:
                            frontier.append([newMatrix, node, move_name, step + 1])
                            matrixInFrontier.append(newMatrix)

        if done:
            pathMatrix, pathAction, pathStep = [], [], []
            pathNode = reached[-1]
            while pathNode is not None:
                idx = reached.index(pathNode)
                pathMatrix.append(reached[idx])
                pathAction.append(actionList[idx])
                pathStep.append(stepList[idx])
                pathNode = fatherList[idx]

            pathMatrix.reverse()
            pathAction.reverse()
            pathStep.reverse()

            for i in range(len(pathMatrix)):
                grid_container.controls.clear()
                grid_container.controls.append(ft.Text(f"BƯỚC: {pathStep[i]} | {pathAction[i]}", size=20))
                grid_container.controls.append(create_puzzle_ui(pathMatrix[i]))
                log_view.controls.insert(0, ft.Text(f"Step {pathStep[i]}: {pathAction[i]}"))
                page.update()
                await asyncio.sleep(0.5)
        else:
            log_view.controls.append(ft.Text("Không tìm thấy kết quả!", color="red"))
            page.update()

    page.add(
        ft.Text("8-Puzzle Visualizer (New Version)", size=30, weight="bold", color="blueaccent"),
        ft.Row([
            input_field,
            ft.FilledButton("Giải và Chạy", icon=ft.Icons.PLAY_ARROW, on_click=solve_and_animate)
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([
            ft.Container(grid_container, expand=2),
            ft.VerticalDivider(),
            ft.Container(
                content=ft.Column([ft.Text("Log:"), log_view]),
                expand=1, bgcolor=ft.Colors.WHITE10, padding=10, border_radius=10
            )
        ], height=500)
    )

if __name__ == "__main__":
    ft.run(main)