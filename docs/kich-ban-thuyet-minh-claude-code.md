# Kịch bản thuyết minh — Ứng dụng Claude Code trong phát triển phần mềm

**Dùng cho:** người trình bày của Ban KHCNĐMST, đọc song song với tệp
`Claude Code EVNGENCO1 - Trinh chieu.html` (23 slide).
**Thời lượng:** khoảng 32 phút nói, chừa 8 phút hỏi đáp.

## Cách dùng tài liệu này

Phần trong khung trích dẫn là lời nói, viết sẵn để đọc trôi được thành câu.
Anh/chị không cần thuộc lòng, nhưng nên đọc to một lượt trước buổi để quen nhịp.
Phần **Lưu ý** là chỉ dẫn thao tác và chỗ cần nhấn giọng.

Chỗ nào có dấu `[...]` là chỗ cần anh/chị điền trải nghiệm thật của Ban. Tôi cố
tình để trống thay vì bịa, vì một tình huống thật của chính người trình bày có
sức thuyết phục hơn mọi số liệu trên slide.

**Chuẩn bị trước:** mở sẵn tệp slide, nhấn **F** để vào chế độ trình chiếu toàn
màn hình. Nếu định trình diễn trực tiếp, mở sẵn một cửa sổ terminal thứ hai đã
đăng nhập, đặt sẵn ở một thư mục dự án thật.

---

## Mở đầu

### Slide 1 — Bìa · ~60 giây

> Chào anh chị. Hôm nay Ban Khoa học Công nghệ và Đổi mới Sáng tạo xin chia sẻ
> về Claude Code, một công cụ lập trình có hỗ trợ AI.
>
> Trước khi vào nội dung, tôi muốn nói rõ một điều để anh chị khỏi hiểu nhầm
> ngay từ đầu. Đây không phải buổi giới thiệu một công cụ gợi ý mã kiểu mới.
> Claude Code làm việc theo cách khác hẳn, và chính chỗ khác đó là lý do buổi
> hôm nay đáng thời gian của anh chị.
>
> Mục tiêu của tôi rất cụ thể: hết buổi này, anh chị về máy mình cài được, chạy
> được, và quan trọng nhất là biết giao việc gì cho nó thì an toàn.

**Lưu ý:** đừng vội chuyển slide. Câu "không phải công cụ gợi ý mã" là câu định
khung cả buổi, để nó đọng một nhịp rồi mới đi tiếp.

### Slide 2 — Mục tiêu · ~90 giây

> Bốn điều anh chị sẽ mang về.
>
> Thứ nhất, cài đặt được trên máy mình, bất kể Windows hay macOS, chỉ một dòng
> lệnh.
>
> Thứ hai, và đây là điều tôi muốn anh chị nhớ nhất, hiểu đúng Claude Code khác
> công cụ gợi ý mã ở chỗ nào. Hiểu sai điểm này là nguyên nhân chính khiến nhiều
> người dùng vài hôm rồi bỏ, vì thấy "cũng chẳng hơn gì".
>
> Thứ ba, ba nguyên tắc để kết quả nó làm ra dùng được, chứ không phải đống mã
> phải sửa lại từ đầu.
>
> Thứ tư, phương án cho anh em chưa có tài khoản. Phần này tôi để cuối, nhưng ai
> đang ở hoàn cảnh đó thì yên tâm là có đường đi.

**Lưu ý:** không đọc mục lục bên phải. Chỉ cần một câu: "Chúng ta đi theo bảy
phần, khoảng ba mươi phút."

---

## Phần 1 — Tổng quan (slide 3–6)

### Slide 3 — Claude là gì · ~75 giây

> Claude là họ mô hình ngôn ngữ lớn của Anthropic. Hiện có bốn mô hình, khác
> nhau ở độ sâu suy luận và chi phí.
>
> Anh chị không cần nhớ hết. Chỉ cần nhớ một điều: Opus 5.5 là mặc định cho việc
> lập trình, và cứ để nguyên mặc định là được. Khi nào gặp bài toán rối, nhiều
> bước phụ thuộc nhau, thì đổi sang Fable. Khi nào làm việc đơn giản và muốn
> tiết kiệm thì dùng Haiku.
>
> Con số đáng chú ý là một triệu token ngữ cảnh. Nói cho dễ hình dung, nó đủ để
> đọc và giữ trong đầu một kho mã nguồn cỡ lớn cùng lúc, chứ không phải chỉ một
> vài tệp.

