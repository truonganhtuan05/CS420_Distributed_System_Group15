# KỊCH BẢN THUYẾT TRÌNH BÁO CÁO ĐỒ ÁN MÔN HỆ PHÂN TÁN (CS420G)
## ĐỀ TÀI: NGHIÊN CỨU KIẾN TRÚC PHÂN TÁN CỦA GITHUB VÀ TRIỂN KHAI TỰ ĐỘNG HÓA CI/CD VỚI GITHUB ACTIONS
* **Giảng viên hướng dẫn:** ThS. Nguyễn Minh Nhật
* **Nhóm thực hiện:** Nhóm 15 (CS420G)
* **Thành viên:** 
  1. Lê Văn Hoài Rin (MSSV: 29211434457) - Trưởng nhóm
  2. Nguyễn Trung Hiếu (MSSV: 29211441367)
  3. Trương Anh Tuấn (MSSV: 29211453666)
* **Tổng thời lượng dự kiến:** 20 - 25 phút trình bày + 10 phút hỏi đáp (Q&A)

---

## BẢNG PHÂN CHIA VAI TRÒ THUYẾT TRÌNH

| Thành viên | Slide phụ trách | Nội dung trọng tâm | Thời lượng |
| :--- | :--- | :--- | :---: |
| **Lê Văn Hoài Rin** (Trưởng nhóm) | Slide 1 – 7 | Mở đầu, Lý do chọn đề tài, Mục tiêu, So sánh SVN vs Git, Kiến trúc DAG & SHA, Thuật toán 3-Way Merge | ~8 phút |
| **Nguyễn Trung Hiếu** | Slide 8 – 11 | Hệ điều phối GitHub Actions (Master-Worker), Thiết kế bài toán Demo, Bảng Đầu vào/Đầu ra, Kiến trúc 4 tầng, Ma trận song song (Matrix) | ~7 phút |
| **Trương Anh Tuấn** | Slide 12 – 16 | Triển khai thực nghiệm: 5 Kịch bản (Đồng bộ, Xung đột ghi đồng thời, Matrix Testing, Ngắt mạch Fail-Fast, CD Artifacts), Bảng tổng hợp | ~8 phút |
| **Cả nhóm (Hoài Rin chốt)** | Slide 17 – 18 | Kết luận, Bài học kinh nghiệm môn Hệ phân tán, Lời cảm ơn và Phiên hỏi đáp (Q&A) | ~3 phút + Q&A |

---

## CHI TIẾT LỜI THOẠI & HƯỚNG DẪN TỪNG SLIDE

### SLIDE 1: TRANG BÌA (TITLE SLIDE)
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~1 phút
* **Mục tiêu:** Tạo phong thái đĩnh đạc, tự tin; nêu rõ định vị đề tài gắn liền môn Hệ phân tán.
* **Lời thoại gợi ý:**
  > "Kính chào Thầy Nguyễn Minh Nhật cùng toàn thể các bạn sinh viên lớp CS420G.  
  > Em tên là **Lê Văn Hoài Rin**, đại diện cho **Nhóm 15** gồm có em, bạn **Nguyễn Trung Hiếu** và bạn **Trương Anh Tuấn**.  
  > Hôm nay, nhóm chúng em xin được báo cáo đề tài Đồ án môn Hệ phân tán với tên gọi: **'Nghiên cứu kiến trúc phân tán của GitHub và Triển khai tự động hóa CI/CD với GitHub Actions'**.  
  > Mục tiêu lớn nhất của nhóm em không chỉ là sử dụng Git như một công cụ lập trình thông thường, mà là đi sâu giải phẫu cấu trúc dữ liệu đồ thị DAG, thuật toán hòa giải xung đột phân tán, và mô hình tính toán song song Master-Worker của GitHub Actions. Sau đây em xin phép được bắt đầu."

---

