import flet as ft
import random
import copy
import asyncio

def calculate_conflicts(state, var, val):
    conflicts = 0
    for i in range(9):
        if i != var and state[i] == val:
            conflicts += 1
    if var < 7:
        if val >= state[var + 1]:
            conflicts += 1
    if 0 < var <= 7:
        if state[var - 1] >= val:
            conflicts += 1
    if var == 8:
        for i in range(8):
            if val >= state[i]:
                conflicts += 1
    elif var < 8:
        if state[8] >= val:
            conflicts += 1
    return conflicts

async def run_min_conflicts_async(update_ui_callback):
    max_restarts = 500
    steps_per_try = 500

    for attempt in range(max_restarts):
        state = [random.randint(0, 8) for _ in range(9)]
        await update_ui_callback(state, f"🔄 [LẦN THỬ {attempt + 1}] Khởi tạo bảng ngẫu nhiên: {list(state)}")

        for step in range(steps_per_try):
            conflicted_vars = []
            for i in range(9):
                if calculate_conflicts(state, i, state[i]) > 0:
                    conflicted_vars.append(i)

            if not conflicted_vars:
                await update_ui_callback(state, f"✅ TÌM THẤY NGHIỆM TẠI LẦN THỬ {attempt + 1} (Mất {step} bước)!",
                                         success=True)
                return state

            var = random.choice(conflicted_vars)
            min_c = float('inf')
            best_vals = []

            for v in range(9):
                c = calculate_conflicts(state, var, v)
                if c < min_c:
                    min_c = c
                    best_vals = [v]
                elif c == min_c:
                    best_vals.append(v)

            chosen_val = random.choice(best_vals)
            state[var] = chosen_val

            log_msg = f"Lần {attempt + 1} | Bước {step + 1}: Sửa ô {var} thành {chosen_val} (Số lỗi: {min_c})"
            await update_ui_callback(state, log_msg)

    await update_ui_callback(state, f"❌ KHÔNG TÌM THẤY NGHIỆM SAU {max_restarts} LẦN RESTART.", success=False)
    return None

def satisfies_rule(xi, val_i, xj, val_j):
    if xi < 7 and xj == xi + 1: return val_i < val_j
    if xj < 7 and xi == xj + 1: return val_i > val_j
    if xi == 8 and xj < 8: return val_i < val_j
    if xj == 8 and xi < 8: return val_i > val_j
    return True

def revise(domains, xi, xj):
    revised = False
    for x in domains[xi][:]:
        satisfies = False
        for y in domains[xj]:
            if satisfies_rule(xi, x, xj, y):
                satisfies = True
                break
        if not satisfies:
            domains[xi].remove(x)
            revised = True
    return revised

async def run_ac3_async(update_ui_callback, initial_domains_str):
    domains = []
    try:
        lines = initial_domains_str.strip().split('\n')
        for i in range(9):
            data = list(map(int, lines[i].replace(',', ' ').split()))
            domains.append(data)
    except Exception as e:
        await update_ui_callback(None,
                                 "❌ Lỗi đọc Domain. Vui lòng nhập 9 dòng, mỗi dòng là các số cách nhau bởi khoảng trắng.")
        return

    arcs = []
    for i in range(7):
        arcs.append((i, i + 1))
        arcs.append((i + 1, i))
    for i in range(8):
        arcs.append((8, i))
        arcs.append((i, 8))
    arcs = list(set(arcs))
    queue = copy.deepcopy(arcs)

    await update_ui_callback(domains, "Khởi tạo AC-3: Nạp Queue và các Domains ban đầu.", is_ac3=True)

    loop_count = 0
    done = False
    success = True

    while queue and not done:
        loop_count += 1
        xi, xj = queue.pop(0)

        domain_before = list(domains[xi])
        if revise(domains, xi, xj):
            log_msg = f"Lặp {loop_count}: Xét ({xi}, {xj}) -> Thu gọn Ô {xi}: {domain_before} -> {domains[xi]}"
            await update_ui_callback(domains, log_msg, is_ac3=True)

            if len(domains[xi]) == 0:
                await update_ui_callback(domains, f"❌ Ô {xi} RỖNG! Bài toán vô nghiệm.", is_ac3=True, success=False)
                success = False
                done = True
                break

            added_arcs = []
            for xk in range(9):
                if xk != xi and xk != xj:
                    if (xk, xi) in arcs and (xk, xi) not in queue:
                        queue.append((xk, xi))
                        added_arcs.append((xk, xi))

    if success:
        is_solved = all(len(d) == 1 for d in domains)
        if is_solved:
            await update_ui_callback(domains, "✅ AC-3 ĐÃ ÉP THÀNH CÔNG VỀ 1 NGHIỆM DUY NHẤT!", is_ac3=True,
                                     success=True)
        else:
            await update_ui_callback(domains, "⚠️ AC-3 HOÀN TẤT NHƯNG CHƯA ĐẠT ĐƯỢC 1 NGHIỆM DUY NHẤT.", is_ac3=True)