**Lưu ý:** slide này đi nhanh. Nếu thiếu thời gian, đây là một trong hai slide
cắt được mà không ảnh hưởng mạch chính.

### Slide 4 — Khác biệt · ~90 giây

Đây là slide quan trọng nhất của phần đầu. Nói chậm.

> Bên trái là công cụ gợi ý trong dòng, kiểu anh chị đang gõ thì nó đoán đoạn
> tiếp theo. Nó chỉ nhìn thấy tệp đang mở. Phần việc còn lại vẫn là của kỹ sư:
> tự mở tệp, tự tìm chỗ sửa, tự chạy kiểm thử, tự xử lý lỗi.
>
> Bên phải là Claude Code. Nó nhìn thấy cả dự án. Nó tự tìm tệp, sửa nhiều tệp
> một lúc, tự chạy lệnh, và tự xử lý lỗi cho đến khi đạt. Phần việc của kỹ sư
> đổi hẳn: mô tả kết quả cần đạt, rồi duyệt kế hoạch và duyệt kết quả.
>
> Tôi muốn nhấn mạnh dòng cuối: khác biệt nằm ở phạm vi hoạt động, không phải
> công cụ nào tốt hơn. Hai thứ này giải hai bài toán khác nhau.

**Lưu ý:** nếu trong phòng có người đang dùng công cụ gợi ý mã, nói thêm một câu
rằng hai thứ dùng chung được, không phải chọn một bỏ một.

### Slide 5 — Bốn cách dùng · ~75 giây

> Cùng một lõi Claude Code, dùng được qua bốn đường.
>
> Dòng lệnh là bản đầy đủ nhất, và là bản tôi khuyến nghị cho kỹ sư. Ứng dụng
> Desktop hợp với người ngại terminal, xem được diff trực quan và chạy nhiều
> phiên song song. Ngoài ra có bản cắm vào VS Code và JetBrains, và bản chạy
> thẳng trên web không cần cài gì.
>
> Điểm đáng giá là tất cả dùng chung một lõi. Tệp cấu hình CLAUDE.md anh chị
> viết một lần thì chỗ nào cũng đọc được.

**Lưu ý:** đây là slide thứ hai cắt được nếu thiếu thời gian.

### Slide 6 — Vòng lặp · ~90 giây

> Claude Code làm việc theo một vòng lặp ba bước: thu thập ngữ cảnh, thực thi,
> rồi kiểm chứng. Chưa đạt thì quay lại bước một.
>
> Anh chị nhìn phiên làm việc bên phải. Tôi yêu cầu sửa một kiểm thử đang hỏng,
> và nói rõ là không được đổi API. Nó đọc hai tệp liên quan, sửa một chỗ, chạy
> kiểm thử. Còn một ca hỏng. Nó sửa tiếp một dòng, chạy lại, bốn mươi tám trên
> bốn mươi tám ca đạt. Rồi mới báo xong.
>
> Chỗ đáng chú ý không phải là nó sửa được. Chỗ đáng chú ý là **nó tự biết mình
> chưa xong**, vì có bộ kiểm thử để tự chấm. Ý này sẽ quay lại ở nguyên tắc số
> hai.

**Lưu ý:** đây là chỗ tốt nhất để trình diễn trực tiếp. Nếu có terminal mở sẵn,
chạy một yêu cầu thật ở đây thay vì nói theo slide. Nếu máy chiếu hoặc mạng
không chắc chắn thì cứ bám slide, vì slide đã đủ kể hết câu chuyện.

---

## Phần 2 — Ứng dụng và ba nguyên tắc (slide 7–10)

### Slide 7 — Giao việc gì · ~90 giây

