# Project-1-CS-TTNT
#### PROJECT 1 PSEUDU-CODE

##### Cấu trúc dữ liệu
```
struct Node{
  x,
  y,
  heuristic,
  Node* parent
};
```
##### Mở rộng Node
```
int check[size(Ma trận) * size(Ma trận)] = {0}
int step_X[] = {-1,-1,-1,0,1,1,1,0};
int step_Y[] = {-1,0,1,1,1,0,-1,-1};
function Mở_rộng(node, A){
  Node temp;
  int i = 0;
  loop do{
    if (A.x + step_X[i] và A.y + step_Y[i] thuộc ma trận && Ô đó có check = 0 && Ô đó không phải là chướng ngại vật){
      temp.x = A.x + step_X[i];
      temp.y = A.y + step_Y[i];
      temp.value = A.x * size(Ma trận) + A.y;
      temp.heuristic = Euclid(temp,Goal);
      temp.parent = A;
      A.Thêm_node(temp);
      Đánh dấu check = 1 là đã mở;
    }
    i += 1;
  }
}
```
##### Thuật toán A*
```
Node result[size(Ma trận) * size(Ma trận)];
<priority-queue> A
A.Thêm_node(Start)
result[Start.value] = -1;
loop do{
  if (A = rỗng)
    then return Thất_bại;
  Node temp = Lấy_node_ưu tiên nhất(A);
  result[temp.value] = temp.parent.value;
  if (temp = Goal)
    then return Lời_giải;
  Mở_rộng(temp,A);
}
```
##### Lời giải
```
function Lời_Giải(Goal){
  Node temp = Goal;
  printf("(%d,%d)", Goal.x, Goal.y);
  while (result[temp.parent.value] != -1){
    printf(" <-- ");
    printf("(%d,%d)", temp.parent.x, temp.parent.y);
    temp = temp.parent;
  }
}
```