def main(page: ft.Page):
    page.title = "CSP Visualizer (AC-3 & Min-Conflicts)"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    algo_dropdown = ft.Dropdown(
        label="Thuật toán",
        options=[ft.dropdown.Option("Min-Conflicts"), ft.dropdown.Option("AC-3")],
        value="Min-Conflicts",
        width=200
    )

    speed_dropdown = ft.Dropdown(
        label="Tốc độ hiển thị",
        options=[ft.dropdown.Option("Nhanh"), ft.dropdown.Option("Bình thường"), ft.dropdown.Option("Chậm")],
        value="Nhanh",
        width=150
    )

    default_ac3_domain = "\n".join(["0 1 2 3 4 5 6 7 8" for _ in range(9)])
    ac3_input = ft.TextField(
        label="Domain ban đầu (AC-3)",
        multiline=True,
        min_lines=9,
        max_lines=9,
        value=default_ac3_domain,
        width=300,
        visible=False
    )

    def on_algo_change(e):
        ac3_input.visible = (algo_dropdown.value == "AC-3")
        page.update()

    algo_dropdown.on_change = on_algo_change

    grid_container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )

    log_view = ft.ListView(expand=True, spacing=5, auto_scroll=True)

    def render_grid(state_or_domains, is_ac3=False):
        grid_container.controls.clear()
        if not state_or_domains: return

        for r in range(3):
            row_items = []
            for c in range(3):
                i = r * 3 + c
                if is_ac3:
                    text_val = str(state_or_domains[i]).replace('[', '').replace(']', '')
                    font_size = 14 if len(state_or_domains[i]) > 3 else 20
                else:
                    text_val = str(state_or_domains[i])
                    font_size = 30

                row_items.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"Ô {i}", size=12, color="white70"),
                            ft.Text(text_val, size=font_size, weight="bold", color="white", text_align="center")
                        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        bgcolor="blueaccent",
                        border_radius=8,
                        padding=5,
                        width=120,
                        height=120
                    )
                )
            grid_container.controls.append(ft.Row(row_items, alignment=ft.MainAxisAlignment.CENTER, spacing=10))

        page.update()

    async def update_ui(data, log_msg, is_ac3=False, success=None):
        if data:
            render_grid(data, is_ac3=is_ac3)

        color = "black"
        if success is True:
            color = "green"
        elif success is False:
            color = "red"

        log_view.controls.append(ft.Text(log_msg, color=color))
        page.update()

        delay = 0.1
        if speed_dropdown.value == "Bình thường":
            delay = 0.5
        elif speed_dropdown.value == "Chậm":
            delay = 1.0
        await asyncio.sleep(delay)

    async def solve_and_animate(e):
        btn_start.disabled = True
        log_view.controls.clear()
        grid_container.controls.clear()
        page.update()

        try:
            if algo_dropdown.value == "Min-Conflicts":
                await run_min_conflicts_async(update_ui)
            else:
                await run_ac3_async(update_ui, ac3_input.value)
        finally:
            btn_start.disabled = False
            page.update()

    btn_start = ft.FilledButton("Bắt Đầu Trực Quan", icon=ft.Icons.PLAY_ARROW, on_click=solve_and_animate)

    custom_border = ft.Border(
        top=ft.BorderSide(1, ft.Colors.OUTLINE),
        bottom=ft.BorderSide(1, ft.Colors.OUTLINE),
        left=ft.BorderSide(1, ft.Colors.OUTLINE),
        right=ft.BorderSide(1, ft.Colors.OUTLINE)
    )

    page.add(
        ft.Text("CSP Visualizer (AC-3 & Min-Conflicts)", size=30, weight="bold", color="blueaccent"),
        ft.Row([algo_dropdown, speed_dropdown, btn_start], alignment=ft.MainAxisAlignment.START),
        ft.Row([ac3_input], alignment=ft.MainAxisAlignment.START),
        ft.Divider(),
        ft.Row([
            ft.Container(
                content=grid_container,
                expand=3,
                padding=20,
                border=custom_border,
                border_radius=10
            ),
            ft.VerticalDivider(),
            ft.Container(
                content=ft.Column([
                    ft.Text("Nhật ký thực thi (Logs)", weight="bold", color="blueaccent"),
                    log_view
                ]),
                expand=4,
                padding=10,
                border=custom_border,
                border_radius=10
            )
        ], expand=True)
    )

if __name__ == "__main__":
    ft.run(main)