> Sáu nhóm việc giao được. Tôi không đọc hết, chỉ nêu ba nhóm anh chị dùng được
> ngay tuần này.
>
> Đọc hiểu mã nguồn: vào một kho mã chưa quen, hỏi nghiệp vụ này xử lý ở đâu.
> Bổ sung kiểm thử: phần mã đã chạy lâu nay nhưng chưa ai viết kiểm thử. Và sửa
> lỗi kéo theo nhiều tệp, kiểu đổi một cấu trúc dữ liệu là phải sửa đồng bộ cả
> chục chỗ.
>
> Phần dưới mới là phần quan trọng. "Cải thiện hiệu năng hệ thống" là một yêu
> cầu vô nghĩa, nó sẽ sửa lung tung. Còn "API orders phản hồi mất ba giây, tìm
> nguyên nhân và xử lý" thì nó làm được. Yêu cầu càng cụ thể, kết quả càng chính
> xác.

**Lưu ý:** [nếu Ban đã có ví dụ thật, thay cặp ví dụ ở cuối slide bằng một tình
huống trong dự án của đơn vị — hiệu quả hơn hẳn ví dụ chung chung].

### Slide 8 — Nguyên tắc 1: duyệt kế hoạch · ~110 giây

> Nguyên tắc thứ nhất: duyệt kế hoạch trước khi cho thực thi.
>
> Bấm Shift Tab để bật chế độ lập kế hoạch. Ở chế độ này nó chỉ đọc và đề xuất,
> chưa sửa một dòng nào. Nó khảo sát mã liên quan, rồi trình bày sẽ sửa gì, ở
> đâu. Anh chị duyệt xong nó mới làm, làm xong thì ghi lại thành commit.
>
> Hai con số ở giữa là cách tôi hình dung giá trị của bước này. Đọc và duyệt một
> kế hoạch mười dòng mất chừng một phút. Nếu bỏ qua bước đó, cái anh chị phải rà
> là bốn trăm dòng thay đổi.
>
> Phát hiện sai lệch ở bước lập kế hoạch thì gần như không tốn công sửa. Phát
> hiện ở bước cuối thì phải làm lại từ đầu.

**Lưu ý:** hai con số mười và bốn trăm là con số minh hoạ cho dễ hình dung,
không phải số đo. Nếu có ai hỏi thì nói thẳng như vậy.

### Slide 9 — Nguyên tắc 2: tiêu chí kiểm chứng · ~110 giây

> Nguyên tắc thứ hai, và theo tôi là nguyên tắc quyết định: khai báo tiêu chí để
> công cụ tự đánh giá kết quả.
>
> Tài liệu chính thức liệt kê bốn nguyên nhân thường gặp khi một phiên làm việc
> không đạt kỳ vọng. Một trong số đó là công cụ báo hoàn thành trong khi thực ra
> chưa đạt, đơn giản vì nó không có cách nào tự kiểm chứng.
>
> Cách xử lý nằm ở khung bên trái. Trong tệp CLAUDE.md, anh chị viết rõ: sau mỗi
> thay đổi mã nguồn, chạy lint và chạy kiểm thử; chỉ được báo hoàn thành khi cả
> hai lệnh đều thành công. Có câu đó, nó sẽ tự lặp đến khi đạt.
>
> Nhưng phải phân biệt hai loại tiêu chí. Bên phải: kiểm thử đạt hay không đạt,
> biên dịch thành công hay không, kiểu dữ liệu hợp lệ hay không — những thứ này
> máy tự chấm được. Còn giao diện đẹp hay xấu, câu chữ ổn chưa, kiến trúc hợp lý
> chưa — những thứ này bắt buộc phải có người thẩm định. Không giao cho máy được.

### Slide 10 — Nguyên tắc 3: quyền dừng · ~110 giây

> Nguyên tắc thứ ba: giữ quyền dừng và quay lui ở mọi thời điểm.
>
> Anh chị xem phiên bên trái. Tôi yêu cầu bổ sung kiểm thử cho module báo cáo.
> Nó đọc tệp, thêm kiểm thử — đúng yêu cầu. Nhưng đến dòng thứ ba nó bắt đầu sửa
> cart.ts, tức là sửa mã nguồn, không phải thêm kiểm thử. Đi lệch rồi.
>
> Tôi bấm Escape. Nó dừng ngay. Tôi nói lại cho rõ: không sửa cart.ts, chỉ thêm
> kiểm thử. Rồi dùng lệnh rewind để khôi phục tệp nó đã lỡ sửa. Chạy lại, mười
> hai trên mười hai ca đạt.
>
> Escape là phím quan trọng nhất cần nhớ trong cả buổi hôm nay. Nó thể hiện đúng
> quan hệ làm việc: anh chị điều hành phiên làm việc, không phải ngồi xem.

