import flet as ft
import copy
import asyncio
import random
import math


# =====================================================================
# HÀM TRỢ GIÚP CHUNG CHO MÔI TRƯỜNG PARTIAL OBSERVABLE (BELIEF STATES)
# =====================================================================

def is_goal(state, goals):
    """
    state: tuple các ma trận hiện tại. Ví dụ (matrix1, matrix2)
    goals: list các ma trận đích. Ví dụ [winMatrix1, winMatrix2]
    Trả về True nếu tất cả các ma trận trong state đều trùng với CÙNG MỘT ma trận đích.
    """
    for g in goals:
        if all(m == g for m in state):
            return True
    return False


def get_neighbors(state, goals):
    """
    Sinh các trạng thái lân cận. Nếu một sub-state đã tới đích, nó sẽ đứng im.
    Trả về: danh sách các tuple (new_state, action_name)
    """
    actions = [
        ("UP", lambda x, y: (x > 0, x - 1, y)),
        ("DOWN", lambda x, y: (x < 2, x + 1, y)),
        ("LEFT", lambda x, y: (y > 0, x, y - 1)),
        ("RIGHT", lambda x, y: (y < 2, x, y + 1))
    ]
    neighbors = []

    for act_name, condition in actions:
        new_state_list = []
        moved_at_least_one = False

        for m in state:
            # Nếu ma trận này đã khớp với bất kỳ goal nào, nó sẽ ngừng di chuyển
            if any(m == g for g in goals):
                new_state_list.append(copy.deepcopy(m))
                continue

            x, y = -1, -1
            for i in range(3):
                for j in range(3):
                    if m[i][j] == 0:
                        x, y = i, j

            can_move, nx, ny = condition(x, y)
            if can_move:
                new_m = copy.deepcopy(m)
                new_m[x][y] = new_m[nx][ny]
                new_m[nx][ny] = 0
                new_state_list.append(new_m)
                moved_at_least_one = True
            else:
                new_state_list.append(copy.deepcopy(m))

        if moved_at_least_one:
            neighbors.append((tuple(new_state_list), act_name))

    return neighbors


def get_hn(state, goals):
    """Tính tổng Heuristic (Manhattan distance) cho toàn bộ belief state"""
    hn = 0
    for m in state:
        for a in range(1, 9):
            x1, y1 = -1, -1
            for i in range(3):
                for j in range(3):
                    if m[i][j] == a: x1, y1 = i, j

            for g in goals:
                xg, yg = -1, -1
                for i in range(3):
                    for j in range(3):
                        if g[i][j] == a: xg, yg = i, j
                hn += abs(x1 - xg) + abs(y1 - yg)
    return hn


def get_ucs_gn(state, goals, step):
    """Cost cho thuật toán UCS"""
    gn = step
    for m in state:
        for g in goals:
            for i in range(3):
                for j in range(3):
                    if m[i][j] != 0 and m[i][j] != g[i][j]:
                        gn += 1
    return gn


# =====================================================================
# THUẬT TOÁN TÌM KIẾM
# =====================================================================

def solve_bfs(start_state, goals):
    if is_goal(start_state, goals): return [start_state], ["None"], [0]
    frontier = [[start_state, None, "None", 0]]
    matrixInFrontier = [start_state]
    reached = []
    fatherList = []
    actionList = []
    stepList = []

    while frontier:
        node, father, action, step = frontier.pop(0)
        matrixInFrontier.pop(0)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        for new_state, act in get_neighbors(node, goals):
            if new_state not in matrixInFrontier and new_state not in reached:
                if is_goal(new_state, goals):
                    reached.append(new_state)
                    fatherList.append(node)
                    actionList.append(act)
                    stepList.append(step + 1)

                    pathState, pathAction, pathStep = [], [], []
                    curr = new_state
                    while curr is not None:
                        idx = reached.index(curr)
                        pathState.append(reached[idx])
                        pathAction.append(actionList[idx])
                        pathStep.append(stepList[idx])
                        curr = fatherList[idx]
                    pathState.reverse()
                    pathAction.reverse()
                    pathStep.reverse()
                    return pathState, pathAction, pathStep
                else:
                    frontier.append([new_state, node, act, step + 1])
                    matrixInFrontier.append(new_state)
    return None, None, None