### SLIDE 2: NỘI DUNG TRÌNH BÀY (AGENDA)
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~45 giây
* **Mục tiêu:** Giúp Thầy và cả lớp nắm được mạch logic 5 phần của bài báo cáo.
* **Lời thoại gợi ý:**
  > "Bài thuyết trình của nhóm em được xây dựng bám sát theo quy chuẩn đồ án của Trường và định hướng của Thầy, gồm 5 phần chính:  
  > - **Phần 1: Mở đầu** – Khái quát vấn đề thực tế trong hệ phân tán và giải pháp Git/GitHub.  
  > - **Phần 2: Chương 1 - Cơ sở lý thuyết** – Phân tích cấu trúc DAG, tính bất biến Merkle và thuật toán 3-Way Merge.  
  > - **Phần 3: Chương 2 - Thiết kế hệ thống Demo** – Làm rõ bài toán cùng các tham số **Đầu vào (Input) và Đầu ra (Output)** theo đúng dặn dò của Thầy.  
  > - **Phần 4: Chương 3 - Triển khai thực nghiệm** – Báo cáo kết quả 5 kịch bản kiểm thử thực tế với hình ảnh minh chứng.  
  > - **Phần 5: Kết luận & Đánh giá** – Rút ra các bài học đắt giá trong môn Hệ phân tán."

---

### SLIDE 3: 1. LÝ DO CHỌN ĐỀ TÀI (VẤN ĐỀ VS GIẢI PHÁP)
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Chứng minh đề tài hoàn toàn thuộc về môn Hệ phân tán chứ không phải môn Công nghệ phần mềm.
* **Lời thoại gợi ý:**
  > "Kính thưa Thầy, khi nhiều kỹ sư phân tán cùng phát triển một hệ thống, họ đối mặt với 3 thách thức kinh điển:  
  > **Thứ nhất là Tranh chấp ghi đồng thời (Concurrent Write Conflict):** Hai node cùng sửa một vùng dữ liệu độc lập mà không biết về nhau;  
  > **Thứ hai là Điểm lỗi đơn (SPOF) ở các hệ thống tập trung:** Nếu máy chủ SVN bị mất mạng hay sập nguồn, toàn bộ kỹ sư đều phải dừng làm việc;  
  > **Thứ ba là Nút thắt cổ chai khi kiểm thử tuần tự:** Kiểm tra thủ công trên máy cá nhân gây trễ và dễ xung đột môi trường.  
  > Giải pháp từ Git và GitHub Actions mang lại tính phân tán hoàn hảo: Mỗi máy trạm là một **Bản sao đầy đủ (Full Replica)** giúp loại bỏ hoàn toàn SPOF; thuật toán **3-Way Merge** hòa giải xung đột không cần khóa tệp; và **GitHub Actions** điều phối các máy ảo Worker chạy kiểm thử song song tự động."
* **Từ khóa ăn điểm:** *SPOF, Concurrent Write, Full Replica, Non-blocking, 3-Way Merge.*

---

### SLIDE 4: 2. MỤC TIÊU VÀ PHẠM VI NGHIÊN CỨU
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~1 phút
* **Mục tiêu:** Xác lập rõ ranh giới nghiên cứu, tránh bị Thầy hỏi ngoài phạm vi.
* **Lời thoại gợi ý:**
  > "Về mục tiêu nghiên cứu, nhóm xác định rõ: Về mặt lý thuyết, phân tích cấu trúc DAG, hàm băm SHA, mô hình Master-Worker và cơ chế ngắt mạch (Circuit Breaker). Về mặt thực nghiệm, xây dựng hoàn chỉnh một REST API dịch vụ tính toán phân tán, thiết lập ma trận 3 Worker ảo song song trên GitHub Actions và giải quyết xung đột ghi đồng thời.  
  > Về phạm vi, nhóm tập trung vào Git CLI v2.x trên Windows 11 và các máy ảo Ubuntu Runner được cấp phát trên đám mây GitHub. Đề tài không khảo sát việc tự dựng GitHub Enterprise Server trên máy chủ vật lý riêng."

---

### SLIDE 5: 1.1. SỰ TIẾN HÓA TỪ CVCS SANG DVCS (SVN VS GIT)
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** So sánh chuyên sâu, làm nổi bật tính sẵn sàng cao và khả năng làm việc Offline-first của Git.
* **Lời thoại gợi ý:**
  > "Thưa Thầy, bảng so sánh này thể hiện rõ bước nhảy vọt từ kiến trúc tập trung sang kiến trúc phân tán:  
  > Ở hệ thống SVN, toàn bộ cơ sở dữ liệu lịch sử nằm độc nhất tại Server trung tâm. Máy trạm chỉ tải về một snapshot làm việc tạm thời. Mất mạng là tê liệt hoàn toàn.  
  > Trong khi đó, với Git, mỗi câu lệnh `clone` tạo ra một **Full Replica** chứa 100% lịch sử dự án. Mọi thao tác commit, tạo nhánh, duyệt log đều diễn ra trên đĩa cứng cục bộ với tốc độ cực nhanh và hỗ trợ **Offline 100%**. Tính phân tán này giúp hệ thống đạt độ sẵn sàng cao (High Availability) và không bao giờ có điểm lỗi đơn."
