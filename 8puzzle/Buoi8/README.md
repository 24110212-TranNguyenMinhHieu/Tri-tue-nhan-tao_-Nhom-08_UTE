Chương trình này mô phỏng quá trình giải bài toán 8-Puzzle (Trò chơi xếp hình 8 ô vuông) bằng giao diện trực quan.
Chương trình sẽ tự động tìm kiếm đường đi để đưa một ma trận bị xáo trộn về trạng thái đích (đã sắp xếp) và hiển thị hoạt ảnh từng bước di chuyển.

CÁCH HOẠT ĐỘNG:
Môi trường: Một ma trận 3x3 chứa các số từ 1 đến 8 và một ô trống (được đại diện bằng số 0). Trạng thái đích luôn là:
1 2 3
4 5 6
7 8 0
Hành động: Ô trống (0) có thể di chuyển theo 4 hướng: Lên (UP), Xuống (DOWN), Trái (LEFT), Phải (RIGHT) để hoán đổi vị trí với các con số liền kề nó (nếu hợp lệ).
Thuật toán: Chương trình cung cấp các bộ não đằng sau để giải quyết:
- BFS Quét qua tất cả các trạng thái theo từng lớp. Đảm bảo luôn tìm được đường đi ngắn nhất.
- DFS Đi sâu vào một hướng cho đến khi chạm đáy nhánh thì mới quay lui. (Lưu ý: Thuật toán này có thể duyệt rất lâu với không gian trạng thái lớn).
- IDS Kết hợp ưu điểm của BFS và DFS, tăng dần độ sâu giới hạn (mặc định max_depth = 30) để tìm đường đi.
- Greedy Sử dụng hàm heuristic đánh giá khoảng cách Manhattan (tổng khoảng cách từ vị trí hiện tại của các ô số đến vị trí đích). Thuật toán sẽ ưu tiên mở rộng các trạng thái có vẻ gần với đích nhất, giúp giải quyết bài toán nhanh chóng hơn.
- UCS Sử dụng hàm chi phí kết hợp giữa số bước đi (gn) và hàm heuristic đếm số lượng ô đang nằm sai vị trí (Misplaced tiles). Phương pháp này giúp cân bằng giữa hiệu suất thời gian và việc tìm ra đường đi tối ưu.
- A* Sử dụng hàm chi phí kết hợp giữa số bước đi thực tế (gn) và hàm heuristic khoảng cách Manhattan (hn). Đây là thuật toán mạnh mẽ giúp đảm bảo tìm ra đường đi tối ưu nhất một cách hiệu quả.
- IDA* (Iterative Deepening A*) Kết hợp ưu điểm của IDS và A*, sử dụng giới hạn chi phí (dựa trên hàm Manhattan) thay vì giới hạn độ sâu như IDS thông thường. Thuật toán này giúp tiết kiệm tối đa bộ nhớ trong khi vẫn đảm bảo tìm được đường đi tối ưu.

Kết thúc: Chương trình dừng tính toán khi ma trận khớp với trạng thái đích, sau đó xuất ra log các thao tác và tự động chạy hoạt ảnh (animation) trình diễn lại đường đi.

HƯỚNG DẪN SỬ DỤNG
Vì code đã được tích hợp thành một ứng dụng hoàn chỉnh bằng thư viện Flet, hãy thực hiện theo các bước sau:
B1. Chuẩn bị môi trường
Đảm bảo bạn đã cài đặt thư viện giao diện Flet trên máy bằng lệnh Terminal: pip install flet
B2. Khởi chạy chương trình
Chạy file mã nguồn Python (chứa UI và thuật toán). Giao diện "8-Puzzle Multi-Algorithm Visualizer" sẽ hiện lên trên màn hình.
B3. Nhập dữ liệu đầu vào
Tại ô "Nhập ma trận", bạn cần nhập đúng 9 số (từ 0 đến 8, không trùng lặp), cách nhau bởi khoảng trắng.
Ví dụ: 1 2 3 4 0 6 7 5 8
Trạng thái khởi tạo sẽ ngay lập tức được vẽ lên lưới ma trận trên màn hình.
B4. Chọn thuật toán và Giải
Tại mục "Thuật toán", mở menu thả xuống và chọn thuật toán bạn muốn chạy (BFS, DFS, IDS, Greedy, UCS, A*, hoặc IDA*).
Nhấn nút "Giải" (biểu tượng Play).
B5. Quan sát quá trình và kết quả
Hệ thống sẽ thông báo "Đang tính toán..." ở cột Log bên phải.
Khi tìm ra đường đi, log sẽ in ra tổng số bước và chi tiết từng hành động. Đồng thời, ma trận ở giữa màn hình sẽ tự động di chuyển các ô số mô phỏng lại y hệt quá trình giải bài toán.