def solve_dfs(start_state, goals):
    if is_goal(start_state, goals): return [start_state], ["None"], [0]
    frontier = [[start_state, None, "None", 0]]
    matrixInFrontier = [start_state]
    reached = []
    fatherList = []
    actionList = []
    stepList = []

    while frontier:
        node, father, action, step = frontier.pop()
        if node in matrixInFrontier:
            matrixInFrontier.remove(node)

        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        for new_state, act in get_neighbors(node, goals):
            if new_state not in matrixInFrontier and new_state not in reached:
                if is_goal(new_state, goals):
                    reached.append(new_state)
                    fatherList.append(node)
                    actionList.append(act)
                    stepList.append(step + 1)

                    pathState, pathAction, pathStep = [], [], []
                    curr = new_state
                    while curr is not None:
                        idx = reached.index(curr)
                        pathState.append(reached[idx])
                        pathAction.append(actionList[idx])
                        pathStep.append(stepList[idx])
                        curr = fatherList[idx]
                    pathState.reverse()
                    pathAction.reverse()
                    pathStep.reverse()
                    return pathState, pathAction, pathStep
                else:
                    frontier.append([new_state, node, act, step + 1])
                    matrixInFrontier.append(new_state)
    return None, None, None


def solve_ids(start_state, goals, max_depth=30):
    depth = 0
    while depth <= max_depth:
        frontier = [[start_state, None, "None", 0]]
        matrixInFrontier = [start_state]
        reached = []
        fatherList = []
        actionList = []
        stepList = []
        result = None

        while frontier:
            node, father, action, step = frontier.pop()
            if node in matrixInFrontier:
                matrixInFrontier.remove(node)

            reached.append(node)
            fatherList.append(father)
            actionList.append(action)
            stepList.append(step)

            if is_goal(node, goals):
                result = (reached, fatherList, actionList, stepList)
                break

            if step >= depth:
                continue

            for new_state, act in get_neighbors(node, goals):
                if new_state not in matrixInFrontier and new_state not in reached:
                    if is_goal(new_state, goals):
                        reached.append(new_state)
                        fatherList.append(node)
                        actionList.append(act)
                        stepList.append(step + 1)
                        result = (reached, fatherList, actionList, stepList)
                        break
                    frontier.append([new_state, node, act, step + 1])
                    matrixInFrontier.append(new_state)

            if result is not None:
                break

        if result is not None:
            reached, fatherList, actionList, stepList = result
            pathState, pathAction, pathStep = [], [], []
            curr = reached[-1]
            while curr is not None:
                idx = reached.index(curr)
                pathState.append(reached[idx])
                pathAction.append(actionList[idx])
                pathStep.append(stepList[idx])
                curr = fatherList[idx]
            pathState.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathState, pathAction, pathStep

        depth += 1
    return None, None, None


def solve_greedy(start_state, goals):
    step = 0
    cost = get_hn(start_state, goals) + step  # Giữ nguyên logic gn + hn từ file của bạn
    frontier = [[start_state, None, "None", step, cost]]
    matrixInFrontier = [start_state]
    reached = []
    fatherList = []
    actionList = []
    stepList = []

    while frontier:
        minIdx = 0
        for i in range(1, len(frontier)):
            if frontier[i][4] < frontier[minIdx][4]: minIdx = i

        node, father, action, step, cost = frontier.pop(minIdx)
        matrixInFrontier.remove(node)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        if is_goal(node, goals):
            pathState, pathAction, pathStep = [], [], []
            curr = node
            while curr is not None:
                idx = reached.index(curr)
                pathState.append(reached[idx])
                pathAction.append(actionList[idx])
                pathStep.append(stepList[idx])
                curr = fatherList[idx]
            pathState.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathState, pathAction, pathStep

        for new_state, act in get_neighbors(node, goals):
            if new_state not in matrixInFrontier and new_state not in reached:
                new_cost = get_hn(new_state, goals) + step + 1
                frontier.append([new_state, node, act, step + 1, new_cost])
                matrixInFrontier.append(new_state)

    return None, None, None


