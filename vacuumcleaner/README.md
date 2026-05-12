Chương trình này mô phỏng một robot hút bụi hoạt động trên một sàn nhà có kích thước 5x5. 
Máy hút bụi (bắt đầu từ ô trên cùng bên trái (0,0)) sẽ tự động di chuyển ngẫu nhiên để tìm và dọn sạch các ô bị bẩn.

CÁCH HOẠT ĐỘNG:
  Môi trường: Một ma trận 5x5 chứa các giá trị 1 (Bẩn) và 0 (Sạch).
  Hành động: Nếu ô hiện tại Bẩn (1) thì máy sẽ dọn dẹp (chuyển thành 0).
  Nếu ô hiện tại Sạch (0) hoặc sau khi dọn thì máy sẽ chọn ngẫu nhiên một hướng (Lên, Xuống, Trái, Phải) hợp lệ để di chuyển tiếp.
  Kết thúc: Chương trình dừng lại khi toàn bộ sàn nhà đã sạch hoặc khi vượt quá 1000 bước đi.

HƯỚNG DẪN SỬ DỤNG
Vì code được chia làm 3 Cell, hãy thực hiện theo các bước sau:
  B1. Chạy Cell 1
    Khi chạy Cell này, chương trình sẽ yêu cầu bạn nhập dữ liệu đầu vào.
    Cách nhập: Bạn cần nhập 25 số (0 hoặc 1) cách nhau bởi dấu cách.
    Ví dụ: 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1
    Sau khi nhập, chương trình sẽ hiển thị ma trận sàn nhà dưới dạng lưới để bạn dễ quan sát.
  B2. Chạy Cell 2
    Chỉ cần run Cell này. Đây là nơi chứa các hàm của máy hút bụi:
      getRules: Kiểm tra xem vị trí máy để đưa ra các hướng đi hợp lệ.
      move: Cập nhật tọa độ mới cho máy (tức là máy di chuyển).
      isDirty: Kiểm tra xem trên toàn bộ sàn xem còn vết bẩn nào không.
  B3. Chạy Cell 3
    Nhấn Run để xem máy hút bụi bắt đầu làm việc.
    Mỗi khi máy hút bụi dọn một ô, ô đó sẽ được thông báo đã dọn và ma trận sàn mới sẽ được in.
    Cuối cùng, chương trình sẽ báo cáo tổng số bước đã đi để hoàn thành công việc hoặc khi vượt quá giới hạn.