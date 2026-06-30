Chương trình này mô phỏng quá trình giải bài toán Thỏa mãn ràng buộc (Constraint Satisfaction Problem - CSP) bằng giao diện trực quan sử dụng thư viện Flet.
Chương trình sẽ tự động tìm kiếm nghiệm để điền các giá trị vào 9 biến (ô) sao cho thỏa mãn tất cả các ràng buộc toán học, đồng thời hiển thị hoạt ảnh từng bước suy luận, tính toán và cắt tỉa của thuật toán.

CÁCH HOẠT ĐỘNG:
Môi trường: Gồm một lưới 3x3 chứa 9 ô vuông (từ Ô 0 đến Ô 8). Cần điền các giá trị vào 9 ô này sao cho thỏa mãn bộ 3 ràng buộc sau:
- Ràng buộc AllDiff: Các giá trị trong 9 ô phải hoàn toàn khác nhau.
- Ràng buộc tăng dần: Ô trước phải nhỏ hơn ô sau (Ô i < Ô i+1 với i < 7).
- Ràng buộc Ô 8: Giá trị của Ô 8 phải nhỏ hơn tất cả các ô còn lại (i < 8).

Thuật toán: Chương trình cung cấp hai bộ não đằng sau để giải quyết:
- Min-Conflicts: Giải quyết theo hướng tìm kiếm cục bộ. Khởi tạo ngẫu nhiên các giá trị, sau đó liên tục chọn các ô đang vi phạm ràng buộc và đổi nó sang một giá trị mới sao cho số lượng xung đột là ít nhất. Tích hợp cơ chế Random Restart (Khởi động lại ngẫu nhiên) để không bị kẹt ở cực tiểu cục bộ.
- AC-3 (Arc Consistency 3): Giải quyết theo hướng thu gọn miền giá trị (Domain). Thuật toán lan truyền các ràng buộc qua các cung (arcs), liên tục kiểm tra và cắt tỉa những giá trị sai luật ra khỏi tập hợp giá trị khả dĩ của mỗi ô, cho đến khi mỗi ô bị ép về đúng 1 nghiệm duy nhất.

HƯỚNG DẪN SỬ DỤNG
Vì code đã được tích hợp thành một ứng dụng hoàn chỉnh bằng thư viện Flet, hãy thực hiện theo các bước sau:
B1. Chuẩn bị môi trường
Đảm bảo bạn đã cài đặt thư viện giao diện Flet trên máy bằng lệnh Terminal: pip install flet
B2. Khởi chạy chương trình
Chạy file mã nguồn Python. Giao diện "CSP Visualizer (AC-3 & Min-Conflicts)" sẽ hiện lên trên màn hình.

<img width="1918" height="1017" alt="image" src="https://github.com/user-attachments/assets/c4e02557-e6c5-4868-b3a8-496c8083a589" />

B3. Lựa chọn thuật toán
- Tại mục "Thuật toán", mở menu thả xuống và chọn thuật toán bạn muốn chạy (Min-Conflicts hoặc AC-3).
- 
<img width="285" height="222" alt="image" src="https://github.com/user-attachments/assets/374d1168-589d-4344-881b-c3e03cb26bde" />

B4. Cài đặt tốc độ
- Chọn "Tốc độ hiển thị" ở menu thả xuống tiếp theo (Nhanh, Bình thường, hoặc Chậm) để tiện theo dõi hoạt ảnh.

<img width="211" height="276" alt="image" src="https://github.com/user-attachments/assets/734b9bf7-f8d7-498b-b563-463e84ced672" />

B5. Bắt đầu Giải
- Nhấn nút "Bắt Đầu Trực Quan" có biểu tượng Play.

<img width="256" height="65" alt="image" src="https://github.com/user-attachments/assets/66736ced-9150-4578-be2f-93a3509498df" />

- Chương trình sẽ hiển thị trực tiếp quá trình biến đổi các ô số trên lưới 3x3 ở bên trái, đồng thời xuất ra log các thao tác tính toán chi tiết ở bảng "Nhật ký thực thi" bên phải.

<img width="1918" height="1012" alt="image" src="https://github.com/user-attachments/assets/71c31b91-04eb-4cb9-bbab-3bb8df294c5a" />

<img width="1918" height="1012" alt="image" src="https://github.com/user-attachments/assets/39914005-12f0-4e31-b969-254b57fcf9c5" />

<img width="1918" height="1011" alt="image" src="https://github.com/user-attachments/assets/ae7b850a-c02e-4ff2-877e-eea38a1b69fc" />