def solve_ucs(start_state, goals):
    step = 0
    cost = get_ucs_gn(start_state, goals, step)
    frontier = [[start_state, None, "None", step, cost]]
    matrixInFrontier = [start_state]
    reached = []
    fatherList = []
    actionList = []
    stepList = []

    while frontier:
        minIdx = 0
        for i in range(1, len(frontier)):
            if frontier[i][4] < frontier[minIdx][4]: minIdx = i

        node, father, action, step, cost = frontier.pop(minIdx)
        matrixInFrontier.remove(node)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)

        if is_goal(node, goals):
            pathState, pathAction, pathStep = [], [], []
            curr = node
            while curr is not None:
                idx = reached.index(curr)
                pathState.append(reached[idx])
                pathAction.append(actionList[idx])
                pathStep.append(stepList[idx])
                curr = fatherList[idx]
            pathState.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathState, pathAction, pathStep

        for new_state, act in get_neighbors(node, goals):
            if new_state not in matrixInFrontier and new_state not in reached:
                new_cost = get_ucs_gn(new_state, goals, step + 1)
                frontier.append([new_state, node, act, step + 1, new_cost + cost])
                matrixInFrontier.append(new_state)

    return None, None, None


def solve_astar(start_state, goals):
    costList = []
    fatherList = []
    actionList = []
    stepList = []
    matrixInFrontier = []

    step = 0
    cost = get_hn(start_state, goals) + step
    frontier = [[start_state, None, "None", step, cost]]
    matrixInFrontier.append(start_state)
    reached = []

    while frontier:
        minIdx = 0
        for i in range(1, len(frontier)):
            if frontier[i][4] < frontier[minIdx][4]: minIdx = i
        node, father, action, step, cost = frontier.pop(minIdx)

        matrixInFrontier.remove(node)
        reached.append(node)
        fatherList.append(father)
        actionList.append(action)
        stepList.append(step)
        costList.append(cost)

        if is_goal(node, goals):
            pathState, pathAction, pathStep = [], [], []
            curr = node
            while curr is not None:
                idx = reached.index(curr)
                pathState.append(reached[idx])
                pathAction.append(actionList[idx])
                pathStep.append(stepList[idx])
                curr = fatherList[idx]
            pathState.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathState, pathAction, pathStep

        for new_state, act in get_neighbors(node, goals):
            g_new = step + 1
            new_cost = get_hn(new_state, goals) + g_new

            in_reached = False
            for i in range(len(reached)):
                if reached[i] == new_state:
                    in_reached = True
                    if g_new < stepList[i]:
                        reached.pop(i)
                        fatherList.pop(i)
                        actionList.pop(i)
                        stepList.pop(i)
                        costList.pop(i)
                        frontier.append([new_state, node, act, g_new, new_cost])
                        matrixInFrontier.append(new_state)
                    break

            if not in_reached:
                in_frontier = False
                for i in range(len(frontier)):
                    if frontier[i][0] == new_state:
                        in_frontier = True
                        if g_new < frontier[i][3]:
                            frontier[i][1] = node
                            frontier[i][2] = act
                            frontier[i][3] = g_new
                            frontier[i][4] = new_cost
                        break
                if not in_frontier:
                    frontier.append([new_state, node, act, g_new, new_cost])
                    matrixInFrontier.append(new_state)

    return None, None, None


