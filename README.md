# Project-1-CS-TTNT
#### PROJECT 1 PSEUDU-CODE

##### Cấu trúc dữ liệu
```
struct Node{
  int x,
  int y,
  int heuristic,
  int parent
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
    if (node.x + step_X[i] và node.y + step_Y[i] thuộc ma trận && Ô đó có check = 0 && Ô đó không phải là chướng ngại vật){
      temp.x = node.x + step_X[i];
      temp.y = node.y + step_Y[i];
      temp.heuristic = Euclid(temp,Goal);
      temp.parent = node.x*size(Ma trận) + node.y;
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
result[Start.x*size + Start.y] = -1;
loop do{
  if (A = rỗng)
    then return Thất_bại;
  Node temp = Lấy_node_ưu tiên nhất(A);
  result[temp.x*size + temp.y] = temp.parent;
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
  while (temp.parent != -1){
    printf(" <-- ");
    printf("(%d,%d)", result[temp.parent].x, result[temp.parent].y);
    temp = result[temp.parent];
  }
}
```