* **Từ khóa ăn điểm:** *Centralized vs Decentralized, Full Replica, High Availability, Offline-First.*

---

### SLIDE 6: 1.2. CẤU TRÚC DỮ LIỆU PHÂN TÁN: ĐỒ THỊ DAG & HÀM BĂM SHA
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~2 phút
* **Mục tiêu:** Điểm nhấn lý thuyết cao nhất: liên hệ cấu trúc Git với định lý quan hệ nhân quả (Causal Ordering) của Lamport.
* **Lời thoại gợi ý:**
  > "Kính thưa Thầy, đây là slide lý thuyết cốt lõi nhất. Hai trụ cột toán học giúp Git vận hành phân tán an toàn gồm:  
  > **Thứ nhất là Cơ chế lưu trữ theo nội dung (Content-Addressable Storage):** Mọi đối tượng (Blob, Tree, Commit) đều được hash SHA-1 hoặc SHA-256 dựa trên nội dung và hash cha. Cơ chế này giống hệt **Merkle Tree trong Blockchain**, đảm bảo tính bất biến (Immutability). Dù truyền qua mạng không an toàn, không ai có thể sửa đổi dữ liệu quá khứ mà không bị phát hiện ngay lập tức.  
  > **Thứ hai là Đồ thị phi chu trình có hướng (DAG):** Trong hệ phân tán, không có đồng hồ vật lý đồng bộ tuyệt đối. Git sử dụng **Quan hệ nhân quả (Causal Ordering)** tương tự như **Lamport Logical Clocks** mà Thầy đã giảng dạy. Dựa vào con trỏ cha-con trong đồ thị DAG, Git xác định chính xác sự kiện nào xảy ra trước, sự kiện nào xảy ra sau, và khi nào hai sự kiện xảy ra đồng thời."
* **Từ khóa ăn điểm:** *Content-Addressable Storage, Merkle Tree, Immutability, Directed Acyclic Graph (DAG), Lamport Logical Clocks, Causal Ordering.*

---

### SLIDE 7: 1.3. THUẬT TOÁN HÒA GIẢI XUNG ĐỘT 3-WAY MERGE
* **Người trình bày:** Lê Văn Hoài Rin (chuyển giao cho Hiếu)
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Giải thích cơ chế 3 điểm nút và chuyển lời cho bạn Nguyễn Trung Hiếu.
* **Lời thoại gợi ý:**
  > "Vậy khi hai node phân tán cùng cập nhật dữ liệu thì Git xử lý ra sao? Git không dùng cơ chế khóa (Non-blocking) mà sử dụng thuật toán **3-Way Merge** dựa trên 3 điểm nút:  
  > Điểm 1 là **Base Commit (B)** – tổ tiên chung gần nhất trên đồ thị DAG;  
  > Điểm 2 và 3 là trạng thái hiện tại của **Node A** và **Node B**.  
  > Nếu Node A sửa dòng 10, Node B sửa dòng 50: Git tự động gộp sạch sẽ.  
  > Nếu cả A và B cùng sửa dòng 10: Git chèn **Conflict Markers** để con người hòa giải.  
  > Tiếp theo đây, em xin mời bạn **Nguyễn Trung Hiếu** trình bày về hệ điều phối tác vụ phân tán của GitHub Actions."
* **Từ khóa ăn điểm:** *3-Way Merge, Common Ancestor, Conflict Markers, Non-blocking.*

---

### SLIDE 8: 1.4. ĐIỀU PHỐI TÁC VỤ PHÂN TÁN VỚI GITHUB ACTIONS
* **Người trình bày:** Nguyễn Trung Hiếu
* **Thời lượng:** ~2 phút
* **Mục tiêu:** Khẳng định GitHub Actions là mô hình phân tán Master-Worker chuẩn mực.
* **Lời thoại gợi ý:**
  > "Kính chào Thầy và các bạn, em là **Nguyễn Trung Hiếu**. Em xin tiếp tục phần báo cáo với tầng tính toán phân tán của GitHub Actions.  
  > GitHub Actions hoạt động theo mô hình **Master-Worker** chuẩn mực:  
  > - **Master Coordinator (GitHub Cloud):** Hoạt động theo kiến trúc hướng sự kiện (Event-Driven). Khi nhận được push event, Master phân tích file workflow YAML và lập lịch điều phối tác vụ.  
  > - **Distributed Workers (Runners):** Là các máy ảo độc lập tạm thời (Ephemeral Virtual Machines) chạy trên nền tảng đám mây Azure. Mỗi worker nhận chỉ thị, tải mã nguồn, chạy kiểm thử song song độc lập, truyền luồng nhật ký real-time về Master và tự động hủy sau khi hoàn tất, đảm bảo cô lập tài nguyên tuyệt đối."