**Lưu ý:** nhấn mạnh chữ Escape. Nếu chỉ có một điều người nghe mang về được thì
nên là điều này.

---

## Phần 3 — Cài đặt và tập lệnh (slide 11–14)

### Slide 11 — Cài đặt · ~80 giây

> Cài đặt chỉ một dòng lệnh.
>
> Trên Windows, mở PowerShell, dán dòng irm. Trên macOS và Linux, mở Terminal,
> dán dòng curl. Nếu máy do bộ phận Công nghệ thông tin quản lý tập trung thì
> cài qua WinGet.
>
> Ai không quen terminal thì tải ứng dụng Claude Desktop, trong đó đã kèm sẵn
> Claude Code, không cần cài riêng.
>
> Một điều cần nói trước: Claude Code không dùng được với gói miễn phí.

**Lưu ý:** nếu có người hỏi về tài khoản và chi phí, trả lời ngắn gọn ngoài
slide: [Ban trả lời theo tình hình cấp phát thực tế của đơn vị].

### Slide 12 — Khởi tạo · ~80 giây

> Ba bước cho phiên đầu tiên. Vào thư mục dự án, gõ claude, lần đầu nó mở trình
> duyệt để xác thực. Rồi gõ lệnh init.
>
> Lệnh init sinh ra tệp CLAUDE.md. Đây là tệp quan trọng nhất trong cả quy
> trình. Nó lưu quy ước viết mã của dự án, lệnh chạy kiểm thử, và những khu vực
> hạn chế sửa. Mọi phiên làm việc sau đều nạp tệp này.
>
> Hai lưu ý. Giữ tệp dưới hai trăm dòng, viết dài quá thì nó tuân thủ kém đi và
> dễ bỏ sót. Và nhớ rằng đây là ngữ cảnh, không phải cưỡng chế: khai báo giúp
> tăng mức tuân thủ chứ không bảo đảm tuyệt đối, kết quả vẫn phải rà.

### Slide 13 — Các lệnh thường dùng · ~80 giây

> Mười lệnh, tôi nêu bốn cái anh chị dùng hằng ngày.
>
> Lệnh init cho lần đầu. Lệnh clear khi xong một việc và chuyển sang việc khác
> không liên quan — cái này nên tập thành thói quen, ngữ cảnh sạch thì câu trả
> lời tốt hơn và rẻ hơn. Lệnh diff để xem lại những gì vừa thay đổi. Lệnh rewind
> để quay lui.
>
> Khung lưu ý phía dưới tôi để riêng vì nó hay gây mất thời gian. Nhiều hướng
> dẫn trên mạng đã cũ. Phím tắt thăng đã bỏ, nay dùng lệnh memory. Các cụm think
> hard, think harder không còn là từ khoá nâng mức suy luận nữa, riêng ultrathink
> thì vẫn còn tác dụng. Và tài liệu chính thức nay ở code.claude.com, không phải
> địa chỉ cũ.

**Lưu ý:** khung này là chỗ dễ bị hỏi vặn nhất. Nội dung đã đối chiếu với tài
liệu chính thức, cứ tự tin.

### Slide 14 — Thao tác nhập liệu · ~70 giây

> Bốn thao tác gõ nhanh. Dấu a còng để chỉ đích danh tệp cần đọc. Escape để
> dừng. Shift Tab để đổi chế độ. Và kéo thả ảnh vào, chẳng hạn ảnh chụp màn hình
> lỗi hoặc bản thiết kế giao diện.
>
> Nhưng dòng dưới cùng mới là điều tôi muốn anh chị nhớ: câu chữ của yêu cầu
> quan trọng hơn mọi phím tắt. Nêu rõ kết quả cần đạt và cách kiểm chứng.

