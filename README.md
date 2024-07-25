# Thử mô phỏng lại trò chơi "Cắm cờ" THT toàn quốc bảng C1

## Tổng quan đề
Trò chơi “Cắm cờ” là trò chơi đối kháng cho hai đội

Game Master sẽ chuẩn bị một mê cung 40x40, với các cột/hàng đánh số từ 1 đến 40

Ô nằm giao giữa hàng i và cột j là ô $(i, j)$ có giá trị $A_{ij}$
- $A_{ij} = -1$ thì không thể đi vào được
- $A_{ij} \neq 1$ nếu cắm cờ thì đội sẽ nhận được số điểm tương ứng là Aij

Hai đội xuất phát tại hai vị trí (40, 1) và (40, 40). Trong t bước, mỗi đội sẽ đưa ra quyết định đi sang ô kề cạnh hoặc đặt cờ tại vị trí đang đứng

Đội có số điểm lớn nhất sẽ chiến thắng

### (***Những điều được liệt kê dưới đây không phải là kì thi chính thức***)
## Xây dựng chương trình

Đây là một dạng bài interactive

Trước khi trận đấu bắt đầu, bạn nhận được một chuỗi `UP` hoặc `DOWN` trên một dòng tương ứng với vị trị bắt đầu (40, 1) (40, 40)

Dòng tiếp theo bao gồm một số tự nhiên t $(1 \le t \le 1600)$, là số bước thực hiện trước khi kết thúc trò chơi

40 dòng tiếp theo, mỗi dòng chứa một dãy 40 số nguyên $A_{ij}$ $(-1 \le A_{ij} \le 10)$  là giá trị của ô bảng

Khi trận đấu bắt đầu, mỗi bước:
- Đầu tiên đưa ra quyết định di chuyển của bạn, in ra một chuỗi trong các chuỗi sau đây trên một dòng:
    - `PLACE_FLAG` để đặt cờ tại ô hiện tại $(x, y)$ (giả sử bạn đang ở ô $(x, y)$)
    - `MOVE_UP` di chuyển tới $(x, y-1)$
    - `MOVE_DOWN` di chuyển tới $(x, y+1)$
    - `MOVE_LEFT` di chuyển tới $(x-1, y)$
    - `MOVE_RIGHT` di chuyển tới $(x+1, y)$
- Sau đó bạn sẽ nhận được quyết định của đối phương bằng một trong các chuỗi trên
Sau t bước, trận đấu sẽ kết thúc và đưa ra người chiến thắng

Lưu ý:
- Nếu cả bạn và đối phương đều **đặt cờ tại cùng một ô** thì sẽ **xem như không làm gì**
- Nếu bạn cố gắng **di chuyển ra ngoài bảng** hoặc **di chuyển vào ô không đi vào được** thì sẽ **xem như không làm gì**
- Nếu bạn cố in ra **một chuỗi không đúng** thì sẽ **xem như không làm gì**

Ví dụ:

<table><thead>
    <tr>
        <th>You</th>
        <th>Game Master</th>
        <th>Opponent</th>
        <th>Bước</th>
    </tr></thead>
<tbody>
    <tr>
        <td colspan='2'>LEFT</td>
        <td></td>
        <td rowspan='4'>READY</td>
    </tr>
    <tr>
        <td></td>
        <td colspan='2'>RIGHT</td>
    </tr>
    <tr><td colspan='3'>2</td></tr>
    <tr>
        <td colspan='3'>
            <span style="white-space: pre-line">1 1 1 ...
            1 1 1 ...
            .
            .
            .
            1 1 1 ...
            (full 1)
            </span>
        </td>
    </tr>
    <tr>
        <td>PLACE_FLAG</td>
        <td></td>
        <td>PLACE_FLAG</td>
        <td rowspan='3'>1</td>
    </tr>
    <tr>
        <td colspan='2'>PLACE_FLAG</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td colspan='2'>PLACE_FLAG</td>
    </tr>
    <tr>
        <td>MOVE_RIGHT</td>
        <td></td>
        <td>MOVE_UP</td>
        <td rowspan='3'>2</td>
    </tr>
    <tr>
        <td colspan='2'>MOVE_UP</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td colspan='2'>MOVE_RIGHT</td>
    </tr>
    <tr>
        <td colspan='4'>DRAW!</td>
    </tr>
</tbody>
</table>


## `fight.py`
Lưu file code của hai đội trong file `code1.cpp` và `code2.cpp`

Sau khi chạy chương trình python, điểm và kết quả của của hai đội sẽ được hiển thị

Lưu ý chương trình này **không có môi trường sandbox**, tức có nghĩa chương trình của hai đội **có thể chạy câu lệnh không an toàn** (vi gút vi gútt)