* **Từ khóa ăn điểm:** *Master-Worker Architecture, Event-Driven, Ephemeral Virtual Machines, Task Dispatching, Resource Isolation.*

---

### SLIDE 9: 2.1. BÀI TOÁN DEMO VÀ THAM SỐ ĐẦU VÀO / ĐẦU RA
* **Người trình bày:** Nguyễn Trung Hiếu
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Trả lời trực tiếp yêu cầu dặn dò của Giảng viên về Đầu vào và Đầu ra.
* **Lời thoại gợi ý:**
  > "Kính thưa Thầy, thực hiện đúng dặn dò của Thầy trên nhóm lớp về việc làm rõ bài toán và tham số, nhóm em đã chuẩn hóa như sau:  
  > **Bài toán Demo:** Xây dựng một dịch vụ tính toán phân tán Stateless REST API kết hợp chuỗi cung ứng CI/CD khép kín.  
  > **Tham số Đầu vào (Inputs):**  
  > 1. Mã nguồn Python lõi nghiệp vụ toán học (`calculator.py`) và HTTP Server (`server.py`);  
  > 2. Bộ 7 ca kiểm thử tự động pytest;  
  > 3. Tệp đặc tả workflow điều phối phân tán `ci-cd.yml`;  
  > 4. Các commit đồng thời từ Node A và Node B tạo xung đột.  
  > **Tham số Đầu ra (Outputs):**  
  > 1. Đồ thị Git DAG hòa giải xung đột thành công;  
  > 2. Nhật ký thực thi song song của 3 máy ảo Worker (Python 3.10, 3.11, 3.12);  
  > 3. Phản hồi ngắt mạch Fail-Fast bảo vệ hệ thống;  
  > 4. Gói lưu trữ phần mềm Artifacts sẵn sàng phát hành."
* **Từ khóa ăn điểm:** *Stateless REST API, Inputs/Outputs, Automated Pytest, Ephemeral Artifacts.*

---

### SLIDE 10: 2.2. MÔ HÌNH KIẾN TRÚC 4 TẦNG HỆ THỐNG DEMO
* **Người trình bày:** Nguyễn Trung Hiếu
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Giới thiệu cấu trúc phân tầng rõ ràng, thể hiện sự am hiểu kiến trúc.
* **Lời thoại gợi ý:**
  > "Thưa Thầy, hệ thống được nhóm cấu trúc thành 4 tầng rõ rệt:  
  > - **Tầng 1 - Các Node máy trạm (Replicas):** Nơi các kỹ sư (Dev Rin, Dev Hiếu) làm việc độc lập trên local Git DAG;  
  > - **Tầng 2 - Remote Coordination Hub:** GitHub Central Repo tiếp nhận push, kiểm soát xung đột và kích hoạt webhook;  
  > - **Tầng 3 - Cụm Worker Runners:** 3 máy ảo Ubuntu chạy song song ma trận kiểm thử;  
  > - **Tầng 4 - Tầng bàn giao & triển khai (CD Target):** Tự động đóng gói Artifact nén và mô phỏng deploy ra môi trường live."
* **Từ khóa ăn điểm:** *Kiến trúc 4 tầng, Replica Nodes, Coordination Hub, Continuous Delivery.*

---

