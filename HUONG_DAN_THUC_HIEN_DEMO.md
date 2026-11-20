# HƯỚNG DẪN THỰC HÀNH VÀ CHỤP ẢNH MINH CHỨNG ĐỒ ÁN
## MÔN: HỆ PHÂN TÁN (CS420G) - NHÓM 15
**Đề tài:** Nghiên cứu kiến trúc phân tán của GitHub và Triển khai tự động hóa CI/CD với GitHub Actions

---

### BƯỚC 1: KHỞI TẠO VÀ ĐẨY DỰ ÁN LÊN GITHUB
1. Đăng nhập vào [GitHub](https://github.com) của một bạn trong nhóm.
2. Tạo một Repository mới với tên: `CS420_Distributed_System_Group15` (chọn Public).
3. Mở PowerShell tại thư mục này (`d:\HocKyI_Nam4\CS_420_G\DA_HePhanTan_ver4`) và chạy các lệnh:
   ```powershell
   git init
   git add .
   git commit -m "feat: Khoi tao kien truc phan tan va workflow CI/CD"
   git branch -M main
   git remote add origin https://github.com/<tai-khoan-cua-ban>/CS420_Distributed_System_Group15.git
   git push -u origin main
   ```
4. **CHỤP ẢNH 1:** Chụp màn hình terminal sau khi chạy `git push` thành công và trang chủ GitHub hiển thị mã nguồn. *(Dán vào Mục 3.2 của Báo cáo)*.

---

### BƯỚC 2: QUAN SÁT TÍNH TOÁN SONG SONG TRÊN GITHUB ACTIONS (MATRIX RUNNERS)
1. Trên trang GitHub Repository, bấm vào tab **Actions**.
2. Bạn sẽ thấy workflow `CS420 Distributed CI-CD Pipeline` đang chạy tự động.
3. Bấm vào chi tiết run đó, bạn sẽ thấy 4 Job:
   - `🔍 Static Analysis & Lint`
   - `🧪 Test Node (Python 3.10)`, `🧪 Test Node (Python 3.11)`, `🧪 Test Node (Python 3.12)` (3 máy ảo Worker chạy song song cùng lúc!)
   - `📦 Build & Containerization`
   - `🚀 Continuous Deployment Simulation`
4. **CHỤP ẢNH 2:** Chụp đồ thị các Job của workflow xanh hoàn toàn (Success) hiển thị cả 3 Worker Python 3.10, 3.11, 3.12. *(Dán vào Mục 3.4 của Báo cáo)*.
5. **CHỤP ẢNH 3:** Bấm vào một Job Test, mở mục `Thu thập thông tin Worker Node` để chụp lại thông tin Hostname, OS ảo, Commit SHA. *(Dán vào Mục 3.4 của Báo cáo)*.

---

### BƯỚC 3: MÔ PHỎNG CƠ CHẾ CHỊU LỖI & NGĂN CHẶN LỖI (FAIL-FAST / RED PIPELINE)
1. Mở file `tests/test_calculator.py`. Sửa dòng test đầu tiên:
   ```python
   assert DistributedCalculator.add(10, 20) == 999  # Cố tình sửa sai logic
   ```
2. Commit và đẩy lên GitHub:
   ```powershell
   git add tests/test_calculator.py
   git commit -m "fix(test): Co tinh tao loi de kiem thu co che Fail-Fast"
   git push origin main
   ```
3. Vào tab **Actions** trên GitHub, bạn sẽ thấy Runner phát hiện lỗi và báo **MÀU ĐỎ (Failed)**. Các job Build và Deploy phía sau bị **HỦY/CHẶN NGAY LẬP TỨC**.
4. **CHỤP ẢNH 4:** Chụp màn hình Pipeline báo ĐỎ và log chi tiết lỗi của pytest. *(Dán vào Mục 3.5 của Báo cáo)*.
5. Sửa lại giá trị đúng `== 30` rồi commit, push lại để pipeline xanh trở lại.

---

### BƯỚC 4: THỰC HIỆN KỊCH BẢN XUNG ĐỘT GHI ĐỒNG THỜI (MERGE CONFLICT)
1. Chạy file script đã được chuẩn bị sẵn:
   ```powershell
   .\simulate_conflict.ps1
   ```
2. Terminal sẽ tự động tạo 2 nhánh `feature-node-a` và `feature-node-b`, mô phỏng 2 thành viên sửa cùng dòng code và kích hoạt xung đột.
3. **CHỤP ẢNH 5:** Chụp màn hình terminal báo `CONFLICT (content): Merge conflict in app/calculator.py`. *(Dán vào Mục 3.3 của Báo cáo)*.
4. Mở file `app/calculator.py` trong VS Code để thấy các dấu `<<<<<<< HEAD`, `=======`, `>>>>>>> feature-node-b`.
5. **CHỤP ẢNH 6:** Chụp màn hình VS Code hiển thị vùng xung đột trực quan. *(Dán vào Mục 3.3 của Báo cáo)*.
6. Sau khi chụp xong, gõ lệnh sau để khôi phục trạng thái sạch:
   ```powershell
   git merge --abort
   git checkout main
   ```

---

### BƯỚC 5: TẢI GÓI PHÁT HÀNH (ARTIFACT DEPLOYMENT)
1. Tại tab **Actions** trên GitHub, bấm vào lượt chạy thành công ở Bước 2.
2. Cuộn xuống cuối trang phần **Artifacts**, bạn sẽ thấy file nén `distributed-app-package`.
3. **CHỤP ẢNH 7:** Chụp màn hình mục Artifacts này. *(Dán vào Mục 3.6 của Báo cáo)*.