def solve_idastar(start_state, goals):
    costLimit = get_hn(start_state, goals)
    while True:
        frontier = [[start_state, None, "None", 0]]
        matrixInFrontier = [start_state]
        reached = []
        fatherList = []
        actionList = []
        stepList = []
        result = None
        nextCostLimit = float('inf')

        while frontier:
            node, father, action, step = frontier.pop()
            if node in matrixInFrontier:
                matrixInFrontier.remove(node)

            reached.append(node)
            fatherList.append(father)
            actionList.append(action)
            stepList.append(step)

            if is_goal(node, goals):
                result = (reached, fatherList, actionList, stepList)
                break

            for new_state, act in get_neighbors(node, goals):
                if new_state not in matrixInFrontier and new_state not in reached:
                    costChild = get_hn(new_state, goals) + step + 1
                    if costChild > costLimit:
                        if costChild < nextCostLimit:
                            nextCostLimit = costChild
                    else:
                        if is_goal(new_state, goals):
                            reached.append(new_state)
                            fatherList.append(node)
                            actionList.append(act)
                            stepList.append(step + 1)
                            result = (reached, fatherList, actionList, stepList)
                            break
                        frontier.append([new_state, node, act, step + 1])
                        matrixInFrontier.append(new_state)
            if result is not None:
                break

        if result is not None:
            reached, fatherList, actionList, stepList = result
            pathState, pathAction, pathStep = [], [], []
            curr = reached[-1]
            while curr is not None:
                idx = reached.index(curr)
                pathState.append(reached[idx])
                pathAction.append(actionList[idx])
                pathStep.append(stepList[idx])
                curr = fatherList[idx]
            pathState.reverse()
            pathAction.reverse()
            pathStep.reverse()
            return pathState, pathAction, pathStep

        costLimit = nextCostLimit
        if costLimit == float('inf'):
            return None, None, None


def solve_simple_hill_climbing(start_state, goals):
    cost = get_hn(start_state, goals)
    info = [[start_state, None, "None", 0, cost]]
    done = False

    while not done:
        current_state = info[-1][0]
        if is_goal(current_state, goals): break

        moved = False
        for new_state, act in get_neighbors(current_state, goals):
            childCost = get_hn(new_state, goals)
            if childCost < info[-1][4]:
                info.append([new_state, current_state, act, info[-1][3] + 1, childCost])
                moved = True
                break

        if not moved:
            done = True

    return [s[0] for s in info], [s[2] for s in info], [s[3] for s in info]


def solve_steepest_ascent_hill_climbing(start_state, goals):
    cost = get_hn(start_state, goals)
    info = [[start_state, None, "None", 0, cost]]
    done = False

    while not done:
        current_state = info[-1][0]
        if is_goal(current_state, goals): break

        best_state, best_cost, best_act = None, info[-1][4], None

        for new_state, act in get_neighbors(current_state, goals):
            childCost = get_hn(new_state, goals)
            if childCost < best_cost:
                best_state = new_state
                best_cost = childCost
                best_act = act

        if best_state is not None:
            info.append([best_state, current_state, best_act, info[-1][3] + 1, best_cost])
        else:
            done = True

    return [s[0] for s in info], [s[2] for s in info], [s[3] for s in info]


def solve_stochastic_hill_climbing(start_state, goals):
    cost = get_hn(start_state, goals)
    info = [[start_state, None, "None", 0, cost]]
    done = False

    while not done:
        current_state = info[-1][0]
        if is_goal(current_state, goals): break

        better_neighbors = []
        for new_state, act in get_neighbors(current_state, goals):
            childCost = get_hn(new_state, goals)
            if childCost < info[-1][4]:
                better_neighbors.append([new_state, current_state, act, info[-1][3] + 1, childCost])

        if better_neighbors:
            info.append(random.choice(better_neighbors))
        else:
            done = True

    return [s[0] for s in info], [s[2] for s in info], [s[3] for s in info]


def solve_random_restart_hill_climbing(start_state, goals, maxRestart=50):
    for _ in range(maxRestart):
        pathState, pathAction, pathStep = solve_steepest_ascent_hill_climbing(start_state, goals)
        if pathState and is_goal(pathState[-1], goals):
            return pathState, pathAction, pathStep
    return pathState, pathAction, pathStep  # Return last attempt if fail