### SLIDE 11: 2.3. CẤU HÌNH ĐIỀU PHỐI VÀ MA TRẬN SONG SONG (MATRIX)
* **Người trình bày:** Nguyễn Trung Hiếu (chuyển giao cho Tuấn)
* **Thời lượng:** ~2 phút
* **Mục tiêu:** Phân tích đoạn mã YAML điều phối phân tán và chuyển lời cho bạn Trương Anh Tuấn.
* **Lời thoại gợi ý:**
  > "Về cấu hình kỹ thuật, đây là đoạn mã YAML quan trọng nhất trong file `ci-cd.yml`:  
  > Nhóm sử dụng từ khóa `needs: code-quality` để thiết lập thứ tự nhân quả. Khi kiểm tra cú pháp đạt, chỉ thị `strategy: matrix` kích hoạt tính toán phân tán: GitHub Master tự động nhân bản và cấp phát đồng thời 3 máy ảo Ubuntu độc lập chạy Python 3.10, 3.11 và 3.12.  
  > Thuộc tính `fail-fast: false` giúp chúng em khảo sát độc lập từng node môi trường. Nhờ chạy song song, thời gian kiểm thử được rút ngắn 60% so với chạy tuần tự.  
  > Sau đây, em xin mời bạn **Trương Anh Tuấn** báo cáo chi tiết kết quả thực nghiệm 5 kịch bản kiểm thử."
* **Từ khóa ăn điểm:** *Strategy Matrix, Parallel Instances, Fail-fast, YAML Workflow Spec.*

---

### SLIDE 12: 3.1. KỊCH BẢN 1: ĐỒNG BỘ DỮ LIỆU PHÂN TÁN LÊN REMOTE HUB
* **Người trình bày:** Trương Anh Tuấn
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Báo cáo kịch bản 1, chỉ rõ bằng chứng thực tế trên ảnh chụp màn hình.
* **Lời thoại gợi ý:**
  > "Kính thưa Thầy và các bạn, em là **Trương Anh Tuấn**. Em xin phép báo cáo kết quả thực nghiệm 5 kịch bản kiểm thử trên hệ thống thực tế.  
  > Ở **Kịch bản 1**: Nhóm tiến hành khởi tạo kho lưu trữ phân tán và thực hiện lệnh `git push` lên GitHub Remote Hub.  
  > Như Thầy có thể quan sát trên ảnh chụp màn hình terminal bên phải: Toàn bộ đối tượng nén được truyền tải an toàn qua giao thức HTTPS. GitHub xác nhận nhận đủ dữ liệu và ngay lập tức gửi tín hiệu Webhook để kích hoạt chuỗi CI/CD Pipeline."
* **Từ khóa ăn điểm:** *Git Push, HTTPS Protocol, Webhook Trigger, Remote Hub Synchronization.*

---

### SLIDE 13: 3.2. KỊCH BẢN 2: XUNG ĐỘT ĐỒNG THỜI & HÒA GIẢI (MERGE CONFLICT)
* **Người trình bày:** Trương Anh Tuấn
* **Thời lượng:** ~2 phút
* **Mục tiêu:** Điểm nhấn thực nghiệm lớn nhất: giải thích kịch bản xung đột bằng script PowerShell và ảnh conflict markers.
* **Lời thoại gợi ý:**
  > "Kịch bản 2 là phép thử quan trọng nhất về tính toàn vẹn trạng thái phân tán. Chúng em sử dụng script `simulate_conflict.ps1` để tái hiện tình huống:  
  > Dev Rin sửa hàm add thành số thực float; Dev Hiếu sửa hàm add thành làm tròn 4 chữ số thập phân trên hai nhánh rẽ riêng biệt.  
  > Khi gộp nhánh thứ hai vào main, Git lập tức phát hiện xung đột và từ chối tự động ghi đè. Thông báo `CONFLICT (content)` xuất hiện trên terminal như ảnh chụp bên phải.  
  > Các ký hiệu Conflict Markers xuất hiện rõ ràng trong file `calculator.py`. Hai kỹ sư tiến hành họp bàn, thống nhất giữ logic chung và tạo ra Merge Commit, đưa hệ thống về trạng thái đồng thuận phân tán."
* **Từ khóa ăn điểm:** *Conflict (content), Conflict Markers, Consensus, Merge Commit.*

---

### SLIDE 14: 3.3. KỊCH BẢN 3: TÍNH TOÁN SONG SONG TRÊN 3 WORKER RUNNERS
* **Người trình bày:** Trương Anh Tuấn
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Nhấn mạnh số liệu thực tế: 3 máy ảo chạy đồng thời, tổng thời gian ~18 giây, giảm 60% so với chạy tuần tự.
* **Lời thoại gợi ý:**
  > "Kịch bản 3 minh chứng tính toán song song phân tán (Parallel Distributed Execution):  
  > Như trên hình ảnh minh chứng tab Actions: Hệ thống đã khởi tạo 3 Worker độc lập trên 3 phiên bản Python 3.10, 3.11 và 3.12.  
  > Mỗi máy ảo sở hữu Hostname riêng biệt, chạy độc lập 7 bài unit test và đều đạt 100% pass.  
  > Điều đáng chú ý là thay vì mất gần 50 giây nếu chạy tuần tự, tổng thời gian kiểm thử chỉ mất 18 giây - tương đương với thời gian của worker chạy chậm nhất. Điều này chứng minh hiệu quả tối ưu hóa tài nguyên phân tán."