---

## Phần 4 — Bộ công cụ AgentKit (slide 15–17)

### Slide 15 — AgentKit là gì · ~80 giây

> Phần này nói về AgentKit, bộ công cụ Ban đang dùng.
>
> AgentKit không thay thế Claude Code. Nó là bộ quy trình cài thêm vào, đóng gói
> quy ước làm việc của đơn vị thành các lệnh có sẵn.
>
> Giá trị nằm ở ba chỗ. Quy trình thống nhất: cùng một lệnh cho ra cùng một
> trình tự, không phụ thuộc vào việc ai đặt câu hỏi khéo hơn ai. Quy ước dùng
> chung: chuẩn mã nguồn, lệnh kiểm thử, giới hạn an toàn khai báo một lần cho cả
> dự án. Và không khoá vào một công cụ: cùng bộ kỹ năng đó chạy được trên bảy
> công cụ AI khác nhau.
>
> Bốn khái niệm cần biết: Kit là gói nội dung, Skill là quy trình gọi bằng lệnh
> ak, Agent là tác tử làm một nhiệm vụ, Hook là thứ tự kích hoạt tại mốc quy
> định.

**Lưu ý:** câu trích cuối slide — "hook không phải là cơ chế bảo đảm an toàn" —
nên nói rõ một nhịp: hook chặn được thao tác, nhưng đừng coi nó là hàng rào bảo
mật.

### Slide 16 — Quy trình năm bước · ~80 giây

> Quy trình khuyến nghị gồm năm bước, chạy tuần tự: xác định mục tiêu, lập kế
> hoạch, triển khai, kiểm thử, rà soát.
>
> Điều quan trọng nằm ở dòng cuối: chạy từng bước một, đừng gộp cả quy trình vào
> một yêu cầu. Gộp bước thì mất hết các điểm dừng kiểm soát, mà điểm dừng mới
> chính là mục đích của quy trình này.

### Slide 17 — Bốn lệnh dùng hằng ngày · ~90 giây

> Đi sâu vào bốn lệnh anh chị dùng nhiều nhất.
>
> Lệnh brainstorm chốt bốn điều trước khi bắt tay: kết quả cần đạt, ràng buộc,
> việc không làm, và tiêu chí nghiệm thu. Dùng khi mở đầu một việc nhiều bước,
> hoặc khi còn hơn một cách làm phải chọn.
>
> Lệnh plan chia việc thành các pha có tiêu chí nghiệm thu, rồi ghi kế hoạch ra
> tệp. Dùng khi việc cần chia pha hoặc cần quyết định kiến trúc.
>
> Lệnh cook thực thi đúng phạm vi đã duyệt, tự chạy kiểm chứng, tự sửa hồi quy
> do chính nó gây ra rồi chạy lại. Dùng khi phạm vi đã rõ.
>
> Lệnh code-review soát lỗi và chỗ thiếu kiểm chứng. Lưu ý: nó chỉ đọc và báo
> cáo, không tự sửa, không tự hợp nhất.
>
> Dòng cuối là chi tiết thực dụng nhất: plan ghi kế hoạch ra tệp, rồi cook nhận
> đúng đường dẫn tệp đó mà làm. Hai lệnh nối thẳng vào nhau.

---

## Phần 5 — Bài viết thực tế (slide 18–20)

Ba slide này đi nhanh, mỗi slide khoảng bảy mươi giây. Mục đích là cho anh em
thấy đây không phải kinh nghiệm riêng của Ban mà có nguồn kiểm chứng được.

### Slide 18 — Bài 1: cách các nhóm của Anthropic dùng · ~70 giây

> Bài thứ nhất là của chính Anthropic, kể cách các nhóm nội bộ họ dùng.
>
> Nhóm Sản phẩm dùng nó làm điểm khởi đầu cho mọi việc lập trình, để xác định
> cần đọc tệp nào trước khi sửa. Nhóm An ninh thì đổi hẳn quy trình: trước đây
> viết tài liệu thiết kế, code tạm, rồi bỏ luôn phần kiểm thử; nay yêu cầu mã
> giả trước rồi dẫn qua quy trình viết kiểm thử trước khi viết mã.
>
> Hai con số đo được: gỡ lỗi sự cố nhanh gấp ba lần, và một nhóm giảm tám mươi
> phần trăm thời gian tra cứu tài liệu kỹ thuật.
>
> Điều tôi rút ra cho đơn vị mình: giá trị lớn nhất rơi vào người chưa quen kho
> mã, sửa được lỗi trong module người khác viết mà không phải chờ đúng người đó
> rảnh.

