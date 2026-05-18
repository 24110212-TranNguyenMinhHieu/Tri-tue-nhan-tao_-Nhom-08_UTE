Chương trình này mô phỏng quá trình giải bài toán 8Puzzle bằng thuật toán BFS.
Bộ mã nguồn gồm 4 file: 2 file Jupyter Notebook (.ipynb) chứa logic thuật toán in ra console và 2 file Python (.py) tích hợp giao diện trực quan (Visualizer) sử dụng thư viện Flet.

CÁCH HOẠT ĐỘNG:
Môi trường: Một ma trận 3x3 chứa các số từ 1 đến 8 và một ô trống (được đại diện bằng số 0).
Mục tiêu: Di chuyển ô trống (Lên, Xuống, Trái, Phải) để sắp xếp ma trận từ trạng thái ban đầu về trạng thái đích (Win Matrix) theo thứ tự:
1 2 3
4 5 6
7 8 0
Thuật toán BFS: 
    - Cách 1 (8puzzleBFS1): Lấy trạng thái từ danh sách chờ (frontier) ra rồi mới kiểm tra xem đã đến đích chưa.
    - Cách 2 (8puzzleBFS2): Kiểm tra trạng thái đích ngay khi vừa tạo ra trạng thái mới (trước khi đưa vào danh sách chờ), giúp phát hiện kết quả sớm hơn.
Kết thúc: Chương trình sẽ dừng lại khi tìm được đường đi tới đích và truy xuất lại từng bước di chuyển (Step), kèm theo hành động tương ứng (UP, DOWN, LEFT, RIGHT).

HƯỚNG DẪN SỬ DỤNG:
Tùy vào việc bạn muốn xem kết quả dưới dạng text hay giao diện, hãy làm theo các bước sau:
    1. Nếu sử dụng các file logic thuần (.ipynb):
-Mở file 8puzzleBFS1.ipynb hoặc 8puzzleBFS2.ipynb và chạy (Run) Cell code.
-Cách nhập: Khi chương trình yêu cầu "Nhập ma trận:", bạn cần nhập 9 số (từ 0 đến 8, không trùng lặp) cách nhau bởi dấu cách.
-Ví dụ: 1 2 3 0 5 6 4 7 8
-Sau khi nhập, chương trình sẽ tự động duyệt BFS và in ra màn hình console chi tiết từng ma trận ứng với mỗi bước đi cho đến khi tới đích.
  2. Nếu sử dụng các file giao diện Visualizer (.py):
-Đảm bảo bạn đã cài đặt thư viện Flet (chạy lệnh pip install flet trong terminal nếu chưa có).
-Chạy file 8puzzleBFS1.py hoặc 8puzzleBFS2.py.
-Dưới terminal, chương trình sẽ yêu cầu bạn nhập 9 số giống hệt như trên. (Ví dụ: 1 2 3 0 5 6 4 7 8).
-Ngay sau khi nhập và thuật toán chạy xong, một cửa sổ giao diện sẽ hiện lên.
-Thao tác: Bấm nút "Next Matrix" trên giao diện để theo dõi sự di chuyển của ô trống qua từng bước. Phần hộp thoại bên dưới (Log) sẽ ghi nhận chi tiết hành động và thứ tự bước đi.