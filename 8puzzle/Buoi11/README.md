Chương trình này mô phỏng quá trình giải bài toán 8-Puzzle (Trò chơi xếp hình 8 ô vuông) trong Môi trường quan sát một phần (Partial Observable - Belief States) bằng giao diện trực quan.
Chương trình sẽ tự động tìm kiếm đường đi để đưa các ma trận trạng thái khởi tạo (Start States) về khớp với trạng thái đích (Goal States) và hiển thị hoạt ảnh từng bước di chuyển đồng thời.

CÁCH HOẠT ĐỘNG:
Môi trường: Gồm các ma trận 3x3 chứa các số từ 1 đến 8 và một ô trống (được đại diện bằng số 0). Trạng thái đích và khởi tạo có thể tùy biến với 4 mức độ quan sát:
- Hoàn toàn (1 Start - 1 Goal): Bài toán cơ bản.
- Start mù (2 Start - 1 Goal): Không chắc chắn về điểm bắt đầu.
- Goal mù (1 Start - 2 Goal): Không chắc chắn về mục tiêu.
- Cả 2 mù (2 Start - 2 Goal): Không chắc chắn về cả điểm bắt đầu lẫn mục tiêu.
Hành động: Ô trống (0) có thể di chuyển theo 4 hướng: Lên (UP), Xuống (DOWN), Trái (LEFT), Phải (RIGHT) để hoán đổi vị trí với các con số liền kề nó. *(Lưu ý: Trong belief states, nếu một ma trận trạng thái đã tới đích, nó sẽ đứng im trong khi các ma trận khác tiếp tục di chuyển).*
Thuật toán: Chương trình cung cấp các bộ não đằng sau để giải quyết:
- BFS Quét qua tất cả các trạng thái theo từng lớp. Đảm bảo luôn tìm được đường đi ngắn nhất.
- DFS Đi sâu vào một hướng cho đến khi chạm đáy nhánh thì mới quay lui. (Lưu ý: Thuật toán này có thể duyệt rất lâu với không gian trạng thái lớn).
- IDS Kết hợp ưu điểm của BFS và DFS, tăng dần độ sâu giới hạn (mặc định max_depth = 30) để tìm đường đi.
- Greedy Sử dụng hàm heuristic đánh giá khoảng cách Manhattan cho toàn bộ tập trạng thái. Thuật toán sẽ ưu tiên mở rộng các trạng thái có vẻ gần với đích nhất, giúp giải quyết bài toán nhanh chóng hơn.
- UCS Sử dụng hàm chi phí kết hợp giữa số bước đi (gn) và hàm đếm số lượng ô đang nằm sai vị trí cho toàn bộ tập trạng thái. Giúp cân bằng giữa hiệu suất thời gian và tối ưu đường đi.
- A* Sử dụng hàm chi phí kết hợp giữa số bước đi thực tế (gn) và hàm heuristic khoảng cách Manhattan (hn). Đây là thuật toán mạnh mẽ giúp đảm bảo tìm ra đường đi tối ưu nhất.
- IDA* (Iterative Deepening A*) Kết hợp ưu điểm của IDS và A*, sử dụng giới hạn chi phí (dựa trên hàm Manhattan) thay vì giới hạn độ sâu. Giúp tiết kiệm tối đa bộ nhớ trong khi vẫn đảm bảo đường đi tối ưu.
- Simple Hill Climbing Đánh giá lần lượt các trạng thái kề và di chuyển ngay lập tức tới trạng thái đầu tiên có hàm heuristic tốt hơn trạng thái hiện tại thay vì phải đánh giá toàn bộ.
- Steepest-Ascent Hill Climbing Đánh giá tất cả trạng thái kề và luôn chọn bước đi có hàm heuristic tốt nhất. (Lưu ý: Dễ bị mắc kẹt tại "đỉnh địa phương" và dừng sớm).
- Stochastic Hill Climbing Lựa chọn ngẫu nhiên một hướng đi và di chuyển ngay nếu nó tốt hơn trạng thái hiện tại. Cách này giúp tính toán nhanh hơn và có cơ hội lách qua điểm mắc kẹt.
- Random Restart Hill Climbing Khắc phục nhược điểm mắc kẹt ở đỉnh địa phương của Hill Climbing bằng cách tự động khởi động lại quá trình tìm kiếm từ đầu nhiều lần (tối đa 50 lần) cho đến khi tìm thấy trạng thái đích.
- Local Beam Search Lưu giữ K trạng thái tốt nhất tại mỗi bước duyệt thay vì chỉ 1 trạng thái. Thuật toán sẽ sinh ra tất cả các trạng thái kề từ K trạng thái này, lọc lại top K trạng thái có heuristic tốt nhất để đi tiếp, giúp tăng tỷ lệ tìm được đích và không bị kẹt.
- Simulated Annealing Khắc phục nhược điểm mắc kẹt ở đỉnh địa phương bằng cách cho phép di chuyển đến các trạng thái tệ hơn với một xác suất nhất định. Xác suất này phụ thuộc vào nhiệt độ (T) giảm dần theo thời gian, giúp thuật toán lách qua các điểm bế tắc ở giai đoạn đầu và hội tụ ở giai đoạn cuối.

Kết thúc: Chương trình dừng tính toán khi TẤT CẢ các ma trận hiện tại đều khớp với CÙNG MỘT trạng thái đích, sau đó xuất ra log các thao tác và tự động chạy hoạt ảnh (animation) trình diễn lại đường đi.

HƯỚNG DẪN SỬ DỤNG
Vì code đã được tích hợp thành một ứng dụng hoàn chỉnh bằng thư viện Flet, hãy thực hiện theo các bước sau:
B1. Chuẩn bị môi trường
Đảm bảo bạn đã cài đặt thư viện giao diện Flet trên máy bằng lệnh Terminal: pip install flet
B2. Khởi chạy chương trình
Chạy file mã nguồn Python. Giao diện "8-Puzzle Belief States Visualizer" sẽ hiện lên trên màn hình.
B3. Nhập dữ liệu đầu vào
- Chọn "Độ quan sát (Môi trường)" ở menu thả xuống đầu tiên. Giao diện sẽ tự động hiển thị số lượng ô nhập liệu Start/Goal tương ứng.
- Tại các ô Start/Goal, bạn cần nhập đúng 9 số (từ 0 đến 8, không trùng lặp), cách nhau bởi khoảng trắng. (Ví dụ: 1 2 3 4 0 6 7 5 8).
B4. Chọn thuật toán và Giải
- Tại mục "Thuật toán", mở menu thả xuống và chọn thuật toán bạn muốn chạy.
*(Lưu ý: Nếu chọn Local Beam Search, bạn có thể tùy chỉnh thông số "K". Nếu chọn Simulated Annealing, bạn có thể chỉnh thông số "T0", "Tmin", và "Alpha" ở các ô bên cạnh).*
- Nhấn nút "Bắt Đầu Trực Quan (Giải)" có biểu tượng Play.
B5. Quan sát quá trình và kết quả
Hệ thống sẽ thông báo "Đang tính toán..." ở cột Log bên phải.
Khi tìm ra đường đi, log sẽ in ra tổng số bước và chi tiết từng hành động. Đồng thời, các ma trận ở giữa màn hình sẽ tự động di chuyển các ô số mô phỏng lại y hệt quá trình giải bài toán (chạy song song cho toàn bộ belief states).