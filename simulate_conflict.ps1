# ==============================================================================
# SCRIPT MÔ PHỎNG XUNG ĐỘT PHÂN TÁN (DISTRIBUTED MERGE CONFLICT SIMULATION)
# Môn học: Hệ phân tán (CS420G) - Nhóm 15
# Mục đích: Tự động tạo 2 nhánh phân kỳ từ 2 lập trình viên (Dev A & Dev B)
#          cùng sửa đổi một dòng mã nguồn độc lập, tạo ra tình huống tranh chấp
#          ghi đồng thời (Concurrent Write Conflict) để quan sát cơ chế hòa giải.
# ==============================================================================

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   KỊCH BẢN THỰC NGHIỆM: XUNG ĐỘT TRẠNG THÁI TRONG GIT   " -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Kiểm tra xem git đã được khởi tạo chưa
if (-not (Test-Path ".git")) {
    Write-Host "[1/6] Khởi tạo Git repository cục bộ..." -ForegroundColor Green
    git init
    git config user.name "Team15-Coordinator"
    git config user.email "team15@dtu.edu.vn"
    git add .
    git commit -m "feat: Initial commit - CS420 Distributed Architecture"
}

# 2. Tạo nhánh cơ sở main
git branch -M main

# 3. Mô phỏng Lập trình viên A (Lê Văn Hoài Rin) tạo nhánh feature-node-a
Write-Host "`n[2/6] Node A (Dev Rin) tạo nhánh 'feature-node-a'..." -ForegroundColor Green
git checkout -b feature-node-a main

# Giả lập Dev A cập nhật logic hàm add
$fileCalc = "app/calculator.py"
(Get-Content $fileCalc) -replace 'return a \+ b', 'return float(a + b) # Node A formatted as float' | Set-Content $fileCalc
git add $fileCalc
git commit -m "feat(node-a): Dev Rin formats addition output as float"
Write-Host "-> Node A đã commit thay đổi thành công." -ForegroundColor Gray

# 4. Mô phỏng Lập trình viên B (Nguyễn Trung Hiếu) tạo nhánh feature-node-b từ main
Write-Host "`n[3/6] Node B (Dev Hiếu) tạo nhánh 'feature-node-b' từ main..." -ForegroundColor Green
git checkout main
git checkout -b feature-node-b main

# Giả lập Dev B cũng cập nhật đúng hàm add nhưng logic khác
(Get-Content $fileCalc) -replace 'return a \+ b', 'return round(a + b, 4) # Node B rounded to 4 decimals' | Set-Content $fileCalc
git add $fileCalc
git commit -m "feat(node-b): Dev Hieu rounds addition output to 4 decimals"
Write-Host "-> Node B đã commit thay đổi thành công." -ForegroundColor Gray

# 5. Hợp nhất nhánh của Dev A vào main trước
Write-Host "`n[4/6] Tiến hành hợp nhất nhánh của Node A vào main..." -ForegroundColor Green
git checkout main
git merge feature-node-a --no-edit
Write-Host "-> Hợp nhất feature-node-a vào main: THÀNH CÔNG (Fast-forward/Recursive)" -ForegroundColor Cyan

# 6. Thử hợp nhất nhánh của Dev B vào main -> Kích hoạt Merge Conflict
Write-Host "`n[5/6] Tiến hành hợp nhất nhánh của Node B vào main (Kỳ vọng Xung đột)..." -ForegroundColor Yellow
git merge feature-node-b

Write-Host "`n[6/6] KẾT QUẢ QUAN SÁT ĐƯỢC:" -ForegroundColor Magenta
Write-Host "Git đã phát hiện xung đột ghi đồng thời (Concurrent Write Conflict)!" -ForegroundColor Red
Write-Host "File bị xung đột: app/calculator.py" -ForegroundColor Yellow
Write-Host "`nHãy mở file 'app/calculator.py' để xem các ký hiệu xung đột:" -ForegroundColor White
Write-Host "  <<<<<<< HEAD (Phiên bản trên main từ Node A)" -ForegroundColor Cyan
Write-Host "  =======" -ForegroundColor Gray
Write-Host "  >>>>>>> feature-node-b (Phiên bản từ Node B)" -ForegroundColor Cyan

Write-Host "`n[HƯỚNG DẪN CHỤP ẢNH MINH CHỨNG]:" -ForegroundColor Green
Write-Host "1. Chụp lại màn hình terminal này để dán vào Mục 3.3 của Báo cáo."
Write-Host "2. Chạy lệnh: git status để chụp ảnh trạng thái 'both modified'."
Write-Host "3. Mở file calculator.py chụp đoạn code xung đột."
Write-Host "4. Sau đó chạy: git merge --abort để khôi phục trạng thái ban đầu khi cần."
