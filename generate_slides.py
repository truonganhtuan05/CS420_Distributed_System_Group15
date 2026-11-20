import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions: 13.333 x 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Bảng màu chuẩn Đại học Duy Tân
    C_NAVY = RGBColor(0, 51, 102)     # #003366
    C_RED = RGBColor(139, 0, 0)       # #8B0000
    C_DARK = RGBColor(30, 41, 59)     # #1E293B
    C_GRAY = RGBColor(100, 116, 139)  # #64748B
    C_LIGHT = RGBColor(241, 245, 249) # #F1F5F9
    C_WHITE = RGBColor(255, 255, 255)
    C_GOLD = RGBColor(217, 119, 6)    # #D97706 Accent

    def add_header(slide, title_text, category_text="ĐỒ ÁN HỆ PHÂN TÁN (CS420G) - NHÓM 15"):
        # Header banner top
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.05))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_NAVY
        top_bar.line.color.rgb = C_NAVY

        # Accent red line
        red_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(1.05), Inches(13.333), Inches(0.05))
        red_bar.fill.solid()
        red_bar.fill.fore_color.rgb = C_RED
        red_bar.line.color.rgb = C_RED

        # Category text
        txBox1 = slide.shapes.add_textbox(Inches(0.8), Inches(0.1), Inches(11), Inches(0.28))
        tf1 = txBox1.text_frame
        tf1.word_wrap = True
        p1 = tf1.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(9.5)
        p1.font.bold = True
        p1.font.color.rgb = RGBColor(180, 200, 230)

        # Title text
        txBox2 = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(11), Inches(0.6))
        tf2 = txBox2.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = title_text
        p2.font.size = Pt(21)
        p2.font.bold = True
        p2.font.color.rgb = C_WHITE

    def add_card(slide, left, top, width, height, bg_color=C_LIGHT, border_color=None):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        if border_color:
            shape.line.color.rgb = border_color
            shape.line.width = Pt(1.5)
        else:
            shape.line.fill.background()
        return shape

    def add_guide_cue(slide, speaker_text, duration_text, cue_text):
        """Thêm thanh hướng dẫn trình bày trực quan thanh lịch ở chân slide"""
        cue_bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.85), Inches(11.733), Inches(0.52))
        cue_bar.fill.solid()
        cue_bar.fill.fore_color.rgb = RGBColor(238, 242, 255) # Light indigo
        cue_bar.line.color.rgb = RGBColor(165, 180, 252)
        cue_bar.line.width = Pt(1)

        tb = slide.shapes.add_textbox(Inches(0.9), Inches(6.87), Inches(11.5), Inches(0.48))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        
        r_spk = p.add_run()
        r_spk.text = f"🎙️ {speaker_text} ({duration_text}) | "
        r_spk.font.bold = True
        r_spk.font.size = Pt(9.5)
        r_spk.font.color.rgb = C_NAVY

        r_cue = p.add_run()
        r_cue.text = f"Trọng tâm nói: {cue_text}"
        r_cue.font.size = Pt(9)
        r_cue.font.color.rgb = C_DARK

    def set_speaker_notes(slide, presenter, duration, goal, script, key_terms):
        """Thiết lập Speaker Notes (Ghi chú diễn giả) chi tiết cho PowerPoint"""
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        
        full_notes = (
            f"========================================================================\n"
            f"HƯỚNG DẪN THUYẾT TRÌNH (SPEAKER NOTES)\n"
            f"========================================================================\n"
            f"👤 Người trình bày: {presenter}\n"
            f"⏱️ Thời lượng ước tính: {duration}\n"
            f"🎯 Mục tiêu slide: {goal}\n\n"
            f"📢 LỜI THOẠI CHI TIẾT (SCRIPT NÓI):\n"
            f"{script}\n\n"
            f"🔑 TỪ KHÓA ĂN ĐIỂM HỆ PHÂN TÁN:\n"
            f"{key_terms}\n"
            f"========================================================================"
        )
        tf.text = full_notes

    # =========================================================================
    # SLIDE 1: TRANG BÌA (TITLE SLIDE)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = C_NAVY
    bg1.line.color.rgb = C_NAVY

    tb_u = s1.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.333), Inches(0.8))
    p_u = tb_u.text_frame.paragraphs[0]
    p_u.text = "ĐẠI HỌC DUY TÂN - TRƯỜNG KHOA HỌC MÁY TÍNH"
    p_u.font.size = Pt(14)
    p_u.font.bold = True
    p_u.font.color.rgb = RGBColor(255, 120, 120)

    tb_t = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(2.2))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p_t1 = tf_t.paragraphs[0]
    p_t1.text = "NGHIÊN CỨU KIẾN TRÚC PHÂN TÁN CỦA GITHUB"
    p_t1.font.size = Pt(32)
    p_t1.font.bold = True
    p_t1.font.color.rgb = C_WHITE

    p_t2 = tf_t.add_paragraph()
    p_t2.text = "VÀ TRIỂN KHAI TỰ ĐỘNG HÓA CI/CD VỚI GITHUB ACTIONS"
    p_t2.font.size = Pt(28)
    p_t2.font.bold = True
    p_t2.font.color.rgb = RGBColor(100, 200, 255)

    add_card(s1, 1.0, 4.3, 11.333, 2.0, bg_color=RGBColor(10, 40, 80))
    tb_info = s1.shapes.add_textbox(Inches(1.3), Inches(4.45), Inches(10.7), Inches(1.7))
    tf_i = tb_info.text_frame
    
    p_i1 = tf_i.paragraphs[0]
    p_i1.text = "Môn học: HỆ PHÂN TÁN (CS420G)   |   Mã đề tài: 01CS420   |   Nhóm: 15"
    p_i1.font.size = Pt(14)
    p_i1.font.bold = True
    p_i1.font.color.rgb = C_WHITE

    p_i2 = tf_i.add_paragraph()
    p_i2.text = "Giảng viên hướng dẫn: ThS. Nguyễn Minh Nhật"
    p_i2.font.size = Pt(13)
    p_i2.font.color.rgb = RGBColor(220, 220, 220)

    p_i3 = tf_i.add_paragraph()
    p_i3.text = "Sinh viên thực hiện:  Lê Văn Hoài Rin (29211434457)   -   Nguyễn Trung Hiếu (29211441367)   -   Trương Anh Tuấn (29211453666)"
    p_i3.font.size = Pt(13)
    p_i3.font.color.rgb = RGBColor(255, 230, 150)

    add_guide_cue(s1, "Lê Văn Hoài Rin", "1 phút", "Chào Thầy và các bạn, giới thiệu tên đề tài, nhóm 15 và 3 thành viên, định vị chủ đề gắn liền môn Hệ phân tán.")
    set_speaker_notes(
        s1,
        presenter="Lê Văn Hoài Rin (Trưởng nhóm)",
        duration="1 phút",
        goal="Tạo ấn tượng ban đầu tự tin, chuyên nghiệp; nêu rõ đề tài môn Hệ phân tán.",
        script=(
            "Kính chào Thầy Nguyễn Minh Nhật cùng toàn thể các bạn sinh viên lớp CS420G.\n"
            "Em tên là Lê Văn Hoài Rin, đại diện cho Nhóm 15 gồm có em, bạn Nguyễn Trung Hiếu và bạn Trương Anh Tuấn.\n"
            "Hôm nay, nhóm chúng em xin được báo cáo đề tài Đồ án môn Hệ phân tán: 'Nghiên cứu kiến trúc phân tán của GitHub và Triển khai tự động hóa CI/CD với GitHub Actions'.\n"
            "Mục tiêu của đề tài không dừng lại ở việc sử dụng Git như một công cụ lưu trữ mã nguồn, mà là phân tích sâu bản chất của Git như một Hệ thống Cơ sở Dữ liệu Phi tập trung và GitHub Actions như một Nền tảng Điều phối Tính toán Phân tán."
        ),
        key_terms="Distributed Version Control, State Machine, Master-Worker, Decentralized Nodes."
    )

    # =========================================================================
    # SLIDE 2: NỘI DUNG TRÌNH BÀY (AGENDA)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "NỘI DUNG BÁO CÁO")

    agenda_items = [
        ("1", "MỞ ĐẦU", "Lý do chọn đề tài, mục tiêu nghiên cứu và phương pháp thực hiện"),
        ("2", "CHƯƠNG 1: TỔNG QUAN LÝ THUYẾT", "Kiến trúc DAG, thuật toán 3-Way Merge và hệ điều phối GitHub Actions"),
        ("3", "CHƯƠNG 2: THIẾT KẾ BÀI TOÁN DEMO", "Bài toán, yêu cầu Đầu vào / Đầu ra, kiến trúc 4 tầng và luồng CI/CD"),
        ("4", "CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM", "5 kịch bản kiểm thử: Đồng bộ, Merge Conflict, Matrix Testing, Fail-Fast & CD"),
        ("5", "KẾT LUẬN & ĐÁNH GIÁ", "Kết quả đạt được, bài học môn Hệ phân tán và hướng phát triển")
    ]

    for idx, (num, title, desc) in enumerate(agenda_items):
        top_pos = 1.4 + idx * 1.05
        add_card(s2, 1.0, top_pos, 11.333, 0.9, bg_color=C_LIGHT)
        
        badge = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.2), Inches(top_pos + 0.12), Inches(0.7), Inches(0.65))
        badge.fill.solid()
        badge.fill.fore_color.rgb = C_NAVY
        badge.line.color.rgb = C_NAVY
        p_b = badge.text_frame.paragraphs[0]
        p_b.text = num
        p_b.font.size = Pt(16)
        p_b.font.bold = True
        p_b.font.color.rgb = C_WHITE
        p_b.alignment = PP_ALIGN.CENTER

        tb = s2.shapes.add_textbox(Inches(2.1), Inches(top_pos + 0.08), Inches(10.0), Inches(0.72))
        tf = tb.text_frame
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(13.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_NAVY
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = C_GRAY

    add_guide_cue(s2, "Lê Văn Hoài Rin", "45 giây", "Điểm qua 5 phần chính, nhấn mạnh Chương 2 & 3 có kịch bản thực nghiệm bám sát chỉ đạo của Giảng viên.")
    set_speaker_notes(
        s2,
        presenter="Lê Văn Hoài Rin",
        duration="45 giây",
        goal="Tóm tắt lộ trình bài thuyết trình, giúp Thầy và lớp nắm được cấu trúc logic.",
        script=(
            "Bài báo cáo hôm nay được nhóm chia làm 5 phần chính:\n"
            "Thứ nhất là Phần Mở đầu, trình bày lý do chọn đề tài và bài toán hệ phân tán thực tế;\n"
            "Thứ hai là Chương 1, tổng quan lý thuyết về kiến trúc DAG và hệ điều phối Actions;\n"
            "Thứ ba là Chương 2, thiết kế chi tiết bài toán demo với các tham số Đầu vào - Đầu ra theo đúng dặn dò của Thầy;\n"
            "Thứ tư là Chương 3, kết quả triển khai 5 kịch bản thực nghiệm trực tiếp;\n"
            "Và cuối cùng là phần Tổng kết cùng những bài học kinh nghiệm trong môn học."
        ),
        key_terms="Bố cục 3 chương chuẩn ĐH Duy Tân, Lý thuyết 6đ, Thực nghiệm 4đ."
    )

    # =========================================================================
    # SLIDE 3: MỞ ĐẦU - LÝ DO CHỌN ĐỀ TÀI
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "1. LÝ DO CHỌN ĐỀ TÀI")

    add_card(s3, 1.0, 1.4, 5.4, 5.1, bg_color=C_LIGHT)
    tb_l = s3.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "VẤN ĐỀ THỰC TẾ TRONG HỆ PHÂN TÁN"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_RED

    points_l = [
        ("Nhiều người ghi đồng thời:", "Khi nhiều kỹ sư ở các node khác nhau sửa cùng tài nguyên, xung đột trạng thái dữ liệu (Race Conditions) là tất yếu."),
        ("Điểm lỗi đơn (SPOF) ở hệ thống cũ:", "Hệ thống SVN/CVS phụ thuộc hoàn toàn máy chủ trung tâm; mất mạng là toàn bộ kỹ sư dừng làm việc."),
        ("Kiểm thử tuần tự gây nghẽn cổ chai:", "Kiểm tra mã nguồn trên máy cá nhân không đồng nhất môi trường, dễ phát sinh lỗi khi tích hợp.")
    ]
    for h, b in points_l:
        p1 = tf_l.add_paragraph()
        p1.text = "• " + h
        p1.font.bold = True
        p1.font.size = Pt(11)
        p1.font.color.rgb = C_DARK
        p2 = tf_l.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_card(s3, 6.9, 1.4, 5.4, 5.1, bg_color=C_LIGHT)
    tb_r = s3.shapes.add_textbox(Inches(7.1), Inches(1.55), Inches(5.0), Inches(4.7))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_r = tf_r.paragraphs[0]
    p_r.text = "GIẢI PHÁP TỪ GIT & GITHUB ACTIONS"
    p_r.font.bold = True
    p_r.font.size = Pt(13)
    p_r.font.color.rgb = C_NAVY

    points_r = [
        ("Mô hình Full Replica phi tập trung:", "Mỗi máy trạm sở hữu 100% cơ sở dữ liệu lịch sử, làm việc offline tuyệt đối, không có điểm lỗi đơn."),
        ("Hòa giải xung đột bằng 3-Way Merge:", "Sử dụng đồ thị DAG và quan hệ nhân quả (Causal Ordering) để phát hiện và gộp trạng thái phân tán."),
        ("Tính toán song song đa Worker:", "GitHub Actions điều phối các máy ảo (Runners) độc lập chạy ma trận kiểm thử song song, ngắt mạch tự động khi có lỗi.")
    ]
    for h, b in points_r:
        p1 = tf_r.add_paragraph()
        p1.text = "✔ " + h
        p1.font.bold = True
        p1.font.size = Pt(11)
        p1.font.color.rgb = C_DARK
        p2 = tf_r.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_guide_cue(s3, "Lê Văn Hoài Rin", "1.5 phút", "Nhấn mạnh sự tương phản: Hệ thống cũ bị SPOF và xung đột ghi; Git giải quyết bằng Full Replica và 3-way merge.")
    set_speaker_notes(
        s3,
        presenter="Lê Văn Hoài Rin",
        duration="1.5 phút",
        goal="Làm rõ tính phân tán của bài toán, chứng minh lý do đề tài này thuộc môn Hệ phân tán.",
        script=(
            "Kính thưa Thầy, trong thực tế khi một nhóm kỹ sư phân tán cùng phát triển phần mềm, chúng ta đối mặt với ba thách thức lớn:\n"
            "Thứ nhất là bài toán Ghi đồng thời (Concurrent Write): Hai người cùng sửa một file mà không biết về nhau, dẫn đến tranh chấp trạng thái dữ liệu;\n"
            "Thứ hai là Điểm lỗi đơn (SPOF) ở các hệ thống tập trung như SVN: Nếu server mất kết nối, toàn bộ kỹ sư đều bị tê liệt;\n"
            "Và thứ ba là việc kiểm thử tuần tự thủ công gây trễ nghẽn.\n"
            "Giải pháp mà Git và GitHub Actions mang lại chính là: Mỗi máy trạm là một bản sao đầy đủ (Full Replica) giúp loại bỏ SPOF; thuật toán 3-Way Merge giúp giải quyết xung đột; và GitHub Actions điều phối các máy ảo Worker chạy kiểm thử song song tự động."
        ),
        key_terms="SPOF (Single Point of Failure), Concurrent Updates, Race Conditions, Full Replica."
    )

    # =========================================================================
    # SLIDE 4: MỞ ĐẦU - MỤC TIÊU VÀ PHẠM VI
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "2. MỤC TIÊU VÀ PHẠM VI NGHIÊN CỨU")

    add_card(s4, 1.0, 1.4, 3.6, 5.1)
    tb1 = s4.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(3.2), Inches(4.7))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "MỤC TIÊU LÝ THUYẾT"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    items1 = [
        "Phân tích cấu trúc phân tán DAG và hàm băm SHA.",
        "Thuật toán 3-Way Merge giải quyết xung đột ghi đồng thời.",
        "Mô hình Master-Worker của GitHub Actions.",
        "Nguyên tắc ngắt mạch (Circuit Breaker / Fail-Fast)."
    ]
    for it in items1:
        p = tf1.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_card(s4, 4.86, 1.4, 3.6, 5.1)
    tb2 = s4.shapes.add_textbox(Inches(5.06), Inches(1.55), Inches(3.2), Inches(4.7))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "MỤC TIÊU THỰC NGHIỆM"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    items2 = [
        "Xây dựng dịch vụ phân tán REST API bằng Python.",
        "Tạo ma trận kiểm thử song song trên 3 Worker (Python 3.10, 3.11, 3.12).",
        "Mô phỏng xung đột đồng thời giữa 2 Node máy trạm.",
        "Đóng gói tự động bản phát hành phân tán (Artifacts/Docker)."
    ]
    for it in items2:
        p = tf2.add_paragraph()
        p.text = "• " + it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_card(s4, 8.73, 1.4, 3.6, 5.1)
    tb3 = s4.shapes.add_textbox(Inches(8.93), Inches(1.55), Inches(3.2), Inches(4.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "PHẠM VI NGHIÊN CỨU"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    items3 = [
        "Trong phạm vi:",
        "  - Git CLI v2.x trên Windows 11.",
        "  - GitHub Cloud Repository công khai.",
        "  - GitHub-hosted Linux Ubuntu Runners.",
        "Ngoài phạm vi:",
        "  - Cài đặt GitHub Enterprise Server trên hạ tầng vật lý riêng.",
        "  - Khảo sát tải hàng triệu request đồng thời."
    ]
    for it in items3:
        p = tf3.add_paragraph()
        p.text = it
        p.font.size = Pt(10)
        p.font.color.rgb = C_DARK

    add_guide_cue(s4, "Lê Văn Hoài Rin", "1 phút", "Nêu ngắn gọn 2 mục tiêu lý thuyết & thực nghiệm, giới hạn rõ phạm vi nghiên cứu trên Cloud Runners.")
    set_speaker_notes(
        s4,
        presenter="Lê Văn Hoài Rin",
        duration="1 phút",
        goal="Xác lập ranh giới đề tài rõ ràng, tránh bị hỏi ngoài phạm vi.",
        script=(
            "Về mục tiêu, nhóm xác định rõ ràng: Lý thuyết là làm sáng tỏ bản chất phân tán của Git DAG và Master-Worker Runner. "
            "Thực nghiệm là xây dựng hoàn chỉnh một ứng dụng REST API kiểm thử song song trên 3 phiên bản Python và giải quyết xung đột.\n"
            "Về phạm vi, nhóm thực hiện trên môi trường máy trạm Windows 11 và các máy ảo Ubuntu Runner được cấp phát trên đám mây của GitHub, phù hợp với quy mô môn học."
        ),
        key_terms="Phạm vi nghiên cứu, Ubuntu Runners, REST API Testing."
    )

    # =========================================================================
    # SLIDE 5: CHƯƠNG 1 - TỔNG QUAN LÝ THUYẾT: CVCS VS DVCS
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "1.1. SỰ TIẾN HÓA TỪ CVCS SANG DVCS", "CHƯƠNG 1: TỔNG QUAN LÝ THUYẾT")

    add_card(s5, 1.0, 1.4, 5.4, 5.1, bg_color=C_LIGHT)
    tb = s5.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "HỆ THỐNG TẬP TRUNG (CVCS - SVN)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_RED
    c_svn = [
        ("Cơ sở dữ liệu:", "Lưu trữ độc nhất tại Server trung tâm."),
        ("Điểm lỗi đơn (SPOF):", "Server sập hoặc đứt cáp là toàn bộ kỹ sư ngừng trệ."),
        ("Tốc độ commit:", "Phụ thuộc độ trễ mạng Internet."),
        ("Thao tác Offline:", "Không thể commit hay duyệt lịch sử khi mất mạng."),
        ("Mô hình kiểm soát:", "Khóa tệp (File locking) gây tắc nghẽn.")
    ]
    for h, b in c_svn:
        p = tf.add_paragraph()
        p.text = "✖ " + h + " " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_card(s5, 6.9, 1.4, 5.4, 5.1, bg_color=C_LIGHT)
    tb = s5.shapes.add_textbox(Inches(7.1), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "HỆ THỐNG PHÂN TÁN (DVCS - GIT)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = C_NAVY
    c_git = [
        ("Cơ sở dữ liệu:", "Mỗi node lưu bản sao đầy đủ (Full Replica)."),
        ("Tính sẵn sàng cao:", "Không có SPOF; mất server vẫn làm việc bình thường."),
        ("Tốc độ commit:", "Cực nhanh vì ghi trực tiếp trên đĩa cứng cục bộ."),
        ("Thao tác Offline:", "Hỗ trợ 100%: commit, tạo nhánh, xem log không cần mạng."),
        ("Mô hình kiểm soát:", "Đồ thị DAG và hòa giải xung đột thông minh 3-Way Merge.")
    ]
    for h, b in c_git:
        p = tf.add_paragraph()
        p.text = "✔ " + h + " " + b
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_guide_cue(s5, "Lê Văn Hoài Rin", "1.5 phút", "Nhấn mạnh từ khóa: 'Full Replica' và 'Offline-first'. SVN phụ thuộc mạng, Git độc lập hoàn toàn.")
    set_speaker_notes(
        s5,
        presenter="Lê Văn Hoài Rin",
        duration="1.5 phút",
        goal="So sánh chuyên sâu giữa 2 kiến trúc, làm nổi bật tại sao DVCS là bước nhảy vọt trong hệ phân tán.",
        script=(
            "Thưa Thầy, để thấy rõ bước tiến công nghệ, bảng này đối chiếu SVN đại diện cho hệ tập trung và Git đại diện cho hệ phân tán.\n"
            "Ở SVN, điểm yếu chí tử là SPOF: Toàn bộ database lịch sử nằm trên server trung tâm. Máy trạm chỉ tải về một snapshot làm việc tạm thời. Mất mạng là dừng toàn bộ hoạt động.\n"
            "Trong khi đó, ở Git, mỗi lệnh clone tạo ra một Full Replica hoàn chỉnh. Mọi thao tác commit, tạo branch, diff đều diễn ra trực tiếp trên đĩa cứng cục bộ với tốc độ micro-giây và khả năng làm việc Offline 100%."
        ),
        key_terms="Centralized vs Distributed, Full Replica, Latency, Offline-first."
    )

    # =========================================================================
    # SLIDE 6: CHƯƠNG 1 - KIẾN TRÚC DỮ LIỆU PHÂN TÁN: DAG & SHA
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "1.2. CẤU TRÚC DỮ LIỆU PHÂN TÁN: ĐỒ THỊ DAG & HÀM BĂM SHA", "CHƯƠNG 1: TỔNG QUAN LÝ THUYẾT")

    add_card(s6, 1.0, 1.4, 11.333, 2.4)
    tb = s6.shapes.add_textbox(Inches(1.3), Inches(1.55), Inches(10.7), Inches(2.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "CƠ CHẾ LƯU TRỮ THEO NỘI DUNG (CONTENT-ADDRESSABLE STORAGE)"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    p_b = tf.add_paragraph()
    p_b.text = "• Mọi đối tượng (Blob, Tree, Commit) đều được định danh bằng mã băm SHA-1 (40 ký tự) hoặc SHA-256.\n" \
               "• Mã băm tính toán dựa trên: [Nội dung tệp] + [Mã băm commit cha] + [Thông tin tác giả & thời gian].\n" \
               "• Tính bất biến (Immutability): Không ai có thể sửa đổi dữ liệu trong quá khứ mà không làm thay đổi toàn bộ mã băm phía sau, tương tự cấu trúc Merkle Tree trong Blockchain."
    p_b.font.size = Pt(11)
    p_b.font.color.rgb = C_DARK

    add_card(s6, 1.0, 4.0, 11.333, 2.5)
    tb = s6.shapes.add_textbox(Inches(1.3), Inches(4.15), Inches(10.7), Inches(2.1))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "ĐỒ THỊ PHI CHU TRÌNH CÓ HƯỚNG (DIRECTED ACYCLIC GRAPH - DAG)"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    p_b = tf.add_paragraph()
    p_b.text = "• Mỗi commit là một đỉnh (node) trong đồ thị DAG, lưu con trỏ trỏ về các commit cha (parent commit).\n" \
               "• Không có chu trình: Thời gian luôn tiến về phía trước, không thể có commit con là cha của chính nó.\n" \
               "• Quan hệ nhân quả (Causal Ordering): Tương tự Logical Clocks của Lamport trong hệ phân tán, đồ thị DAG cho phép xác định chính xác commit nào xảy ra trước, commit nào xảy ra sau, hoặc xảy ra đồng thời (rẽ nhánh)."
    p_b.font.size = Pt(11)
    p_b.font.color.rgb = C_DARK

    add_guide_cue(s6, "Lê Văn Hoài Rin", "2 phút", "Liên hệ kiến thức môn học: 'DAG đại diện cho Causal Ordering - Quan hệ nhân quả tương tự Lamport Logical Clocks'.")
    set_speaker_notes(
        s6,
        presenter="Lê Văn Hoài Rin",
        duration="2 phút",
        goal="Ghi điểm học thuật cao nhất phần lý thuyết: liên hệ cấu trúc Git với lý thuyết hệ phân tán chuẩn mực.",
        script=(
            "Kính thưa Thầy, đây là slide lý thuyết cốt lõi nhất của Chương 1. Hai nền tảng toán học của Git gồm:\n"
            "Thứ nhất là Content-Addressable Storage: Mỗi commit được hash SHA dựa trên nội dung và hash cha. Cơ chế này giống hệt Merkle Tree trong Blockchain, đảm bảo tính toàn vẹn (Immutability). Dù truyền qua mạng không an toàn, không ai có thể sửa ngầm dữ liệu.\n"
            "Thứ hai là đồ thị DAG: Trong hệ phân tán, các máy trạm không có đồng hồ vật lý đồng bộ tuyệt đối. Git giải quyết bằng Quan hệ nhân quả (Causal Ordering) giống như Lamport Logical Clock mà Thầy đã giảng dạy. Dựa vào con trỏ cha-con trên DAG, Git biết chính xác sự kiện nào xảy ra trước, sự kiện nào xảy ra sau, và khi nào hai sự kiện xảy ra đồng thời độc lập."
        ),
        key_terms="DAG, Content-Addressable Storage, Merkle Tree, Lamport Logical Clocks, Causal Ordering."
    )

    # =========================================================================
    # SLIDE 7: CHƯƠNG 1 - NGUYÊN LÝ HOẠT ĐỘNG: 3-WAY MERGE
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "1.3. THUẬT TOÁN HÒA GIẢI XUNG ĐỘT 3-WAY MERGE", "CHƯƠNG 1: TỔNG QUAN LÝ THUYẾT")

    add_card(s7, 1.0, 1.4, 3.6, 5.1)
    tb = s7.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(3.2), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. BASE COMMIT (B)\n(Tổ tiên chung gần nhất)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_NAVY
    p_c = tf.add_paragraph()
    p_c.text = "Điểm rẽ nhánh chung gần nhất trong đồ thị DAG trước khi Node A và Node B tiến hành chỉnh sửa độc lập."
    p_c.font.size = Pt(10.5)

    add_card(s7, 4.86, 1.4, 3.6, 5.1)
    tb = s7.shapes.add_textbox(Inches(5.06), Inches(1.55), Inches(3.2), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2. TRẠNG THÁI HIỆN TẠI\n(Node A vs Node B)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_NAVY
    p_c = tf.add_paragraph()
    p_c.text = "• Node A cập nhật trạng thái tại dòng X.\n• Node B cập nhật trạng thái tại dòng Y (hoặc cùng dòng X).\n• Git so sánh cả A và B đối chiếu ngược lại với Base B."
    p_c.font.size = Pt(10.5)

    add_card(s7, 8.73, 1.4, 3.6, 5.1)
    tb = s7.shapes.add_textbox(Inches(8.93), Inches(1.55), Inches(3.2), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "3. HÒA GIẢI XUNG ĐỘT\n(Resolution Logic)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_RED
    p_c = tf.add_paragraph()
    p_c.text = "• Khác dòng: Tự động gộp sạch sẽ (Auto-merge).\n• Cùng dòng nhưng nội dung khác nhau: Báo CONFLICT.\n• Chèn Conflict Markers (<<<<<<<, =======, >>>>>>>).\n• Yêu cầu lập trình viên xác định trạng thái cuối cùng."
    p_c.font.size = Pt(10.5)

    add_guide_cue(s7, "Lê Văn Hoài Rin", "1.5 phút", "Giải thích cơ chế 3 điểm nút; khác dòng thì auto-merge, cùng dòng thì xuất hiện conflict markers. Chuyển lời cho Hiếu.")
    set_speaker_notes(
        s7,
        presenter="Lê Văn Hoài Rin -> chuyển tiếp Nguyễn Trung Hiếu",
        duration="1.5 phút",
        goal="Giải thích thuật toán 3-Way Merge rõ ràng, chuyển giao phần trình bày cho bạn Nguyễn Trung Hiếu.",
        script=(
            "Thuật toán 3-Way Merge là cơ chế giải quyết tranh chấp ghi đồng thời trong Git. Khác với việc chỉ so sánh 2 file (Diff 2-way), Git tìm nút tổ tiên chung gần nhất (Base B) trên đồ thị DAG.\n"
            "Nếu Node A sửa dòng 10, Node B sửa dòng 50: Git tự động hòa giải và gộp thành công.\n"
            "Nhưng nếu cả A và B cùng sửa dòng 10 với giá trị khác nhau: Git không tự đoán mà chèn các ký hiệu xung đột (Conflict Markers) để kỹ sư chủ động hòa giải.\n"
            "Tiếp theo đây, em xin mời bạn Nguyễn Trung Hiếu tiếp tục trình bày về hệ điều phối GitHub Actions."
        ),
        key_terms="3-Way Merge, Common Ancestor, Conflict Markers, Auto-merge vs Manual Resolution."
    )

    # =========================================================================
    # SLIDE 8: CHƯƠNG 1 - GITHUB ACTIONS: ĐIỀU PHỐI TÁC VỤ PHÂN TÁN
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "1.4. ĐIỀU PHỐI TÁC VỤ PHÂN TÁN VỚI GITHUB ACTIONS", "CHƯƠNG 1: TỔNG QUAN LÝ THUYẾT")

    add_card(s8, 1.0, 1.4, 5.4, 5.1)
    tb = s8.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "MASTER COORDINATOR (GITHUB CLOUD)"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    items = [
        ("Event-Driven Architecture:", "Lắng nghe các sự kiện phân tán (Push, Pull Request, Webhook, Cron Schedule)."),
        ("Workflow Dependency DAG:", "Phân tích file YAML, xác định các Job nào chạy tuần tự (needs), Job nào chạy song song."),
        ("Task Dispatching:", "Gửi các chỉ thị thực thi tới cụm máy trạm Worker tương ứng.")
    ]
    for h, b in items:
        p1 = tf.add_paragraph()
        p1.text = "• " + h
        p1.font.bold = True
        p1.font.size = Pt(11)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_card(s8, 6.9, 1.4, 5.4, 5.1)
    tb = s8.shapes.add_textbox(Inches(7.1), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "DISTRIBUTED WORKER NODES (RUNNERS)"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    items_r = [
        ("Ephemeral Virtual Machines:", "Các máy ảo độc lập (Ubuntu/Windows/macOS), cấp phát động, tự hủy sau khi xong để bảo mật."),
        ("Parallel Matrix Execution:", "Chia nhỏ 1 tác vụ chạy song song trên nhiều node ảo cùng lúc (Matrix Strategy)."),
        ("Real-time Log Streaming:", "Truyền luồng log thực thi trực tiếp về máy chủ trung tâm qua gRPC/Websocket.")
    ]
    for h, b in items_r:
        p1 = tf.add_paragraph()
        p1.text = "• " + h
        p1.font.bold = True
        p1.font.size = Pt(11)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_guide_cue(s8, "Nguyễn Trung Hiếu", "2 phút", "Nhấn mạnh mô hình Master-Worker: GitHub Cloud đóng vai trò Master điều phối; các Runner ảo là Ephemeral Workers.")
    set_speaker_notes(
        s8,
        presenter="Nguyễn Trung Hiếu",
        duration="2 phút",
        goal="Khẳng định GitHub Actions là mô hình tính toán phân tán Master-Worker chuẩn mực.",
        script=(
            "Kính chào Thầy và các bạn, em là Nguyễn Trung Hiếu. Em xin tiếp tục phần báo cáo với tầng tính toán phân tán của GitHub Actions.\n"
            "GitHub Actions là hiện thân của mô hình kiến trúc Master-Worker:\n"
            "Ở phía Master: GitHub Cloud là một Orchestrator hướng sự kiện (Event-driven). Khi nhận được push event, Master phân tích file workflow YAML thành một đồ thị DAG các Job.\n"
            "Ở phía Worker: GitHub điều phối các Runners - bản chất là các máy tính ảo tạm thời (Ephemeral Virtual Machines). Các worker này chạy độc lập, nhận task, thực thi song song và truyền log real-time về Master rồi tự hủy, đảm bảo cô lập tài nguyên tuyệt đối."
        ),
        key_terms="Master-Worker Architecture, Event-Driven, Ephemeral Runners, Task Dispatching."
    )

    # =========================================================================
    # SLIDE 9: CHƯƠNG 2 - BÀI TOÁN DEMO & YÊU CẦU ĐẦU VÀO / ĐẦU RA
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "2.1. BÀI TOÁN DEMO VÀ THAM SỐ ĐẦU VÀO / ĐẦU RA", "CHƯƠNG 2: THIẾT KẾ BÀI TOÁN DEMO")

    add_card(s9, 1.0, 1.35, 11.333, 0.95, bg_color=RGBColor(230, 240, 255), border_color=C_NAVY)
    tb_b = s9.shapes.add_textbox(Inches(1.2), Inches(1.4), Inches(11), Inches(0.85))
    p_b = tb_b.text_frame.paragraphs[0]
    p_b.text = "BÀI TOÁN: CHUỖI CUNG ỨNG PHẦN MỀM PHÂN TÁN TỰ ĐỘNG CHO DỊCH VỤ REST API"
    p_b.font.bold = True
    p_b.font.size = Pt(12)
    p_b.font.color.rgb = C_NAVY
    p_sub = tb_b.text_frame.add_paragraph()
    p_sub.text = "Mô phỏng 2 kỹ sư sửa đổi code độc lập, đồng bộ trạng thái qua GitHub và kích hoạt 3 Worker ảo kiểm thử song song."
    p_sub.font.size = Pt(10.5)

    add_card(s9, 1.0, 2.45, 5.4, 4.2)
    tb = s9.shapes.add_textbox(Inches(1.2), Inches(2.6), Inches(5.0), Inches(3.9))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "YÊU CẦU ĐẦU VÀO (INPUTS)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_RED
    inputs = [
        "1. Mã nguồn dịch vụ tính toán phân tán (app/calculator.py, app/server.py).",
        "2. Bộ kiểm thử đơn vị tự động pytest (tests/test_calculator.py).",
        "3. Tệp đặc tả điều phối phân tán (.github/workflows/ci-cd.yml).",
        "4. Các commit/push đồng thời từ Node A và Node B kích hoạt xung đột."
    ]
    for it in inputs:
        p = tf.add_paragraph()
        p.text = it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_card(s9, 6.9, 2.45, 5.4, 4.2)
    tb = s9.shapes.add_textbox(Inches(7.1), Inches(2.6), Inches(5.0), Inches(3.9))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "YÊU CẦU ĐẦU RA (OUTPUTS)"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = C_NAVY
    outputs = [
        "1. Đồ thị Git DAG thể hiện rõ commit phân kỳ và kết quả 3-Way Merge.",
        "2. Nhật ký chạy song song của 3 Worker Nodes (Python 3.10, 3.11, 3.12).",
        "3. Phản hồi ngắt mạch (Circuit Breaker): Báo đỏ khi phát hiện commit lỗi.",
        "4. Gói phân phối Artifacts (app-<commit-sha>.tar.gz) và log CD deploy."
    ]
    for it in outputs:
        p = tf.add_paragraph()
        p.text = it
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_guide_cue(s9, "Nguyễn Trung Hiếu", "1.5 phút", "Nhấn mạnh: 'Nhóm thực hiện nghiêm túc dặn dò của Thầy về việc xác định rõ bài toán, Đầu vào (Inputs) và Đầu ra (Outputs)'.")
    set_speaker_notes(
        s9,
        presenter="Nguyễn Trung Hiếu",
        duration="1.5 phút",
        goal="Trả lời trực tiếp và đầy đủ yêu cầu dặn dò của Giảng viên trên Zalo/LMS về Đầu vào và Đầu ra.",
        script=(
            "Kính thưa Thầy, tiếp thu dặn dò của Thầy về phần Demo, nhóm chúng em đã chuẩn hóa rất rõ ràng:\n"
            "Bài toán đặt ra là: Xây dựng một dịch vụ tính toán phân tán Stateless REST API kết hợp chuỗi cung ứng CI/CD khép kín.\n"
            "Về Đầu vào (Inputs): Gồm mã nguồn dịch vụ, 7 bài unit test tự động, file workflow ci-cd.yml, và các commit đồng thời từ 2 kỹ sư.\n"
            "Về Đầu ra (Outputs): Phải thu được đồ thị DAG hòa giải xung đột, nhật ký thực thi song song của 3 máy ảo Worker, cơ chế ngắt mạch Fail-Fast bảo vệ hệ thống, và gói phần mềm Artifacts sẵn sàng triển khai."
        ),
        key_terms="Đầu vào / Đầu ra (Inputs/Outputs), Stateless REST API, Circuit Breaker."
    )

    # =========================================================================
    # SLIDE 10: CHƯƠNG 2 - MÔ HÌNH KIẾN TRÚC 4 TẦNG CỦA HỆ THỐNG DEMO
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "2.2. MÔ HÌNH KIẾN TRÚC 4 TẦNG HỆ THỐNG DEMO", "CHƯƠNG 2: THIẾT KẾ BÀI TOÁN DEMO")

    layers = [
        ("TẦNG 1: CÁC NODE MÁY TRẠM (REPLICAS)", "Node A (Dev Rin) và Node B (Dev Hiếu) thực hiện commit độc lập trên local Git DAG.", C_NAVY),
        ("TẦNG 2: REMOTE COORDINATION HUB", "GitHub Central Repository tiếp nhận push, kiểm soát xung đột và kích hoạt webhook.", RGBColor(0, 102, 204)),
        ("TẦNG 3: DISTRIBUTED COMPUTATION RUNNERS", "3 máy ảo Ubuntu độc lập chạy song song ma trận kiểm thử Python 3.10, 3.11, 3.12.", RGBColor(16, 149, 193)),
        ("TẦNG 4: DEPLOYMENT & DELIVERY TARGET", "Tự động đóng gói Artifacts và kích hoạt quy trình triển khai phân tán liên tục.", RGBColor(40, 167, 69))
    ]

    for idx, (title, desc, color) in enumerate(layers):
        top_pos = 1.4 + idx * 1.3
        add_card(s10, 1.0, top_pos, 11.333, 1.1, bg_color=C_LIGHT)
        
        bar = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(top_pos), Inches(0.2), Inches(1.1))
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.color.rgb = color

        tb = s10.shapes.add_textbox(Inches(1.4), Inches(top_pos + 0.08), Inches(10.7), Inches(0.92))
        tf = tb.text_frame
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.bold = True
        p_t.font.size = Pt(12.5)
        p_t.font.color.rgb = color
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = C_DARK

    add_guide_cue(s10, "Nguyễn Trung Hiếu", "1.5 phút", "Đi từ Tầng 1 (Node máy trạm) -> Tầng 2 (Hub trung tâm) -> Tầng 3 (Worker Runners) -> Tầng 4 (Giao phẩm CD).")
    set_speaker_notes(
        s10,
        presenter="Nguyễn Trung Hiếu",
        duration="1.5 phút",
        goal="Trình bày kiến trúc phân tầng chuyên nghiệp, thể hiện sự am hiểu hệ thống.",
        script=(
            "Thưa Thầy, hệ thống demo được nhóm cấu trúc thành 4 tầng rõ rệt:\n"
            "Tầng 1 là Các Node máy trạm cục bộ của kỹ sư, thực hiện việc phát triển mã nguồn và quản lý commit trên đĩa cứng riêng;\n"
            "Tầng 2 là Remote Hub trên GitHub Cloud, đóng vai trò điểm hòa giải trạng thái và phát sinh sự kiện;\n"
            "Tầng 3 là Cụm Worker Runners phân tán, gồm 3 máy ảo Ubuntu được cấp phát động để kiểm thử song song;\n"
            "Tầng 4 là Tầng bàn giao liên tục (Continuous Delivery), nơi ứng dụng được tự động đóng gói thành Artifact và mô phỏng deploy ra môi trường thực tế."
        ),
        key_terms="Kiến trúc 4 tầng, Ephemeral Virtual Machines, Continuous Delivery, Artifact Storage."
    )

    # =========================================================================
    # SLIDE 11: CHƯƠNG 2 - CẤU HÌNH MA TRẬN TÍNH TOÁN SONG SONG
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "2.3. CẤU HÌNH ĐIỀU PHỐI VÀ MA TRẬN SONG SONG (MATRIX)", "CHƯƠNG 2: THIẾT KẾ BÀI TOÁN DEMO")

    add_card(s11, 1.0, 1.4, 6.0, 5.1, bg_color=RGBColor(20, 25, 35))
    tb = s11.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.6), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "ĐẶC TẢ WORKFLOW (.github/workflows/ci-cd.yml)"
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = RGBColor(100, 200, 255)

    code_txt = (
        "jobs:\n"
        "  distributed-matrix-test:\n"
        "    name: Test Node (${{ matrix.python-version }})\n"
        "    needs: code-quality\n"
        "    runs-on: ubuntu-latest\n"
        "    strategy:\n"
        "      fail-fast: false\n"
        "      matrix:\n"
        "        python-version: ['3.10', '3.11', '3.12']\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - name: Setup Python\n"
        "        uses: actions/setup-python@v5\n"
        "      - name: Run Pytest\n"
        "        run: pytest -v tests/"
    )
    p_code = tf.add_paragraph()
    p_code.text = code_txt
    p_code.font.name = "Consolas"
    p_code.font.size = Pt(10)
    p_code.font.color.rgb = RGBColor(220, 220, 220)

    add_card(s11, 7.3, 1.4, 5.0, 5.1)
    tb_r = s11.shapes.add_textbox(Inches(7.5), Inches(1.55), Inches(4.6), Inches(4.7))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_r = tf_r.paragraphs[0]
    p_r.text = "Ý NGHĨA PHÂN TÁN"
    p_r.font.bold = True
    p_r.font.size = Pt(12.5)
    p_r.font.color.rgb = C_NAVY

    expl = [
        ("needs: code-quality", "Quan hệ thứ tự nhân quả: chỉ khi phân tích tĩnh thành công mới kích hoạt các worker sau."),
        ("matrix: ['3.10', '3.11', '3.12']", "GitHub Master tự động nhân bản tác vụ thành 3 instances độc lập chạy song song trên 3 máy ảo khác nhau."),
        ("fail-fast: false", "Không hủy các node khác nếu 1 node bị fail, giúp kỹ sư quan sát phản ứng độc lập của từng môi trường."),
        ("Tối ưu hóa thời gian:", "Rút ngắn 60% thời gian thực thi so với chạy tuần tự từng phiên bản.")
    ]
    for h, b in expl:
        p1 = tf_r.add_paragraph()
        p1.text = "• " + h
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p2 = tf_r.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = C_GRAY

    add_guide_cue(s11, "Nguyễn Trung Hiếu", "2 phút", "Giải thích cơ chế ma trận: 1 file cấu hình điều phối 3 máy ảo chạy đồng thời. Chuyển lời cho Tuấn.")
    set_speaker_notes(
        s11,
        presenter="Nguyễn Trung Hiếu -> chuyển tiếp Trương Anh Tuấn",
        duration="2 phút",
        goal="Giải thích cấu hình kỹ thuật CI/CD, chuyển giao sang phần thực nghiệm cho bạn Trương Anh Tuấn.",
        script=(
            "Về cấu hình kỹ thuật, đây là đoạn code YAML quan trọng nhất trong file ci-cd.yml:\n"
            "Nhóm sử dụng từ khóa 'needs: code-quality' để thiết lập quan hệ nhân quả. Khi phân tích tĩnh đạt, chỉ thị 'strategy: matrix' kích hoạt tính toán phân tán: GitHub Master lập tức sinh ra 3 worker instances độc lập chạy Python 3.10, 3.11 và 3.12 trên 3 máy ảo Ubuntu khác nhau.\n"
            "Thuộc tính 'fail-fast: false' giúp chúng em khảo sát được phản ứng độc lập của từng node môi trường.\n"
            "Sau đây, em xin mời bạn Trương Anh Tuấn báo cáo chi tiết kết quả thực nghiệm 5 kịch bản kiểm thử trên hệ thống."
        ),
        key_terms="Strategy Matrix, Parallel Instances, Fail-fast, YAML Workflow Spec."
    )

    # =========================================================================
    # SLIDE 12: CHƯƠNG 3 - KỊCH BẢN 1: ĐỒNG BỘ PHÂN TÁN LÊN REMOTE HUB
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "3.1. KỊCH BẢN 1: ĐỒNG BỘ DỮ LIỆU PHÂN TÁN LÊN REMOTE HUB", "CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM")

    add_card(s12, 1.0, 1.4, 5.4, 5.1)
    tb = s12.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "QUY TRÌNH THAO TÁC THỰC NGHIỆM"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    steps = [
        "Bước 1: Khởi tạo Git repo cục bộ bằng lệnh 'git init'.",
        "Bước 2: Đưa toàn bộ cấu trúc dự án vào staging 'git add .'.",
        "Bước 3: Tạo snapshot commit gốc với mã băm SHA.",
        "Bước 4: Liên kết Remote Hub: 'git remote add origin https://github.com/...'",
        "Bước 5: Đẩy dữ liệu: 'git push -u origin main'."
    ]
    for st in steps:
        p = tf.add_paragraph()
        p.text = "• " + st
        p.font.size = Pt(10.5)
        p.font.color.rgb = C_DARK

    add_card(s12, 6.9, 1.4, 5.4, 5.1, bg_color=C_LIGHT, border_color=C_NAVY)
    tb_img = s12.shapes.add_textbox(Inches(7.1), Inches(3.0), Inches(5.0), Inches(2.0))
    p_i = tb_img.text_frame.paragraphs[0]
    p_i.text = "[KHUNG CHÈN ẢNH CHỤP THỰC TẾ]\n\nẢnh màn hình PowerShell chạy git push thành công và giao diện web GitHub hiển thị đầy đủ code."
    p_i.font.size = Pt(11.5)
    p_i.font.bold = True
    p_i.font.color.rgb = C_GRAY
    p_i.alignment = PP_ALIGN.CENTER

    add_guide_cue(s12, "Trương Anh Tuấn", "1.5 phút", "Báo cáo kịch bản 1: Khởi tạo repo, push qua HTTPS, kích hoạt webhook tự động. Chỉ tay vào ảnh minh chứng.")
    set_speaker_notes(
        s12,
        presenter="Trương Anh Tuấn",
        duration="1.5 phút",
        goal="Trình bày kết quả kịch bản 1, chỉ rõ bằng chứng thực tế trên ảnh chụp màn hình.",
        script=(
            "Kính thưa Thầy và các bạn, em là Trương Anh Tuấn. Em xin báo cáo kết quả thực nghiệm 5 kịch bản kiểm thử trên hệ thống thực tế.\n"
            "Ở Kịch bản 1: Nhóm tiến hành khởi tạo kho lưu trữ phân tán và thực hiện lệnh git push lên GitHub Remote Hub.\n"
            "Như Thầy có thể quan sát trên ảnh chụp màn hình bên phải: Toàn bộ đối tượng nén được truyền tải an toàn qua giao thức HTTPS. GitHub xác nhận nhận đủ dữ liệu và ngay lập tức gửi tín hiệu Webhook để đánh thức chuỗi CI/CD Pipeline."
        ),
        key_terms="Git Push, HTTPS Protocol, Webhook Trigger, Remote Hub Synchronization."
    )

    # =========================================================================
    # SLIDE 13: CHƯƠNG 3 - KỊCH BẢN 2: XUNG ĐỘT GHI ĐỒNG THỜI & HÒA GIẢI
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "3.2. KỊCH BẢN 2: XUNG ĐỘT ĐỒNG THỜI & HÒA GIẢI (MERGE CONFLICT)", "CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM")

    add_card(s13, 1.0, 1.4, 5.4, 5.1)
    tb = s13.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "DIỄN BIẾN TRANH CHẤP TRẠNG THÁI"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_RED
    cf_steps = [
        ("Node A (Dev Rin):", "Tạo nhánh 'feature-node-a', sửa hàm add() trả về float(a + b) -> Merge vào main thành công."),
        ("Node B (Dev Hiếu):", "Tạo nhánh 'feature-node-b' từ cùng gốc main cũ, sửa hàm add() trả về round(a + b, 4)."),
        ("Xung đột xảy ra:", "Khi gộp nhánh B vào main, Git phát hiện cùng 1 dòng bị sửa khác nhau -> Từ chối gộp tự động."),
        ("Hòa giải trạng thái:", "Lập trình viên xem Conflict Markers, thống nhất logic chung và tạo Merge Commit.")
    ]
    for h, b in cf_steps:
        p1 = tf.add_paragraph()
        p1.text = "• " + h
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_card(s13, 6.9, 1.4, 5.4, 5.1, bg_color=C_LIGHT, border_color=C_RED)
    tb_img = s13.shapes.add_textbox(Inches(7.1), Inches(3.0), Inches(5.0), Inches(2.0))
    p_i = tb_img.text_frame.paragraphs[0]
    p_i.text = "[KHUNG CHÈN ẢNH CHỤP THỰC TẾ]\n\nẢnh màn hình terminal báo lỗi 'CONFLICT (content)' và ảnh mở file calculator.py chứa ký hiệu <<<<<<< HEAD trong VS Code."
    p_i.font.size = Pt(11.5)
    p_i.font.bold = True
    p_i.font.color.rgb = C_GRAY
    p_i.alignment = PP_ALIGN.CENTER

    add_guide_cue(s13, "Trương Anh Tuấn", "2 phút", "Đây là điểm nhấn thực nghiệm lớn nhất: giải thích kịch bản xung đột bằng script PowerShell và ảnh conflict markers.")
    set_speaker_notes(
        s13,
        presenter="Trương Anh Tuấn",
        duration="2 phút",
        goal="Làm nổi bật kịch bản kiểm chứng tính toàn vẹn trạng thái trong hệ phân tán, chứng minh không bị ghi đè ngầm.",
        script=(
            "Kịch bản 2 là phép thử quan trọng nhất về tính toàn vẹn trạng thái phân tán. Chúng em sử dụng script 'simulate_conflict.ps1' để tái hiện tình huống:\n"
            "Dev Rin sửa hàm add thành số thực float; Dev Hiếu sửa hàm add thành làm tròn 4 chữ số thập phân trên hai nhánh rẽ riêng biệt.\n"
            "Khi gộp nhánh thứ hai vào main, Git lập tức phát hiện xung đột và từ chối tự động ghi đè. Thông báo 'CONFLICT (content)' xuất hiện trên terminal như ảnh chụp bên phải.\n"
            "Các ký hiệu Conflict Markers xuất hiện rõ ràng trong file calculator.py. Hai kỹ sư tiến hành họp bàn, thống nhất giữ logic chung và tạo ra Merge Commit, đưa hệ thống về trạng thái đồng thuận phân tán."
        ),
        key_terms="Conflict (content), Conflict Markers, Consensus, Merge Commit."
    )

    # =========================================================================
    # SLIDE 14: CHƯƠNG 3 - KỊCH BẢN 3: MATRIX TESTING SONG SONG
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "3.3. KỊCH BẢN 3: TÍNH TOÁN SONG SONG TRÊN 3 WORKER RUNNERS", "CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM")

    add_card(s14, 1.0, 1.4, 5.4, 5.1)
    tb = s14.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "KẾT QUẢ ĐIỀU PHỐI PHÂN TÁN"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    m_info = [
        ("Worker Node 1:", "Ubuntu 22.04 | Python 3.10 | 7/7 tests PASS (16 giây)"),
        ("Worker Node 2:", "Ubuntu 22.04 | Python 3.11 | 7/7 tests PASS (15 giây)"),
        ("Worker Node 3:", "Ubuntu 22.04 | Python 3.12 | 7/7 tests PASS (18 giây)"),
        ("Tính độc lập:", "Mỗi runner sở hữu hostname, IP ảo và môi trường tách biệt hoàn toàn."),
        ("Độ trễ tổng thể:", "Nhờ chạy song song, tổng thời gian chỉ bằng thời gian của worker chậm nhất (~18s).")
    ]
    for h, b in m_info:
        p1 = tf.add_paragraph()
        p1.text = "✔ " + h
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_card(s14, 6.9, 1.4, 5.4, 5.1, bg_color=C_LIGHT, border_color=C_NAVY)
    tb_img = s14.shapes.add_textbox(Inches(7.1), Inches(3.0), Inches(5.0), Inches(2.0))
    p_i = tb_img.text_frame.paragraphs[0]
    p_i.text = "[KHUNG CHÈN ẢNH CHỤP THỰC TẾ]\n\nẢnh màn hình tab Actions trên GitHub hiển thị 3 nhánh Worker Python 3.10, 3.11, 3.12 đều xanh (Success)."
    p_i.font.size = Pt(11.5)
    p_i.font.bold = True
    p_i.font.color.rgb = C_GRAY
    p_i.alignment = PP_ALIGN.CENTER

    add_guide_cue(s14, "Trương Anh Tuấn", "1.5 phút", "Nhấn mạnh số liệu thực tế: 3 máy ảo chạy đồng thời, tổng thời gian ~18 giây, giảm 60% so với chạy tuần tự.")
    set_speaker_notes(
        s14,
        presenter="Trương Anh Tuấn",
        duration="1.5 phút",
        goal="Trình bày số liệu thực nghiệm đo đạc được, chứng minh lợi ích tính toán song song.",
        script=(
            "Kịch bản 3 minh chứng tính toán song song phân tán (Parallel Distributed Execution):\n"
            "Như trên hình ảnh minh chứng tab Actions: Hệ thống đã khởi tạo 3 Worker độc lập trên 3 phiên bản Python 3.10, 3.11 và 3.12.\n"
            "Mỗi máy ảo sở hữu Hostname riêng biệt, chạy độc lập 7 bài unit test và đều đạt 100% pass.\n"
            "Điều đáng chú ý là thay vì mất gần 50 giây nếu chạy tuần tự, tổng thời gian kiểm thử chỉ mất 18 giây - tương đương với thời gian của worker chạy chậm nhất. Điều này chứng minh hiệu quả tối ưu hóa tài nguyên phân tán."
        ),
        key_terms="Parallel Execution, Independent Hostnames, Latency Optimization, Matrix Results."
    )

    # =========================================================================
    # SLIDE 15: CHƯƠNG 3 - KỊCH BẢN 4: CƠ CHẾ NGẮT MẠCH (FAIL-FAST)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "3.4. KỊCH BẢN 4: PHÁT HIỆN LỖI VÀ NGẮT MẠCH (FAIL-FAST)", "CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM")

    add_card(s15, 1.0, 1.4, 5.4, 5.1)
    tb = s15.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "CƠ CHẾ BẢO VỆ NHÁNH CHÍNH (CIRCUIT BREAKER)"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_RED
    ff_points = [
        ("Mô phỏng sự cố:", "Một lập trình viên cố tình commit bài test sai logic (10 + 20 == 999)."),
        ("Runner phát hiện:", "Worker thực thi bài test lập tức bắt lỗi assertion và trả về exit code 1."),
        ("Ngắt mạch ngay lập tức:", "Toàn bộ Job tiếp theo (Đóng gói, Triển khai) bị HỦY BỎ hoàn toàn."),
        ("Khóa hợp nhất:", "Pull Request bị chuyển sang trạng thái ĐỎ, ngăn chặn mã lỗi phát tán vào hệ sinh thái.")
    ]
    for h, b in ff_points:
        p1 = tf.add_paragraph()
        p1.text = "✖ " + h
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_card(s15, 6.9, 1.4, 5.4, 5.1, bg_color=C_LIGHT, border_color=C_RED)
    tb_img = s15.shapes.add_textbox(Inches(7.1), Inches(3.0), Inches(5.0), Inches(2.0))
    p_i = tb_img.text_frame.paragraphs[0]
    p_i.text = "[KHUNG CHÈN ẢNH CHỤP THỰC TẾ]\n\nẢnh màn hình GitHub Actions báo lỗi MÀU ĐỎ và log chi tiết FAILED từ pytest."
    p_i.font.size = Pt(11.5)
    p_i.font.bold = True
    p_i.font.color.rgb = C_GRAY
    p_i.alignment = PP_ALIGN.CENTER

    add_guide_cue(s15, "Trương Anh Tuấn", "2 phút", "Nhấn mạnh cơ chế Circuit Breaker: khi test fail, pipeline chuyển màu ĐỎ, hủy lập tức các job sau để bảo vệ hệ thống.")
    set_speaker_notes(
        s15,
        presenter="Trương Anh Tuấn",
        duration="2 phút",
        goal="Chứng minh cơ chế chịu lỗi và an toàn hệ thống (Fault Tolerance & Safety).",
        script=(
            "Kịch bản 4 là phép thử về khả năng chịu lỗi và tự bảo vệ của hệ thống: Nếu một node commit code lỗi thì điều gì xảy ra?\n"
            "Chúng em cố tình sửa một assert sai logic. Ngay lập tức, Worker phát hiện và trả về mã lỗi. Giao diện GitHub Actions đổi sang MÀU ĐỎ như Thầy thấy trên màn hình.\n"
            "Đặc biệt, cơ chế Ngắt mạch (Circuit Breaker) dựa trên quan hệ phụ thuộc 'needs' lập tức HỦY BỎ hoàn toàn các Job Build và Deploy tiếp theo. Pull Request bị khóa, ngăn chặn mã lỗi phát tán sang các máy chủ khác."
        ),
        key_terms="Circuit Breaker Pattern, Fail-Fast, Cascading Failure Prevention, Red Pipeline."
    )

    # =========================================================================
    # SLIDE 16: CHƯƠNG 3 - BẢNG TỔNG HỢP CÁC PHÉP THỬ THỰC NGHIỆM
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "3.5. BẢNG TỔNG HỢP KẾT QUẢ CÁC PHÉP THỬ", "CHƯƠNG 3: TRIỂN KHAI THỰC NGHIỆM")

    table_shape = s16.shapes.add_table(rows=6, cols=4, left=Inches(1.0), top=Inches(1.5), width=Inches(11.333), height=Inches(4.8))
    tbl = table_shape.table
    tbl.columns[0].width = Inches(0.8)
    tbl.columns[1].width = Inches(3.8)
    tbl.columns[2].width = Inches(5.2)
    tbl.columns[3].width = Inches(1.533)

    t_headers = ["STT", "Nội dung phép thử", "Kết quả quan sát thực tế", "Đánh giá"]
    for c_idx, th in enumerate(t_headers):
        cell = tbl.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_NAVY
        p = cell.text_frame.paragraphs[0]
        p.text = th
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = C_WHITE
        p.alignment = PP_ALIGN.CENTER

    t_rows = [
        ("1", "Đồng bộ phân tán lên Remote Hub", "100% đối tượng được tải lên an toàn, kích hoạt webhook chuẩn", "ĐẠT"),
        ("2", "Xung đột đồng thời (Merge Conflict)", "Phát hiện xung đột chuẩn xác; ngăn ghi đè; hòa giải 3-way thành công", "ĐẠT"),
        ("3", "Tính toán song song (Matrix Testing)", "3 Worker chạy đồng thời trên 3 phiên bản Python, 100% test pass", "ĐẠT"),
        ("4", "Cơ chế chịu lỗi (Fail-Fast)", "Phát hiện test sai; ngắt ngay lập tức chuỗi build/deploy; khóa nhánh", "ĐẠT"),
        ("5", "Đóng gói phát hành tự động (CD)", "Tạo thành công gói Artifacts nén; xuất log triển khai hoàn tất", "ĐẠT")
    ]

    for r_idx, (col0, col1, col2, col3) in enumerate(t_rows):
        for c_idx, val in enumerate([col0, col1, col2, col3]):
            cell = tbl.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_LIGHT if r_idx % 2 == 0 else C_WHITE
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            if c_idx in [0, 3]:
                p.alignment = PP_ALIGN.CENTER
                if c_idx == 3:
                    p.font.bold = True
                    p.font.color.rgb = RGBColor(0, 128, 0)
            else:
                p.alignment = PP_ALIGN.LEFT
                p.font.color.rgb = C_DARK

    add_guide_cue(s16, "Trương Anh Tuấn", "1.5 phút", "Tóm lược 5 phép thử đều ĐẠT 100%, nhấn mạnh tính thực chứng khoa học. Chuyển lời kết cho Hoài Rin.")
    set_speaker_notes(
        s16,
        presenter="Trương Anh Tuấn -> chuyển tiếp Lê Văn Hoài Rin",
        duration="1.5 phút",
        goal="Tổng kết kết quả thực nghiệm một cách tự tin, khẳng định độ tin cậy của bài làm.",
        script=(
            "Kính thưa Thầy, bảng trên đây tổng hợp toàn bộ 5 phép thử thực nghiệm mà nhóm đã tiến hành.\n"
            "Cả 5/5 kịch bản đều đạt kết quả xuất sắc, phản ánh trung thực nguyên lý của hệ phân tán: từ tính bất biến dữ liệu, giải quyết tranh chấp ghi, đến tính toán song song và khả năng chịu lỗi.\n"
            "Sau đây, em xin kính mời bạn Lê Văn Hoài Rin, trưởng nhóm, phát biểu phần Kết luận và bài học kinh nghiệm."
        ),
        key_terms="Bảng tổng hợp thực nghiệm, Đạt 100%, Tính thực chứng khoa học."
    )

    # =========================================================================
    # SLIDE 17: KẾT LUẬN & BÀI HỌC KINH NGHIỆM
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "KẾT LUẬN VÀ BÀI HỌC KINH NGHIỆM", "TỔNG KẾT ĐỒ ÁN")

    add_card(s17, 1.0, 1.4, 5.4, 5.1)
    tb = s17.shapes.add_textbox(Inches(1.2), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "KẾT QUẢ ĐẠT ĐƯỢC"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    res = [
        ("Về mặt lý thuyết:", "Hệ thống hóa bản chất phân tán của Git (DAG, SHA, 3-Way Merge, quan hệ nhân quả Causal Ordering) và kiến trúc Master-Worker của GitHub Actions."),
        ("Về mặt sản phẩm:", "Xây dựng trọn bộ REST API, bộ kiểm thử đơn vị, file cấu hình CI/CD và script mô phỏng xung đột đồng thời."),
        ("Về mặt thực nghiệm:", "Hoàn thành 5/5 phép thử thực tế, chứng minh tính toàn vẹn trạng thái và tính toán song song đa node.")
    ]
    for h, b in res:
        p1 = tf.add_paragraph()
        p1.text = "✔ " + h
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_card(s17, 6.9, 1.4, 5.4, 5.1)
    tb = s17.shapes.add_textbox(Inches(7.1), Inches(1.55), Inches(5.0), Inches(4.7))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "BÀI HỌC TRONG MÔN HỆ PHÂN TÁN"
    p.font.bold = True
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_NAVY
    lessons = [
        ("Full Replica loại bỏ SPOF:", "Bản sao đầy đủ giúp hệ thống phân tán duy trì tính sẵn sàng cao tuyệt đối ngay cả khi mất kết nối mạng."),
        ("Xung đột là tất yếu:", "Trong hệ phân tán không có đồng hồ tuyệt đối; cần dựa vào đồ thị nhân quả DAG để phát hiện tranh chấp ghi đồng thời."),
        ("Ngắt mạch (Circuit Breaker):", "Là nguyên tắc cốt lõi giúp ngăn ngừa sự cố lan truyền (cascading failures) trong các chuỗi xử lý tự động.")
    ]
    for h, b in lessons:
        p1 = tf.add_paragraph()
        p1.text = "💡 " + h
        p1.font.bold = True
        p1.font.size = Pt(10.5)
        p2 = tf.add_paragraph()
        p2.text = "   " + b
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_GRAY

    add_guide_cue(s17, "Lê Văn Hoài Rin", "1.5 phút", "Khẳng định 3 bài học lớn: Full replica loại bỏ SPOF, Xung đột là tất yếu, và Ngắt mạch là nguyên tắc an toàn.")
    set_speaker_notes(
        s17,
        presenter="Lê Văn Hoài Rin",
        duration="1.5 phút",
        goal="Chốt lại ý nghĩa học thuật môn Hệ phân tán, khẳng định giá trị đề tài.",
        script=(
            "Kính thưa Thầy và các bạn, qua quá trình nghiên cứu và thực hiện đề tài, Nhóm 15 rút ra 3 bài học lớn gắn liền với môn Hệ phân tán:\n"
            "Bài học 1: Mô hình Bản sao đầy đủ (Full Replica) là giải pháp tối ưu để triệt tiêu hoàn toàn điểm lỗi đơn SPOF và bảo đảm tính sẵn sàng cao;\n"
            "Bài học 2: Tranh chấp ghi đồng thời là điều tất yếu trong môi trường phân tán; việc hiểu rõ cấu trúc DAG và quan hệ nhân quả giúp chúng ta thiết kế giải pháp hòa giải an toàn;\n"
            "Và Bài học 3: Cơ chế ngắt mạch (Circuit Breaker) là nguyên tắc sống còn để bảo vệ hệ sinh thái phân tán khỏi lỗi lan truyền."
        ),
        key_terms="Full Replica, Cascading Failures, Circuit Breaker, Causal Ordering."
    )

    # =========================================================================
    # SLIDE 18: LỜI CẢM ƠN & HỎI ĐÁP (Q&A)
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    bg18 = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg18.fill.solid()
    bg18.fill.fore_color.rgb = C_NAVY
    bg18.line.color.rgb = C_NAVY

    tb_end = s18.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.333), Inches(3.0))
    tf_e = tb_end.text_frame
    p_e1 = tf_e.paragraphs[0]
    p_e1.text = "CẢM ƠN THẦY VÀ CÁC BẠN ĐÃ LẮNG NGHE!"
    p_e1.font.size = Pt(32)
    p_e1.font.bold = True
    p_e1.font.color.rgb = C_WHITE
    p_e1.alignment = PP_ALIGN.CENTER

    p_e2 = tf_e.add_paragraph()
    p_e2.text = "NHÓM 15 - MÔN HỆ PHÂN TÁN (CS420G)"
    p_e2.font.size = Pt(18)
    p_e2.font.bold = True
    p_e2.font.color.rgb = RGBColor(100, 200, 255)
    p_e2.alignment = PP_ALIGN.CENTER

    p_e3 = tf_e.add_paragraph()
    p_e3.text = "\n[PHIÊN HỎI ĐÁP - Q&A]"
    p_e3.font.size = Pt(22)
    p_e3.font.bold = True
    p_e3.font.color.rgb = RGBColor(255, 230, 150)
    p_e3.alignment = PP_ALIGN.CENTER

    add_guide_cue(s18, "Cả nhóm 15", "5-10 phút", "Cảm ơn Thầy và các bạn, chuyển sang phiên trả lời câu hỏi phản biện từ Giảng viên.")
    set_speaker_notes(
        s18,
        presenter="Cả nhóm 15 (Lê Văn Hoài Rin, Nguyễn Trung Hiếu, Trương Anh Tuấn)",
        duration="5 - 10 phút",
        goal="Sẵn sàng trả lời các câu hỏi phản biện của Giảng viên.",
        script=(
            "Nhóm 15 xin chân thành cảm ơn Thầy Nguyễn Minh Nhật và toàn thể các bạn sinh viên đã chú ý lắng nghe bài báo cáo của nhóm chúng em.\n"
            "Sau đây, nhóm chúng em rất mong nhận được những nhận xét, góp ý và câu hỏi phản biện từ Thầy và các bạn để nhóm làm rõ hơn các vấn đề học thuật của đề tài. Nhóm em xin chân thành cảm ơn!"
        ),
        key_terms="Q&A Session, Phản biện đồ án."
    )

    # Thử lưu vào file gốc, nếu bị khóa do đang mở thì lưu vào file có tên mới
    target_primary = r"d:\HocKyI_Nam4\CS_420_G\DA_HePhanTan_ver4\Slide_ThuyetTrinh_Nhom15_CS420G.pptx"
    target_backup = r"d:\HocKyI_Nam4\CS_420_G\DA_HePhanTan_ver4\Slide_ThuyetTrinh_Nhom15_CS420G_CoHuongDan.pptx"
    
    try:
        prs.save(target_primary)
        print(f"[+] Tạo thành công và ghi đè trực tiếp tại: {target_primary}")
    except PermissionError:
        prs.save(target_backup)
        print(f"[!] File gốc đang được mở trong editor, đã lưu phiên bản có đầy đủ hướng dẫn tại: {target_backup}")

if __name__ == "__main__":
    create_deck()