def solve_local_beam_search(start_state, goals, k=2):
    cost = get_hn(start_state, goals)
    info = [[start_state, None, "None", 0, cost]]
    currentStateSet = [info]
    visited = [start_state]
    done = False

    while not done:
        neighborStates = []
        for currStatePath in currentStateSet:
            curr_state = currStatePath[-1][0]
            curr_step = currStatePath[-1][3]

            if is_goal(curr_state, goals):
                return [s[0] for s in currStatePath], [s[2] for s in currStatePath], [s[3] for s in currStatePath]

            for new_state, act in get_neighbors(curr_state, goals):
                if new_state not in visited:
                    visited.append(new_state)
                    childCost = get_hn(new_state, goals)
                    newStatePath = copy.deepcopy(currStatePath)
                    newStatePath.append([new_state, curr_state, act, curr_step + 1, childCost])
                    neighborStates.append(newStatePath)

        if len(neighborStates) == 0:
            bestInfo = currentStateSet[0]
            return [s[0] for s in bestInfo], [s[2] for s in bestInfo], [s[3] for s in bestInfo]

        for neighbor in neighborStates:
            if is_goal(neighbor[-1][0], goals):
                return [s[0] for s in neighbor], [s[2] for s in neighbor], [s[3] for s in neighbor]

        neighborStates.sort(key=lambda path: path[-1][4])
        currentStateSet = neighborStates[:k]

    return None, None, None


def solve_simulated_annealing(start_state, goals, T0=100.0, Tmin=0.01, alpha=0.99):
    T = T0
    cost = get_hn(start_state, goals)
    info = [[start_state, None, "None", 0, cost]]

    while T > Tmin:
        current_state = info[-1][0]
        if is_goal(current_state, goals): break

        neighbors_raw = get_neighbors(current_state, goals)
        if not neighbors_raw: break

        randomNeighbor = []
        for new_state, act in neighbors_raw:
            childCost = get_hn(new_state, goals)
            randomNeighbor.append([new_state, current_state, act, info[-1][3] + 1, childCost])

        nextStateInfo = random.choice(randomNeighbor)
        denta = nextStateInfo[4] - info[-1][4]

        if denta < 0:
            info.append(nextStateInfo)
        else:
            try:
                p = math.exp(-denta / T)
            except OverflowError:
                p = 0.0
            if random.random() < p:
                info.append(nextStateInfo)

        T = alpha * T

    return [s[0] for s in info], [s[2] for s in info], [s[3] for s in info]


# =====================================================================
# GIAO DIỆN CHÍNH FLET
# =====================================================================