* **Từ khóa ăn điểm:** *Parallel Execution, Independent Hostnames, Latency Optimization, Matrix Results.*

---

### SLIDE 15: 3.4. KỊCH BẢN 4: PHÁT HIỆN LỖI VÀ NGẮT MẠCH (FAIL-FAST)
* **Người trình bày:** Trương Anh Tuấn
* **Thời lượng:** ~2 phút
* **Mục tiêu:** Chứng minh cơ chế chịu lỗi và an toàn hệ thống (Fault Tolerance & Safety).
* **Lời thoại gợi ý:**
  > "Kịch bản 4 là phép thử về khả năng chịu lỗi và tự bảo vệ của hệ thống: Nếu một node commit code lỗi thì điều gì xảy ra?  
  > Chúng em cố tình sửa một assert sai logic trong unit test (10 + 20 == 999). Ngay lập tức, Worker phát hiện và trả về mã lỗi. Giao diện GitHub Actions đổi sang **MÀU ĐỎ** như Thầy thấy trên màn hình.  
  > Đặc biệt, cơ chế **Ngắt mạch (Circuit Breaker)** dựa trên quan hệ phụ thuộc `needs` lập tức **HỦY BỎ hoàn toàn** các Job Build và Deploy tiếp theo. Pull Request bị khóa, ngăn chặn mã lỗi phát tán sang các máy chủ khác."
* **Từ khóa ăn điểm:** *Circuit Breaker Pattern, Fail-Fast, Cascading Failure Prevention, Red Pipeline.*

---

### SLIDE 16: 3.5. BẢNG TỔNG HỢP KẾT QUẢ CÁC PHÉP THỬ
* **Người trình bày:** Trương Anh Tuấn (chuyển giao cho Hoài Rin)
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Tổng kết kết quả thực nghiệm một cách tự tin, khẳng định độ tin cậy của bài làm.
* **Lời thoại gợi ý:**
  > "Kính thưa Thầy, bảng trên đây tổng hợp toàn bộ 5 phép thử thực nghiệm mà nhóm đã tiến hành.  
  > Cả 5/5 kịch bản đều đạt kết quả xuất sắc, phản ánh trung thực nguyên lý của hệ phân tán: từ tính bất biến dữ liệu, giải quyết tranh chấp ghi, đến tính toán song song và khả năng chịu lỗi.  
  > Sau đây, em xin kính mời bạn **Lê Văn Hoài Rin**, trưởng nhóm, phát biểu phần Kết luận và bài học kinh nghiệm."
* **Từ khóa ăn điểm:** *Bảng tổng hợp thực nghiệm, Đạt 100%, Tính thực chứng khoa học.*

---

### SLIDE 17: KẾT LUẬN VÀ BÀI HỌC KINH NGHIỆM TRONG MÔN HỆ PHÂN TÁN
* **Người trình bày:** Lê Văn Hoài Rin
* **Thời lượng:** ~1.5 phút
* **Mục tiêu:** Chốt lại ý nghĩa học thuật môn Hệ phân tán, khẳng định giá trị đề tài.
* **Lời thoại gợi ý:**
  > "Kính thưa Thầy và các bạn, qua quá trình nghiên cứu và thực hiện đề tài, Nhóm 15 rút ra 3 bài học lớn gắn liền với môn Hệ phân tán:  
  > **Bài học 1:** Mô hình Bản sao đầy đủ (Full Replica) là giải pháp tối ưu để triệt tiêu hoàn toàn điểm lỗi đơn SPOF và bảo đảm tính sẵn sàng cao;  
  > **Bài học 2:** Tranh chấp ghi đồng thời là điều tất yếu trong môi trường phân tán; việc hiểu rõ cấu trúc DAG và quan hệ nhân quả giúp chúng ta thiết kế giải pháp hòa giải an toàn;  
  > **Bài học 3:** Cơ chế ngắt mạch (Circuit Breaker) là nguyên tắc sống còn để bảo vệ hệ sinh thái phân tán khỏi lỗi lan truyền (Cascading Failures)."