### Slide 19 — Bài 2: kho mã lớn · ~70 giây

> Bài thứ hai sát với tình huống của chúng ta nhất: dự án cũ, nhiều module.
>
> Ba khuyến nghị. Đặt CLAUDE.md ở từng thư mục con thay vì gom hết vào gốc, tệp
> gốc chỉ ghi đường dẫn và các điểm dễ sai. Loại trừ những tệp không cần đọc,
> như tệp sinh tự động hay mã thư viện ngoài. Và rà lại cấu hình mỗi ba đến sáu
> tháng, vì quy tắc viết ra để bù khuyết điểm của mô hình cũ sẽ kìm hãm mô hình
> mới.
>
> Đề xuất của tôi: nên giao một người chịu trách nhiệm về cấu hình này, bắt đầu
> bằng danh sách kỹ năng được duyệt và quyền truy cập hạn chế, rồi mở rộng dần.

### Slide 20 — Bài 3: vòng kiểm chứng · ~70 giây

> Bài thứ ba là cách làm cụ thể cho nguyên tắc số hai mà tôi nói ở slide chín.
>
> Vòng kiểm chứng là việc công cụ tự kiểm tra kết quả trước khi báo hoàn thành.
> Cách tự viết một vòng rất đơn giản: liệt kê những chỗ anh chị phải sửa lại
> nhiều lần, viết nó ra thành lời như đang dặn một người mới vào nhóm, rồi lưu
> thành tệp trong thư mục skills.
>
> Một ví dụ cụ thể trong bài: từ chối mọi migration xoá cột mà không có bước chép
> dữ liệu bù. Một câu như vậy là đủ.
>
> Dấu hiệu để đưa lên áp dụng cho cả nhóm là khi anh chị thấy mình phải chạy
> kiểm tra đó sau mỗi lần thay đổi.

---

## Phần 6 — Rủi ro (slide 21)

### Slide 21 — Ba rủi ro · ~100 giây

Nói nghiêm túc, không né tránh. Phần này giữ uy tín cho cả buổi.

> Phần này tôi nói về mặt còn lại.
>
> Rủi ro thứ nhất, và theo tôi là lớn nhất, không phải là mã sai. Mã sai thì
> kiểm thử bắt được. Rủi ro lớn nhất là khối lượng thay đổi vượt quá khả năng rà
> soát. Một yêu cầu mơ hồ để chạy liên tục có thể sinh ra lượng thay đổi mà
> không ai duyệt kịp. Cách xử lý là chia nhỏ việc và duyệt kế hoạch trước.
>
> Thứ hai, mã đưa vào vận hành cần duyệt kỹ hơn, áp tiêu chuẩn thẩm định cao hơn
> so với mã do người trực tiếp viết. Dùng lệnh diff đọc kỹ trước mỗi lần commit.
>
> Thứ ba, hạn chế quyền truy cập. Không cấp toàn quyền vào máy chủ nội bộ hay cơ
> sở dữ liệu. Giữ mật khẩu và khoá API ngoài phiên làm việc, và tệp cấu hình
> biến môi trường thì tuyệt đối không đưa vào kho mã cũng như không dán vào nội
> dung trao đổi.

**Lưu ý:** không vội vàng ở slide này. Người nghe có thể đang lo đúng những điều
đó, trả lời thẳng sẽ chiếm được lòng tin.

---

## Phần 7 — Thay thế và triển khai (slide 22–23)

### Slide 22 — Chưa có tài khoản · ~90 giây