def main(page: ft.Page):
    page.title = "8-Puzzle Multi-Algorithm & Partial Observable Visualizer"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 1100
    page.window.height = 900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    # 1. Các Dropdown Lựa Chọn
    mode_dropdown = ft.Dropdown(
        label="Độ quan sát (Môi trường)",
        options=[
            ft.dropdown.Option("Hoàn toàn (1 Start - 1 Goal)"),
            ft.dropdown.Option("Start mù (2 Start - 1 Goal)"),
            ft.dropdown.Option("Goal mù (1 Start - 2 Goal)"),
            ft.dropdown.Option("Cả 2 mù (2 Start - 2 Goal)"),
        ],
        value="Hoàn toàn (1 Start - 1 Goal)",
        width=300
    )

    algo_dropdown = ft.Dropdown(
        label="Thuật toán",
        options=[
            ft.dropdown.Option("BFS"),
            ft.dropdown.Option("DFS"),
            ft.dropdown.Option("IDS"),
            ft.dropdown.Option("Greedy"),
            ft.dropdown.Option("UCS"),
            ft.dropdown.Option("A*"),
            ft.dropdown.Option("IDA*"),
            ft.dropdown.Option("Simple Hill Climbing"),
            ft.dropdown.Option("Steepest Ascent Hill Climbing"),
            ft.dropdown.Option("Stochastic Hill Climbing"),
            ft.dropdown.Option("Random Restart Hill Climbing"),
            ft.dropdown.Option("Local Beam Search"),
            ft.dropdown.Option("Simulated Annealing"),
        ],
        value="Greedy",
        width=250
    )

    # 2. Input Fields Tùy Biến (Đã bỏ visible=False để luôn hiển thị)
    start1_input = ft.TextField(label="Start 1 (VD: 1 2 3 4 0 6 7 5 8)", value="1 2 3 4 0 6 7 5 8", width=250)
    start2_input = ft.TextField(label="Start 2 (VD: 1 2 3 4 5 6 7 0 8)", value="1 2 3 4 5 6 7 0 8", width=250)

    goal1_input = ft.TextField(label="Goal 1 (VD: 1 2 3 4 5 6 7 8 0)", value="1 2 3 4 5 6 7 8 0", width=250)
    goal2_input = ft.TextField(label="Goal 2 (VD: 1 2 3 4 5 6 7 8 0)", value="1 2 3 4 5 6 7 8 0", width=250)

    k_input = ft.TextField(label="K (Beam Search)", value="2", width=120)
    t0_input = ft.TextField(label="T0 (SA)", value="100.0", width=100)
    tmin_input = ft.TextField(label="Tmin (SA)", value="0.01", width=100)
    alpha_input = ft.TextField(label="Alpha (SA)", value="0.99", width=100)

    log_view = ft.ListView(expand=True, spacing=5, padding=10)
    grid_container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # UI Ma trận
    def create_puzzle_ui(matrix):
        rows = []
        for r in range(3):
            cols = []
            for c in range(3):
                val = matrix[r][c]
                cols.append(
                    ft.Container(
                        content=ft.Text(str(val) if val != 0 else "", size=25, weight="bold"),
                        alignment=ft.Alignment(0, 0),
                        width=70, height=70,
                        bgcolor=ft.Colors.BLUE_ACCENT_700 if val != 0 else ft.Colors.GREY_900,
                        border_radius=10,
                    )
                )
            rows.append(ft.Row(cols, alignment=ft.MainAxisAlignment.CENTER))
        return ft.Container(content=ft.Column(rows), padding=10)

    # Hiển thị song song các Start States (Belief States)
    def create_belief_state_ui(state_tuple):
        boards = [create_puzzle_ui(m) for m in state_tuple]
        return ft.Row(boards, alignment=ft.MainAxisAlignment.CENTER)

    async def solve_and_animate(e):
        current_mode = mode_dropdown.value
        try:
            # Thu thập Start States
            raw_s1 = list(map(int, start1_input.value.split()))
            start_state = ([raw_s1[i:i + 3] for i in range(0, 9, 3)],)

            # Chỉ lấy Start 2 nếu mode yêu cầu
            if current_mode in ["Start mù (2 Start - 1 Goal)", "Cả 2 mù (2 Start - 2 Goal)"]:
                raw_s2 = list(map(int, start2_input.value.split()))
                start_state = start_state + ([raw_s2[i:i + 3] for i in range(0, 9, 3)],)

            # Thu thập Goal States
            raw_g1 = list(map(int, goal1_input.value.split()))
            goals = [[raw_g1[i:i + 3] for i in range(0, 9, 3)]]

            # Chỉ lấy Goal 2 nếu mode yêu cầu
            if current_mode in ["Goal mù (1 Start - 2 Goal)", "Cả 2 mù (2 Start - 2 Goal)"]:
                raw_g2 = list(map(int, goal2_input.value.split()))
                goals.append([raw_g2[i:i + 3] for i in range(0, 9, 3)])
        except:
            log_view.controls.append(
                ft.Text("Lỗi: Nhập đúng định dạng 9 số nguyên cách nhau bằng khoảng trắng!", color="red"))
            page.update()
            return

        selected_algo = algo_dropdown.value
        log_view.controls.clear()
        log_view.controls.append(
            ft.Text(f"Đang tính toán bằng {selected_algo} với {current_mode}...", color="yellow"))

        grid_container.controls.clear()
        grid_container.controls.append(ft.Text("BƯỚC: 0 | INIT", size=20))
        grid_container.controls.append(create_belief_state_ui(start_state))
        page.update()
        await asyncio.sleep(0.1)

        pathState, pathAction, pathStep = None, None, None

        if selected_algo == "BFS":
            pathState, pathAction, pathStep = solve_bfs(start_state, goals)
        elif selected_algo == "DFS":
            pathState, pathAction, pathStep = solve_dfs(start_state, goals)
        elif selected_algo == "IDS":
            pathState, pathAction, pathStep = solve_ids(start_state, goals)
        elif selected_algo == "Greedy":
            pathState, pathAction, pathStep = solve_greedy(start_state, goals)
        elif selected_algo == "UCS":
            pathState, pathAction, pathStep = solve_ucs(start_state, goals)
        elif selected_algo == "A*":
            pathState, pathAction, pathStep = solve_astar(start_state, goals)
        elif selected_algo == "IDA*":
            pathState, pathAction, pathStep = solve_idastar(start_state, goals)
        elif selected_algo == "Simple Hill Climbing":
            pathState, pathAction, pathStep = solve_simple_hill_climbing(start_state, goals)
        elif selected_algo == "Steepest Ascent Hill Climbing":
            pathState, pathAction, pathStep = solve_steepest_ascent_hill_climbing(start_state, goals)
        elif selected_algo == "Stochastic Hill Climbing":
            pathState, pathAction, pathStep = solve_stochastic_hill_climbing(start_state, goals)
        elif selected_algo == "Random Restart Hill Climbing":
            pathState, pathAction, pathStep = solve_random_restart_hill_climbing(start_state, goals)
        elif selected_algo == "Local Beam Search":
            k_val = int(k_input.value) if k_input.value.isdigit() else 2
            pathState, pathAction, pathStep = solve_local_beam_search(start_state, goals, k=k_val)
        elif selected_algo == "Simulated Annealing":
            try:
                t0_val = float(t0_input.value)
            except:
                t0_val = 100.0
            try:
                tmin_val = float(tmin_input.value)
            except:
                tmin_val = 0.01
            try:
                alpha_val = float(alpha_input.value)
            except:
                alpha_val = 0.99
            pathState, pathAction, pathStep = solve_simulated_annealing(start_state, goals, T0=t0_val, Tmin=tmin_val,
                                                                        alpha=alpha_val)

        if pathState:
            log_view.controls.append(ft.Text(f"Tìm thấy đích sau {len(pathState) - 1} bước!", color="green"))
            page.update()
            await asyncio.sleep(1)

            for i in range(len(pathState)):
                grid_container.controls.clear()
                grid_container.controls.append(
                    ft.Text(f"BƯỚC: {pathStep[i]} | {pathAction[i]}", size=20, weight="bold"))
                grid_container.controls.append(create_belief_state_ui(pathState[i]))
                log_view.controls.insert(0, ft.Text(f"Step {pathStep[i]}: {pathAction[i]}"))
                page.update()
                await asyncio.sleep(0.5)
        else:
            log_view.controls.append(ft.Text("Không tìm thấy kết quả hoặc đạt giới hạn duyệt!", color="red"))
            page.update()

    # Layout ghép
    page.add(
        ft.Text("8-Puzzle Visualizer", size=30, weight="bold", color="blueaccent"),

        # Hàng 1: Dropdown Setup
        ft.Row([mode_dropdown, algo_dropdown], alignment=ft.MainAxisAlignment.CENTER),

        # Hàng 2: Input Setup
        ft.Row([
            ft.Column([start1_input, start2_input]),
            ft.Column([goal1_input, goal2_input]),
            ft.Column([k_input, ft.Row([t0_input, tmin_input, alpha_input])])
        ], alignment=ft.MainAxisAlignment.CENTER),

        ft.FilledButton("Bắt Đầu Trực Quan (Giải)", icon=ft.Icons.PLAY_ARROW, on_click=solve_and_animate),
        ft.Divider(),

        # Vùng hiển thị kết quả
        ft.Row([
            ft.Container(grid_container, expand=5),
            ft.VerticalDivider(),
            ft.Container(
                content=ft.Column([ft.Text("Lịch Sử Duyệt:", weight="bold"), log_view]),
                expand=2, bgcolor=ft.Colors.WHITE10, padding=10, border_radius=10
            )
        ], height=450)
    )


if __name__ == "__main__":
    ft.run(main)