* **Từ khóa ăn điểm:** *Full Replica, Cascading Failures, Circuit Breaker, Causal Ordering.*

---

### SLIDE 18: LỜI CẢM ƠN VÀ PHIÊN HỎI ĐÁP (Q&A)
* **Người trình bày:** Cả nhóm 15
* **Thời lượng:** ~5 - 10 phút
* **Mục tiêu:** Phong thái khiêm tốn, cầu thị, sẵn sàng phản biện câu hỏi của Thầy.
* **Lời thoại gợi ý:**
  > "Nhóm 15 xin chân thành cảm ơn Thầy Nguyễn Minh Nhật và toàn thể các bạn sinh viên đã chú ý lắng nghe bài báo cáo của nhóm chúng em.  
  > Sau đây, nhóm chúng em rất mong nhận được những nhận xét, góp ý và câu hỏi phản biện từ Thầy và các bạn để nhóm làm rõ hơn các vấn đề học thuật của đề tài. Nhóm em xin chân thành cảm ơn!"

---

## BỘ CÂU HỎI VẤN ĐÁP (Q&A) DỰ ĐOÁN TỪ GIẢNG VIÊN & CÂU TRẢ LỜI MẪU

### Câu hỏi 1 của GV: *"Tại sao Git lại gọi là Hệ thống Phân tán (DVCS) trong khi hầu hết các nhóm vẫn push code lên một Server GitHub trung tâm?"*
* **Câu trả lời chuẩn:**  
  > "Thưa Thầy, GitHub chỉ đóng vai trò là một **Remote Hub tiện ích** để hỗ trợ cộng tác, chứ không phải là điều kiện tiên quyết để Git hoạt động.  
  > Về mặt bản chất: Mỗi máy trạm của sinh viên là một node Git hoàn chỉnh, chứa toàn bộ cơ sở dữ liệu lịch sử đối tượng (Full Replica). Hai lập trình viên hoàn toàn có thể kết nối mạng LAN ngang hàng (P2P) qua SSH hoặc dùng file `git bundle` để truyền commit trực tiếp cho nhau mà không cần Internet hay GitHub. Nếu máy chủ GitHub bị sập hoàn toàn, bất kỳ máy trạm nào cũng có thể đóng vai trò làm Server phục hồi lại toàn bộ hệ thống."

### Câu hỏi 2 của GV: *"Git phát hiện xung đột (Merge Conflict) dựa vào cơ chế gì? Có phải là dựa vào thời gian (Timestamp) của commit không?"*
* **Câu trả lời chuẩn:**  
  > "Thưa Thầy, Git **không** dựa vào Timestamp vật lý để phát hiện xung đột, vì trong hệ phân tán, đồng hồ giữa các máy tính luôn có độ lệch (Clock Drift).  
  > Thay vào đó, Git dựa vào **Đồ thị DAG và Quan hệ nhân quả (Causal Ordering)** để tìm **Tổ tiên chung gần nhất (Common Ancestor - Base Commit)** thông qua thuật toán 3-Way Merge. Git so sánh sự biến đổi của Node A so với Base, và Node B so với Base. Nếu cả hai node cùng thay đổi một vùng dòng code nhưng nội dung khác nhau, Git xác định đây là xung đột đồng thời độc lập và yêu cầu hòa giải."

### Câu hỏi 3 của GV: *"Trong GitHub Actions, các Worker Runners chia sẻ tài nguyên với nhau như thế nào? Dữ liệu giữa các Job truyền qua đâu?"*
* **Câu trả lời chuẩn:**  
  > "Thưa Thầy, các Worker Runners trong GitHub Actions **hoàn toàn cô lập và không chia sẻ bộ nhớ hay ổ đĩa trực tiếp** với nhau (Shared-Nothing Architecture). Mỗi Runner là một máy ảo Ubuntu riêng biệt.  
  > Để truyền dữ liệu giữa các Job phụ thuộc (ví dụ từ Job Build sang Job Deploy), hệ thống sử dụng cơ chế **Artifact Storage**: Job trước đóng gói dữ liệu và upload lên kho lưu trữ đám mây của GitHub (qua action `upload-artifact`), sau đó Job sau sẽ tải về (qua action `download-artifact`)."