> Giờ đến phần dành cho anh em chưa có tài khoản Claude Code. Có hai đường.
>
> Đường thứ nhất là Google Antigravity, và đây là đường tôi khuyến nghị vì Google
> công bố miễn phí cho người phát triển. Ba bước: tải tại antigravity chấm google
> gạch chéo download, có bản cho cả macOS, Windows và Linux; đăng nhập bằng tài
> khoản Google; rồi mở thư mục dự án và giao việc trong Agent Manager. Agent
> Manager chạy nhiều tác tử song song, mỗi tác tử trả về danh sách việc và bản so
> sánh mã để anh chị rà trước khi nhận.
>
> Đường thứ hai là Codex của OpenAI, dành cho ai đã có sẵn gói ChatGPT trả phí.
> Lệnh cài gần giống hệt Claude Code, anh chị nhìn là nhận ra ngay. Lưu ý là
> Codex không có bản miễn phí.
>
> Và điều quan trọng nhất ở slide này nằm ở khung dưới: ba nguyên tắc tôi nói
> lúc nãy giữ nguyên giá trị với cả hai công cụ. Duyệt kế hoạch, khai báo tiêu
> chí kiểm chứng, giữ quyền dừng. Dùng công cụ nào cũng vậy.

### Slide 23 — Bắt đầu · ~70 giây

> Ba việc để bắt đầu ngay trong tuần này.
>
> Một, cài đặt, một dòng lệnh theo slide mười một. Hai, chạy lệnh init trên một
> dự án thật để sinh tệp CLAUDE.md. Ba, và đây là bước quan trọng nhất, giao cho
> nó một nhiệm vụ nhỏ **có kiểm thử đi kèm**, để nó tự kiểm chứng được.
>
> Đừng bắt đầu bằng việc lớn. Một việc nhỏ chạy thông từ đầu đến cuối sẽ cho anh
> chị cảm nhận đúng hơn mọi slide tôi vừa trình bày.
>
> Ban KHCNĐMST sẵn sàng hỗ trợ anh chị cài đặt và dựng tệp CLAUDE.md cho dự án
> đầu tiên. Xin cảm ơn anh chị đã lắng nghe.

---

## Câu hỏi có thể gặp

**"Nó có thay thế lập trình viên không?"**
Không, và slide 4 đã trả lời: phần việc đổi chứ không mất. Kỹ sư chuyển từ gõ mã
sang mô tả kết quả cần đạt và thẩm định kết quả. Phần thẩm định thì không giao
cho máy được, slide 9 đã nêu rõ loại tiêu chí nào bắt buộc phải có người duyệt.

**"Mã nguồn của mình có bị gửi ra ngoài không?"**
Trả lời theo đúng slide 21: nguyên tắc là hạn chế quyền truy cập, không cấp toàn
quyền vào máy chủ nội bộ hay cơ sở dữ liệu, và không đưa tệp cấu hình biến môi
trường vào nội dung trao đổi. [Nếu đơn vị đã có quy định riêng về dữ liệu thì
dẫn quy định đó].

**"Chi phí thế nào?"**
[Ban trả lời theo tình hình cấp phát thực tế]. Phần nói chắc chắn được: gói miễn
phí không dùng được, và ai chưa có tài khoản thì dùng Antigravity miễn phí theo
slide 22.

**"Kết quả nó làm ra có tin được không?"**
Đây là câu nên mừng khi được hỏi. Trả lời bằng nguyên tắc 2: đừng tin, hãy bắt
nó chứng minh. Khai báo lệnh kiểm thử và lint trong CLAUDE.md thì nó phải tự
chạy và tự lặp đến khi đạt mới được báo hoàn thành.

**"Tôi thử rồi, thấy không hơn gì công cụ gợi ý mã."**
Gần như chắc chắn là do dùng như công cụ gợi ý mã: hỏi từng đoạn nhỏ trong một
tệp. Mời họ thử lại theo slide 7 — giao một việc trọn vẹn có kiểm thử đi kèm, và
bật chế độ lập kế hoạch bằng Shift Tab.

## Phương án rút ngắn

Nếu bị cắt còn 20 phút, bỏ slide 3 và slide 5, rút phần bài viết thực tế
(slide 18–20) xuống còn một phút cho cả ba. Tuyệt đối giữ nguyên slide 4,
slide 8 đến 10, và slide 21.
